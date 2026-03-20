# Digital Forensics Reference Library

> Source: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (Apache 2.0)
> Curated for `maycrest-automate:digital-forensics-analyst`

---

## Quick Lookup

### By Evidence Type

| Evidence Type | Key Artifacts | Primary Tools |
|--------------|---------------|---------------|
| Memory (RAM) | Running processes, network connections, injected code, credentials | Volatility 3, WinPmem, AVML |
| Disk Image | File system, deleted files, MFT, unallocated space | Autopsy, Sleuth Kit, FTK |
| Windows Event Logs | Authentication, process creation, services, PowerShell | Chainsaw, Hayabusa, EvtxECmd |
| Windows Registry | Persistence, user activity, USB devices, installed software | RegRipper, Registry Explorer, python-registry |
| Browser Artifacts | History, downloads, cookies, searches, saved passwords | Hindsight, direct SQLite parsing |
| Timeline | Unified chronological reconstruction from all sources | Timesketch, Plaso (log2timeline) |

### By Operating System

| OS | Key Artifact Locations |
|----|----------------------|
| Windows | `C:\Windows\System32\winevt\Logs\` (EVTX), `C:\Windows\System32\config\` (Registry), `%LOCALAPPDATA%\Google\Chrome\User Data\Default\` (Browser), Prefetch, AmCache, ShimCache |
| Linux | `/var/log/` (syslog, auth.log), `~/.config/google-chrome/Default/` (Browser), `/var/log/audit/` (auditd), `~/.bash_history` |
| macOS | `~/Library/Application Support/Google/Chrome/Default/` (Browser), `/var/log/`, Unified Logging (`log show`) |

### Critical Windows Event IDs

| Event ID | Log | Meaning |
|----------|-----|---------|
| 4624 | Security | Successful logon (check LogonType: 2=interactive, 3=network, 10=RDP) |
| 4625 | Security | Failed logon |
| 4648 | Security | Explicit credential logon (Pass-the-Hash indicator) |
| 4672 | Security | Special privileges assigned to new logon |
| 4688 | Security | New process created (with command line if auditing enabled) |
| 4697 | Security | Service installed |
| 4698 | Security | Scheduled task created |
| 4720 | Security | User account created |
| 4728/4732/4756 | Security | Member added to global/local/universal security group |
| 1102 | Security | Audit log cleared (anti-forensics indicator) |
| 4104 | PowerShell | Script block logging (PowerShell execution content) |

---

## Detailed References

### Memory Forensics with Volatility 3

**Acquisition:**
```bash
# Windows
winpmem_mini_x64.exe output.raw          # WinPmem
DumpIt.exe                                # DumpIt (auto-names)

# Linux
./avml output.lime                        # AVML (Microsoft)
```

**Core analysis workflow:**
```bash
# 1. Identify OS
vol -f memory.raw windows.info

# 2. Process analysis
vol -f memory.raw windows.pslist          # Active processes
vol -f memory.raw windows.pstree          # Parent-child tree
vol -f memory.raw windows.psscan          # Hidden/unlinked processes (rootkit detection)

# 3. Network connections
vol -f memory.raw windows.netscan         # Active and recent connections

# 4. Malware detection
vol -f memory.raw windows.malfind         # Injected code (PAGE_EXECUTE_READWRITE)
vol -f memory.raw windows.dlllist --pid 3847  # DLLs loaded by suspicious process
vol -f memory.raw windows.yarascan --yara-file malware_rules.yar

# 5. Credential extraction
vol -f memory.raw windows.hashdump        # Password hashes
vol -f memory.raw windows.cmdline         # Command line history

