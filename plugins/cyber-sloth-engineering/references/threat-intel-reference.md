# Threat Intelligence Reference Library

> Source: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (Apache 2.0)
> Curated for `cyber-sloth-engineering:threat-intelligence-analyst`

---

## Quick Lookup

### By Intelligence Type

| Intel Type | Sources | Output Format |
|-----------|---------|---------------|
| Strategic | Government advisories (CISA, NSA), vendor reports (Mandiant, CrowdStrike) | Executive briefings, threat landscape assessments |
| Tactical | ATT&CK mappings, Sigma rules, detection signatures | SIEM rules, detection engineering priorities |
| Operational | Campaign analysis, APT group profiling, infrastructure correlation | Threat actor dossiers, IOC feeds |
| Technical | IOCs (hashes, IPs, domains), malware samples, YARA rules | STIX bundles, MISP events, blocklists |

### By Framework

| Framework | Purpose | Key Elements |
|-----------|---------|-------------|
| MITRE ATT&CK | Adversary behavior taxonomy | 14 Tactics, 200+ Techniques, 140+ Groups |
| Diamond Model | Intrusion analysis | Adversary, Infrastructure, Capability, Victim |
| Cyber Kill Chain | Attack phase modeling | Recon through Actions on Objectives |
| STIX 2.1 | Structured threat data exchange | SDOs (indicator, threat-actor, malware, campaign) + SROs |
| TAXII 2.1 | Threat intel transport protocol | Server discovery, collection enumeration, object retrieval |
| TLP | Sharing classification | RED (named recipients), AMBER (org), GREEN (community), CLEAR (public) |

### By ATT&CK Tactic (14 Enterprise Tactics)

| Tactic | ID | Example Techniques |
|--------|----|--------------------|
| Reconnaissance | TA0043 | T1593 Search Open Websites, T1589 Gather Victim Identity |
| Resource Development | TA0042 | T1583 Acquire Infrastructure, T1587 Develop Capabilities |
| Initial Access | TA0001 | T1566 Phishing, T1078 Valid Accounts, T1190 Exploit Public App |
| Execution | TA0002 | T1059 Command/Script Interpreter, T1204 User Execution |
| Persistence | TA0003 | T1053 Scheduled Task, T1547 Boot/Logon Autostart |
| Privilege Escalation | TA0004 | T1068 Exploitation for Priv Esc, T1548 Abuse Elevation |
| Defense Evasion | TA0005 | T1055 Process Injection, T1027 Obfuscated Files |
| Credential Access | TA0006 | T1003 OS Credential Dumping, T1558 Kerberos Tickets |
| Discovery | TA0007 | T1087 Account Discovery, T1018 Remote System Discovery |
| Lateral Movement | TA0008 | T1021 Remote Services, T1550 Use Alternate Auth |
| Collection | TA0009 | T1560 Archive Data, T1213 Data from Info Repositories |
| Command and Control | TA0011 | T1071 Application Layer Protocol, T1573 Encrypted Channel |
| Exfiltration | TA0010 | T1041 Exfil Over C2, T1048 Exfil Over Alt Protocol |
| Impact | TA0040 | T1486 Data Encrypted for Impact, T1489 Service Stop |

---

## Detailed References

### CTI Lifecycle

1. **Planning & Direction** -- Define intelligence requirements, priority information needs, and collection plan
2. **Collection** -- Gather data from OSINT, HUMINT, vendor feeds, MISP communities, TAXII servers
3. **Processing** -- Normalize IOCs, parse STIX bundles, validate indicator confidence, apply TLP markings
4. **Analysis** -- Map to ATT&CK, build actor profiles, correlate infrastructure, assess attribution confidence
5. **Dissemination** -- Publish to SIEM/EDR, generate analyst reports, share via TAXII/MISP, brief stakeholders
6. **Feedback** -- Measure detection coverage, track gap closures, refine collection priorities

### APT Profiling Methodology

**Profile components:** Aliases across vendors, suspected origin/sponsorship, motivation (espionage, financial, hacktivism), targeted sectors and geographies, known campaigns, TTPs mapped to ATT&CK, toolset and malware families, infrastructure patterns, historical timeline.

**Structured profiling with STIX 2.1:**
```python
from stix2 import ThreatActor, IntrusionSet, Relationship, Bundle

threat_actor = ThreatActor(
    name="APT29",
    aliases=["Cozy Bear", "Midnight Blizzard", "NOBELIUM", "The Dukes"],
    roles=["agent"],
    sophistication="strategic",
    resource_level="government",
    primary_motivation="organizational-gain",
    threat_actor_types=["nation-state"],
)

intrusion_set = IntrusionSet(
    name="APT29",
    first_seen="2008-01-01T00:00:00Z",
    goals=["espionage"],
    resource_level="government",
)

bundle = Bundle(objects=[threat_actor, intrusion_set,
    Relationship(relationship_type="attributed-to",
                 source_ref=intrusion_set.id,
                 target_ref=threat_actor.id)])
```

### ATT&CK Navigator Layer Generation

```python
from attackcti import attack_client

lift = attack_client()
techniques = lift.get_techniques_used_by_group("G0016")  # APT29

# Build Navigator layer JSON
layer = {
    "name": "APT29 TTP Coverage",
    "versions": {"attack": "16.1", "navigator": "5.1.0", "layer": "4.5"},
    "domain": "enterprise-attack",
    "techniques": [{
        "techniqueID": tech_id,
        "color": "#ff6666",
        "score": 100,
        "enabled": True,
    } for tech_id in extracted_ids],
    "gradient": {"colors": ["#ffffff", "#ff6666"], "minValue": 0, "maxValue": 100},
}
# Import into ATT&CK Navigator at mitre-attack.github.io/attack-navigator/
```