# 6. Artifact extraction
vol -f memory.raw windows.handles --pid 3847  # File, registry, mutex handles
vol -f memory.raw windows.dumpfiles --pid 3847
vol -f memory.raw windows.registry.hivelist
```

**Process anomaly indicators:**
- `svchost.exe` without `-k` parameter or wrong parent (should be `services.exe`)
- `csrss.exe` or `lsass.exe` with abnormal parent
- Misspelled names: `scvhost.exe`, `lssas.exe`
- Processes spawned by `outlook.exe`, `winword.exe`, `excel.exe`
- Multiple instances of singletons (`lsass.exe`, `smss.exe`)
- Processes in `psscan` but NOT in `pslist` = hidden by rootkits

### Disk Image Analysis with Autopsy/Sleuth Kit

**Image verification and partition mapping:**
```bash
img_stat /cases/evidence.dd               # Image info
mmls /cases/evidence.dd                    # Partition layout
fls -o 2048 /cases/evidence.dd            # List files (offset = partition start)
```

**File recovery:**
```bash
fls -rd -o 2048 /cases/evidence.dd        # List deleted files
icat -o 2048 /cases/evidence.dd 14523 > recovered.docx  # Recover by inode
tsk_recover -o 2048 -d /Users/suspect/Documents \
  /cases/evidence.dd /cases/recovered/     # Bulk recovery
istat -o 2048 /cases/evidence.dd 14523    # File metadata (MAC timestamps)
```

**Autopsy Ingest Modules (enable all for comprehensive analysis):**
Recent Activity, Hash Lookup (NSRL), File Type ID, Keyword Search, Email Parser, Extension Mismatch Detector, Exif Parser, Encryption Detection, Embedded File Extractor, Data Source Integrity.

**Timeline generation:**
```bash
fls -r -m "/" -o 2048 /cases/evidence.dd > bodyfile.txt
mactime -b bodyfile.txt -d > timeline.csv
mactime -b bodyfile.txt -d 2024-01-15..2024-01-20 > incident_timeline.csv
```

### Windows Event Log Analysis

**Collection:**
```bash
# Key logs to extract from forensic image
mount -o ro,loop,offset=$((2048*512)) evidence.dd /mnt/evidence
cp /mnt/evidence/Windows/System32/winevt/Logs/*.evtx /cases/evtx/
sha256sum /cases/evtx/*.evtx > /cases/evtx/evtx_hashes.txt
```

**Sigma-based detection with Chainsaw:**
```bash
chainsaw hunt /cases/evtx/ \
  -s /opt/chainsaw/sigma/rules/ \
  --mapping /opt/chainsaw/mappings/sigma-event-logs-all.yml \
  --csv --output /cases/analysis/chainsaw_results/

chainsaw search /cases/evtx/ -s "mimikatz" --json
chainsaw search /cases/evtx/ -e 4688 --json   # Process creation events
```

**Fast timeline with Hayabusa:**
```bash
hayabusa csv-timeline -d /cases/evtx/ -o hayabusa_timeline.csv -p verbose
hayabusa csv-timeline -d /cases/evtx/ -o critical.csv --min-level critical
hayabusa logon-summary -d /cases/evtx/ -o logon_summary.csv
```

**Attack pattern detection:**
- **Pass-the-Hash:** Event 4624, LogonType 9 with NTLM authentication
- **Lateral movement:** Event 4624, LogonType 3 (network) with NTLM from unusual IPs
- **Privilege escalation:** Event 4672 for unexpected users, 4728/4732 group changes
- **Anti-forensics:** Event 1102 (Security log cleared), 104 (System log cleared)
- **PowerShell attacks:** Event 4104 (Script Block Logging), encoded commands in 4688

### Windows Registry Forensics

**Hive locations:**
```bash
# System hives: C:\Windows\System32\config\
SAM, SYSTEM, SOFTWARE, SECURITY, DEFAULT

# User hives:
C:\Users\<username>\NTUSER.DAT
C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat
```

**Automated extraction with RegRipper:**
```bash
rip.pl -r NTUSER.DAT -f ntuser > ntuser_report.txt
rip.pl -r SYSTEM -f system > system_report.txt
rip.pl -r SOFTWARE -f software > software_report.txt
rip.pl -r SAM -f sam > sam_report.txt

# Specific plugins
rip.pl -r NTUSER.DAT -p userassist    # Program execution history
rip.pl -r SYSTEM -p usbstor           # USB device history
rip.pl -r NTUSER.DAT -p recentdocs    # Recent documents
rip.pl -r SOFTWARE -p uninstall        # Installed software
```

**Key registry artifacts:**
| Artifact | Location | Evidence Value |
|----------|----------|---------------|
| Autorun/Persistence | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` | Malware persistence |
| UserAssist | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | Program execution with timestamps (ROT13 encoded) |
| ShimCache | `SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache` | Executed programs |
| BAM/DAM | `SYSTEM\CurrentControlSet\Services\bam\State\UserSettings` | Recent program execution (Win10+) |
| USB Devices | `SYSTEM\CurrentControlSet\Enum\USBSTOR` | Connected devices with serial numbers |
| MRU Lists | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` | Recently accessed files |
| Typed URLs | `HKCU\Software\Microsoft\Internet Explorer\TypedURLs` | Browser URL history |

### Browser Forensics with Hindsight

```bash
# Run Hindsight against Chrome profile
hindsight.exe -i "C:\Evidence\Chrome\Default" -o /output/analysis -b Chrome
hindsight.exe -i "/path/to/profile" -o /output --cache  # Include cache parsing
```

**Chrome timestamp conversion:** Microseconds since 1601-01-01 (WebKit format). Convert: `datetime((ts/1000000)-11644473600, 'unixepoch')`.

**Browser profile paths:** Chrome Windows: `%LOCALAPPDATA%\Google\Chrome\User Data\Default\`, Edge: `%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\`, Brave: `%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\`

### Timeline Reconstruction with Timesketch

**Data ingestion:**
```bash
# Plaso (comprehensive artifact parsing)
log2timeline.py --storage-file evidence.plaso /path/to/disk/image
log2timeline.py --parsers "winevtx,prefetch,amcache,shimcache,userassist" \
  --storage-file full_analysis.plaso /path/to/mounted/image/

# Import into Timesketch
timesketch_importer -s "Case-2025-001" -t "Endpoint-WKS01" evidence.plaso
timesketch_importer -s "Case-2025-001" -t "Quick-Triage" events.csv
```

**Timesketch search queries:**
```
source_short:Security AND message:"john.admin"
data_type:"windows:evtx:record" AND event_identifier:4104
source_short:Security AND event_identifier:4624 AND xml_string:"LogonType\">3"
datetime:[2025-01-15T00:00:00 TO 2025-01-15T23:59:59]
tag:"suspicious" OR tag:"lateral_movement"
```

---

## Tool Guidance

| Tool | Purpose | Key Usage |
|------|---------|-----------|
| **Volatility 3** | Memory forensics framework | `vol -f dump.raw windows.pslist/psscan/malfind/netscan` |
| **Autopsy** | GUI disk image analysis | Ingest modules, keyword search, timeline, reporting |
| **Sleuth Kit** | CLI disk forensics | `fls`, `icat`, `mmls`, `mactime` for timeline |
| **Chainsaw** | Sigma-based EVTX analysis | `chainsaw hunt` with Sigma rules for threat detection |
| **Hayabusa** | Fast EVTX timeline generator | `hayabusa csv-timeline` with severity filtering |
| **RegRipper** | Automated registry extraction | `rip.pl -r HIVE -f profile` with 200+ plugins |
| **Hindsight** | Chromium browser forensics | Unified timeline from History, Cookies, Downloads, Cache |
| **Timesketch** | Collaborative timeline analysis | Plaso ingestion, Sigma analyzers, investigation stories |
| **Plaso (log2timeline)** | Multi-source artifact parsing | `log2timeline.py` with 100+ parsers into `.plaso` files |
| **WinPmem / DumpIt** | Windows memory acquisition | Raw dump before endpoint isolation |
| **AVML** | Linux memory acquisition | Microsoft's open-source Linux RAM capture |
| **YARA** | Pattern matching in memory/files | Scan memory dumps against malware signature rules |
| **KAPE** | Automated triage collection | Evidence collection including event logs, registry, browser |
| **EvtxECmd** | Eric Zimmerman EVTX parser | CSV/JSON output with field mapping |
| **python-evtx** | Python EVTX parsing library | Custom event parsing and filtering scripts |

### Evidence Acquisition Checklist

1. Document: target host, RAM size, timestamp, analyst name, tool used
2. Capture memory FIRST (volatile evidence lost on shutdown)
3. Hash all evidence files immediately (SHA-256)
4. Mount disk images read-only (`-o ro`)
5. Maintain chain of custody documentation throughout
6. Copy registry hives and transaction logs together (for dirty hive recovery)