### Detection Gap Analysis

Compare actor techniques against your detection capabilities:
```python
actor_techniques = set(technique_map.keys())     # From ATT&CK group data
detected_techniques = {"T1059", "T1071", "T1566"} # Your detection coverage

gaps = actor_techniques - detected_techniques
coverage_pct = len(actor_techniques & detected_techniques) / len(actor_techniques) * 100
# Prioritize gap closure by: frequency across threat groups, data source availability
```

### STIX/TAXII Feed Processing

**Discovery and ingestion:**
```python
from taxii2client.v21 import Server, as_pages
from datetime import datetime, timedelta, timezone

server = Server("https://cti.example.com/taxii/", user="apiuser", password="apikey")
api_root = server.api_roots[0]
for collection in api_root.collections:
    print(collection.id, collection.title, collection.can_read)

# Incremental polling (last 24 hours)
added_after = datetime.now(timezone.utc) - timedelta(hours=24)
for bundle_page in as_pages(collection.get_objects, added_after=added_after, per_request=100):
    process_bundle(bundle_page)
```

**Object routing:**
- `indicator` objects -> SIEM lookup tables, firewall blocklists
- `malware` objects -> EDR threat intelligence library
- `threat-actor` / `campaign` -> TIP for analyst context
- `course-of-action` -> SOAR playbook triggers

**Common pitfalls:** STIX 2.0 vs 2.1 schema incompatibility (check `spec_version`), missing TAXII pagination (`next` link header), clock skew on `added_after`, sharing TLP:RED content inadvertently through automated pipelines.

### Indicator Management with MISP

```python
from pymisp import PyMISP
misp = PyMISP('https://misp.local', 'YOUR_API_KEY', ssl=False)

# Search recent IOCs
result = misp.search(controller='events',
    date_from=(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
    type_attribute='ip-dst', to_ids=True, pythonify=True)

# Export as STIX 2.1 for sharing
stix_output = misp.search(controller='events', return_format='stix2',
    tags=['tlp:white'], published=True)

# Export as Suricata rules for IDS
suricata_rules = misp.search(controller='attributes', return_format='suricata',
    to_ids=True, type_attribute=['ip-dst', 'domain', 'url'])
```

---

## Tool Guidance

| Tool | Purpose | Key Usage |
|------|---------|-----------|
| **ATT&CK Navigator** | TTP visualization and gap analysis | Load JSON layers, overlay threat actor vs. detection coverage |
| **MISP** | IOC sharing and correlation platform | `pymisp` API for feed management, event search, STIX export |
| **OpenCTI** | Knowledge graph CTI platform | STIX 2.1 native, MISP connector, GraphQL API |
| **TheHive + Cortex** | Case management + automated enrichment | Alert creation from high-confidence indicators, analyzer plugins |
| **attackcti** | Python ATT&CK data queries | `get_techniques_used_by_group()`, `get_enterprise_techniques()` |
| **stix2** | STIX object creation and validation | Parse bundles, create indicators, validate required fields |
| **taxii2-client** | TAXII 2.1 server interaction | Server discovery, collection enumeration, paginated object fetch |
| **SpiderFoot** | OSINT infrastructure correlation | Automated scanning: DNS, WHOIS, Shodan, VirusTotal, CertSpotter |
| **Maltego** | Link analysis and visualization | Entity relationship graphing for infrastructure correlation |
| **AlienVault OTX** | Community threat intel | Pulse search API, IOC retrieval, tag-based queries |

### TIP Architecture (Docker Compose Stack)

| Component | Image | Role |
|-----------|-------|------|
| Elasticsearch | `elasticsearch:8.12.0` | Storage and search backend |
| Redis | `redis:7` | Task queue management |
| RabbitMQ | `rabbitmq:3-management` | Message broker |
| MISP | `misp/misp-docker` | IOC management and sharing |
| OpenCTI | `opencti/platform:6.4.4` | Knowledge graph analysis |
| TheHive | `strangebee/thehive:5.3` | Incident case management |
| Cortex | `thehiveproject/cortex:3.1.8` | Automated IOC enrichment |

### OSINT Sources for Threat Actor Profiling

| Source Category | Examples |
|----------------|---------|
| Vendor Reports | Mandiant, CrowdStrike, Recorded Future, Talos |
| Government Advisories | CISA, NSA, FBI joint advisories |
| Malware Repositories | VirusTotal, MalwareBazaar, Malpedia |
| Community Feeds | CIRCL OSINT, botvrij.eu, abuse.ch (URLhaus, Feodo Tracker) |
| Infrastructure Intel | Shodan, Censys, PassiveTotal/RiskIQ, Certificate Transparency |
| Code/Paste Sites | GitHub, GitLab, Pastebin, GitHub Gists |

### Cross-Group Comparison

```python
groups = {"G0016": "APT29", "G0007": "APT28", "G0032": "Lazarus Group"}
group_techniques = {}
for gid, gname in groups.items():
    techs = lift.get_techniques_used_by_group(gid)
    group_techniques[gname] = {extract_id(t) for t in techs}

common = set.intersection(*group_techniques.values())
# Techniques common to all groups = highest priority for detection
```
