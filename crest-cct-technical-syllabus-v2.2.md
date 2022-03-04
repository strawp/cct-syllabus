---

ref: SYL_CCT_V2.0
version: 2.2
status: Public Release
issue_date: 2017-05-17
issued_by: CREST Technical Committee and Assessors Panel

---

# Technical Committee and Assessors Panel

# CREST Certified Tester Technical Syllabus

This document and any information therein are confidential property of CREST and without
infringement neither the whole nor any extract may be disclosed, loaned, copied or used for
manufacturing, provision of services or other purposes whatsoever without prior written consent
of CREST, and no liability is accepted for loss or damage from any cause whatsoever from the
use of the document. CREST retain the right to alter the document at any time unless a written
statement to the contrary has been appended.

## Table of Contents

[TOC]


## Version History

| Version | Date              | Authors                                 | Status          |
| ------- | ----------------- | --------------------------------------- | --------------- |
| 1.0     | 27 May 2016       | Technical Committee and Assessors Panel | Internal Review |
| 2.0     | 3 June 2016       | Technical Committee and Assessors Panel | Public Release  |
| 2.1     | 30 September 2016 | Technical Committee and Assessors Panel | Public Release  |
| 2.2     | 16 May 2017       | Technical Committee and Assessors Panel | Public Release  |


## Document Review

| Reviewer | Position                              |
| -------- | ------------------------------------- |
| Chair    | Technical Committee / Assessors Panel |
| Chair    | CREST Board                           |


## Introduction

The technical syllabus identifies at a high level the technical skills and knowledge that CREST expects
candidates to possess for the Certification Examinations. There are two alternate Certification Examinations
for the Crest Certified Tester (CCT) certification.

### Crest Certified Tester (CCT)

- The (CCT) Infrastructure Certification Examination tests candidates’ knowledge and expertise in
  assessing operating systems, common network services and general network infrastructure security.

- The (CCT) Web Application Certification Examination tests candidates’ knowledge and expertise in
  assessing web applications.

Both Certification Examinations also cover a common set of core skills and knowledge; success at either will
confer CREST Certified Tester status to the individual.

## Certification Examination Structure

### Crest Certified Tester (CCT)

The Certification Examination has two components: a written paper and a practical assessment. The written
paper consists of one section: a set of multiple choice questions. The practical assessment tests candidates’
hands-on penetration testing methodology and skills against reference networks, hosts and applications.
The Notes for Candidates (CCT) document for the Certification Examinations provides further information
regarding the Certification Examinations in general and the skill areas that will be assessed within the
practical components.

## Syllabus Structure

The syllabus is divided into ten knowledge groups (Appendices A to J below), each of which is subdivided
into specific skill areas.

For each skill area, CREST has indicated where and how the area will be assessed: in which Certification
Examination (Application or Infrastructure) and in which component (Written Multiple Choice or Practical).

It should be noted that at the Certified level, CREST expect candidates to have a good working
understanding of technologies across both disciples in order to support client engagements and scoping. As
such **MC** will appear in all syllabus areas for both types of exam.

Within the tables, the following acronyms apply:

- **CCT ACE** Application Certification Examination
- **CCT ICE** Infrastructure Certification Examination
- **MC** Written Multiple Choice
- **P** Practical

# Appendices

## Appendix A: Soft Skills and Assessment Management

### A1 Engagement Lifecycle

- ACE: MC
- ICE: MC
- confidence: 5

> Benefits and utility of penetration testing to the client.
>
> Structure of penetration testing, including the relevant processes and procedures.
>
> Concepts of infrastructure testing and application testing, including black box and white box formats.
>
> Project closure and debrief

### A2 Law & Compliance

- ACE: MC
- ICE: MC
- confidence: 4

> Knowledge of pertinent UK legal issues:
>
> - Computer Misuse Act 1990
>
> - Human Rights Act 1998
>
> - Data Protection Act 1998
>
> - Police and Justice Act 2006
>
>
> Impact of this legislation on penetration testing activities.
>
> Awareness of sector-specific regulatory issues.

#### Revelant Key legislation:

- CMA 1990 Section 1: Unauthorised access to a computer
- HRA 1998 Article 8: Right to respect for private life, how data is held and protected
- DPA 1998:
  - Section 7: People can request to view data an org holds on them
  - Section 10: Data cannot be used for damage or distress
  - Section 11: Data cannot be used for direct marketing
  - Section 14: Request destruction of data
  - Schedule 1: How data is collected / held
  - Exceptions:
    - Section 28: In case of National Security
    - Section 29: Crime and tax
    - Section 36: Domestic use 
- PJA 2006:
  - Section 35: Unauthorised access to computer material
  - Section 36: Unauthorised intent to impair operation
  - Section 37: Making, supplying, obtaining articles for use in computer misuse offences
  - Section 38: Transitional and saving provision
- GDPR 2018 Article 15: Subject Access Requests free
- DPA 2018: De-anonymising and unlawfully obtaining data now criminal offences

#### Computer Misuse Act 1990

- Created out of necessity as no existing laws covered computer misuse after R v Gold & Schifreen case successfully appealed forgery and counterfeiting convictions
- Jurisdiction if computer OR person is in UK at time of offence
- Section 1: Unauthorised access to a computer 
  - Guilty if:
    - Intent to secure access to any program or data held in any computer
    - Access he intends to secure is unauthorised
    - He *knows* at the time that this is the case
  - Punishable by £5000 or 6 months imprisonment
  - Knowledge and intent
  - Attempt sufficient
  - No requirement to show damages
- Section 2: Unauthorised access to a computer to commit further offences
  - More serious crime
  - e.g. blackmailer hacking to find evidence of affair
  - Serious crime doesn't have to be carried out, just intent to do so
  - 5 years / unlimited fine
- Section 3: Unauthorised acts with intent to impair/modification of computer
  - Intent and knowledge to be guilty
  - Virus, ransomware, DoS
  - Max 5 years, unlimited fine

#### Criminal Justice Act 1998

- Amended Computer Misuse Act
- Actually just seems to have removed some subsections

#### Human Rights Act 1998

- Derived from European Convention on Human Rights
- Ability to argue human rights in a British court with the delay and cost of going to European court
- Technically only applies to public bodies, but can be used between citizens as it applies to the court, which is a public body and the judge therefore must act in compatibility with it
- Article 8: Right to respect for private and family life
  - Everyone has the right to respect for **his private and family life**, his home and **his correspondence**.
  - There shall be no interference by a public authority with the exercise of this right except such as is in accordance with the law and is necessary in a democratic society in the interests of national security, public safety or the **economic well-being of the country**, for the **prevention of disorder or crime**, for the protection of health or morals, or for the **protection of the rights and freedoms of others**.
  - Private life defined as:
    - Your sexuality
    - Your body
    - Personal identity
    - **How personal information is held and protected**
  - Breaches might include:
    - Surveillance of home
    - Phone tapping, monitoring emails and internet, CCTV
    - Disclosing personal information to others without consent
- An individual can be monitored on behalf of their company due to exceptions in place in the Data Protection Act (1998) - performance of a contract, assuming their employment contract states this

#### Data protection act 1998

- Replaced Data Protection Act 1984, Access to Personal Files Act 1987
- Implemented EU Data Protection Directive 1995
- Scope
  - Personal data = anything identifying
    - Name and address, phone, email
  - Rights
    - View data an organisation holds on them (section 7) for a modest fee
    - Request correction to that data or have it destroyed (section 14)
    - Data cannot be used in any way to cause damage or distress (section 10)
    - Cannot be used for direct marketing (section 11)
- Principles (schedule 1)
  - Must be processed and obtained lawfully
  - Must be obtained only for lawful purposes
  - Adequate, relevant and not excessive
  - Accurate, up to date
  - Not kept longer than necessary
  - Appropriate technical measures against accidental processing, loss, damage to data
  - Cannot be transferred outside the EEA unless equivalent laws are in place in that country
- Conditions
  - Consent
  - Performance of a contract 
  - Legal obligation
  - Necessary to protect vital interests of the data subject
  - Necessary to carry out public functions
- Exceptions
  - National security (section 28)
  - Crime and tax (section 29)
  - Domestic purposes - your own family (section 36)
- Individuals can make a Subject Access Request to get all data about them from an organisation for £10
  - Following GDPR, this is now free
 - Freedom of Information Act 2000
   - Modified DPA for public bodies
   - Not really relevant to private organisations
 - Police and Justice Act 2006
   - Amends Computer Misuse Act
   - Extension of Police Act 1996 to include:
     - Section 35: Unauthorised access to computer material
     - Section 36: Unauthorised intent to impair operation
     - Section 37: Making, supplying, obtaining articles for use in computer misuse offences
     - Section 38: Transitional and saving provision

#### GDPR 2018

- EU legislation
- Data Protection Principles
  - Processed fairly and lawfully
  - Collected for specified legitimate and explicit purposes
  - Limited to what is necessary
  - Accurate and up-to-date
  - Kept no longer than necessary
  - Processed with appropriate security (based on risk assessments)
- Personal data
- All companies knowingly dealing with EU citizens must comply
- Terms
  - Data Subject
  - Data Controller
  - Data Processor
  - Portability
  - Rectification
  - Erasure
- Lawful basis to process data
  - Consent
  - Performance of a Contract
  - Legal Necessity
  - Vital Interests (life saving)
  - Public Interest
  - Legitimate Interest (e.g. customer relationship)
- Requesting personal data (access request) is now free, can be via any channel
  - Article 15 

#### Data Protection Act 2018

- Adds to GDPR
- Criminalises offenses relating to personal data
  - Unlawfully obtaining personal data
  - Re-identification of de-identified personal data

#### CREST code of conduct

- 2.1 Promotion of good practices
- 2.2 Professional representation
- 2.3 CREST assignments
  - Act professionally
  - Use appropriate tools and techniques
- 2.4 Regulations must be followed
- 2.5 Must maintain technical competencies
- 2.6 Respect the interests of the client
- 2.7 Sanctions may include, barring, revocation of qualifications, legal action
- 2.8 Ethics
  - Honesty
  - Prohibition of bribery
  - Fair competition
  - Integrity
  - Compliance - bring any breach to attention of CREST
 - Complaints procedure
   - Principles
     - Investigated competently, diligently, impartially
     - Not reviewed by any subjects of the complaint
     - 8 weeks resolution
     - Issues should be resolved with members as first point, only referred to CREST as a last resort
   - Measures
     - CREST makes complaints process known to client, NDA signed
     - Formal complaint provided in agreed format
     - Member notified of complaint
     - Complaint reviewed against code of conduct
     - Viewpoint report to member
     - Response to report
     - CREST president gives set of actions and dates
     - Legal action or qualification revoked: CREST Executive involved, further NDAs
     - Industry experts may be involved
     - Recommendation report issued to member
     - Summary report to client
     - If CHECK and suspension, may inform CESG / NCSC
     - Recommendations enacted
     - Notice given to client when measures concluded

### A3 Scoping

- ACE: MC
- ICE: MC
- confidence: 5

> Understanding client requirements.
>
> Scoping project to fulfil client requirements.
>
> Accurate timescale scoping.
>
> Resource planning.

### A4 Understanding Explaining and Managing Risk

- ACE: MC
- ICE: MC
- confidence: 3

> Knowledge of additional risks that penetration testing can present.
>
> Levels of risk relating to penetration testing, the usual outcomes of such risks materialising and how to mitigate the risks.
>
> Effective planning for potential DoS conditions.

How are risks planned / managed in an engagement

- Experience, common sense
- Ensure client understands inherent risks of assurance testing
- Always live systems
- Tiered architecture
  - Primary: Target systems, just try and be read only, get authority
  - Secondary: Servers, won't try and abuse, need authority
  - Tertiary: Laptops, desktops are tertiary systems - do whatever
- Agreed escalation path to communicate issues

### A5 Record Keeping, Interim Reporting & Final Results

- ACE: MC, P
- ICE: MC, P
- confidence: 4

> Understanding reporting requirements.
>
> Understanding the importance of accurate and structured record keeping during the engagement.



## Appendix B: Core Technical Skills

### B1 IP Protocols

- ACE: MC
- ICE: MC
- confidence: 3

> IP protocols: IPv4 and IPv6, TCP, UDP and ICMP.
>
> Awareness that other IP protocols exist.

### B2 Network Architectures

- ACE: MC
- ICE: MC
- confidence: 4

> Varying networks types that could be encountered during a penetration test:
>
> - CAT 5 / Fibre
>
> - 10/100/1000baseT
> - Token ring
>
> - Wireless (802.11)
>
> Security implications of shared media, switched media and VLANs.

### B3 Network Routing

- ACE: MC
- ICE: MC
- confidence: 3

> Network routing protocols RIP, OSPF, and IGRP/EIGRP.

### B4 Network Mapping & Target Identification

- ACE: MC, P
- ICE: MC, P
- confidence: 2
- todo: nmap flags cheatsheet

> Analysis of output from tools used to map the route between the engagement point and a number of targets.
>
> Network sweeping techniques to prioritise a target list and the potential for false negatives.

### B5 Interpreting Tool Output

- ACE: MC
- ICE: MC
- confidence: 3

> Interpreting output from port scanners, network sniffers and other network enumeration tools.

### B6 Filtering Avoidance Techniques

- ACE: MC
- ICE: MC
- confidence: 3

> The importance of egress and ingress filtering, including the risks associated with outbound connections.

### B7 Packet Crafting

- ACE: MC
- ICE: MC
- confidence: 3

> Packet crafting to meet a particular requirement:
>
> - Modifying source ports
>- Spoofing IP addresses
> - Manipulating TTL’s
>- Fragmentation
> - Generating ICMP packets

Nmap options (<https://nmap.org/book/man-bypass-firewalls-ids.html>):

| Function                                                     | Command line switches |
| ------------------------------------------------------------ | --------------------- |
| Fragment packets                                             | `-f`                  |
| Decoy scans (make it look like other hosts are also scanning) | `-D <host>,<host>`    |
| Spoof source address                                         | `-S <ipaddress>`      |
| Spoof source port                                            | `-g / --source-port`  |
| Set time-to-live value                                       | `--ttl <value>`       |
| Ping scan                                                    | `-sn`                 |
| TCP SYN scan                                                 | `-PS<ports>`          |
| TCP ACK scan                                                 | -`PA<ports>`          |
| UDP ping                                                     | `-PU<ports>`          |
| ARP Scan                                                     | `-PR`                 |
| Skip host discovery                                          | `-Pn`                 |



### B8 OS Fingerprinting

- ACE: MC
- ICE: MC, P
- confidence: 4

> Remote operating system fingerprinting; active and passive techniques.

nmap OS Detection from <https://nmap.org/book/man-os-detection.html>

```
nmap -O
```

### B9 Application Fingerprinting and Evaluating Unknown Services

- ACE: MC
- ICE: MC, P
- confidence: 2

> Determining server types and network application versions from application banners.
>
> Evaluation of responsive but unknown network applications.



### B10 Network Access Control Analysis

- ACE: MC
- ICE: MC
- confidence: 2

> Reviewing firewall rule bases and network access control lists.

### B11 Cryptography

- ACE: MC, P
- ICE: MC
- confidence: 3

> Differences between encryption and encoding.
>
> Symmetric / asymmetric encryption
>
> Encryption algorithms: DES, 3DES, AES, RSA, RC4.
>
> Hashes: SHA1 and MD5
>
> Message Integrity codes: HMAC

### B12 Applications of Cryptography

- ACE: MC
- ICE: MC
- confidence: 3

> SSL, IPsec, SSH, PGP
>
> Common wireless (802.11) encryption protocols: WEP, WPA, TKIP

### B13 File System Permissions

- ACE: MC
- ICE: MC
- confidence: 3

> File permission attributes within Unix and Windows file systems and their security implications.
>
> Analysing registry ACLs.

#### Linux / Unix Permissions

`[owner][group][other]`

| Number |              Octal Permission Representation              | Ref  |
| :----: | :-------------------------------------------------------: | :--: |
|   0    |                       No permission                       | ---  |
| **1**  |                    Execute permission                     | --x  |
| **2**  |                     Write permission                      | -w-  |
|   3    | Execute and write permission: 1 (execute) + 2 (write) = 3 | -wx  |
| **4**  |                      Read permission                      | r--  |
|   5    |  Read and execute permission: 4 (read) + 1 (execute) = 5  | r-x  |
|   6    |    Read and write permission: 4 (read) + 2 (write) = 6    | rw-  |
|   7    |  All permissions: 4 (read) + 2 (write) + 1 (execute) = 7  | rwx  |
|  2000  |                        setgid bit                         | s--- |
|  4000  |                        setuid bit                         | s--- |

#### Windows File Permissions

From <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727008(v=technet.10)?redirectedfrom=MSDN>

| Permission           | Meaning for Folders                                          | Meaning for Files                                            |
| :------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Read                 | Permits viewing and listing of files and subfolders          | Permits viewing or accessing of the file's contents          |
| Write                | Permits adding of files and subfolders                       | Permits writing to a file                                    |
| Read & Execute       | Permits viewing and listing of files and subfolders as well as executing of files; inherited by files and folders | Permits viewing and accessing of the file's contents as well as executing of the file |
| List Folder Contents | Permits viewing and listing of files and subfolders as well as executing of files; inherited by folders only | N/A                                                          |
| Modify               | Permits reading and writing of files and subfolders; allows deletion of the folder | Permits reading and writing of the file; allows deletion of the file |
| Full Control         | Permits reading, writing, changing, and deleting of files and subfolders | Permits reading, writing, changing and deleting of the file  |

| Control                      | Full Modify | Execute | Read & Read | Write | Special Permissions |
| :--------------------------- | :---------- | :------ | :---------- | :---- | :------------------ |
| Traverse Folder/Execute File | X           | X       | X           |       |                     |
| List Folder/Read Data        | X           | X       | X           | X     |                     |
| Read Attributes              | X           | X       | X           | X     |                     |
| Read Extended Attributes     | X           | X       | X           | X     |                     |
| Create Files/Write Data      | X           | X       |             |       | X                   |
| Create Folders/Append Data   | X           | X       |             |       | X                   |
| Write Attributes             | X           | X       |             |       | X                   |
| Write Extended Attributes    | X           | X       |             |       | X                   |
| Delete Subfolders and Files  | X           |         |             |       |                     |
| Delete                       | X           | X       |             |       |                     |
| Read Permissions             | X           | X       | X           | X     | X                   |
| Change Permissions           | X           |         |             |       |                     |
| Take Ownership               | X           |         |             |       |                     |

### B14 Audit Techniques

- ACE: MC
- ICE: MC, P
- confidence: 4

> Listing processes and their associated network sockets (if any).
>
> Assessing patch levels.
>
> Finding interesting files.

#### Listing Network Sockets

##### Linux

All listening TCP services (as root to see process name)

```
netstat -tlpn 
```

Useful switches:

| Switch      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `-t` / `-u` | TCP / UDP only                                               |
| `-n`        | Express everything as numerical rather than resolving hosts, guessing services |
| `-a`        | "All": Both listening and non-listening sockets              |
| `-l`        | Listening sockets only                                       |
| -p          | Show the program (only your own are named if you're not root) |

##### Windows

As with Linux, except:

| Linux       | Windows             |
| ----------- | ------------------- |
| `-t` / `-u` | `-p tcp` / `-p udp` |
| `-p`        | `-b`                |
| `-l`        | n/a                 |

#### Getting Patch Level

##### Linux

Kernel version, release, OS:

```
uname -a
```

Often sufficient to:

```
cat /etc/issue
```

Packages:

<https://www.unix.com/linux/111490-os-patch-level-command.html>:

- RPM based (SuSE, Fedora, RHEL, CentOS, ...): rpm -qa
-  DEB based (Debian, Ubuntu, ...): aptitude search ~i
-  Portage based (Gentoo, ...): equery list (provided by gentoolkit)
-  Slackware, LFS: your brain and/or any notes you kept :laughing:

##### Windows

OS version:

```
ver
```

All kinds of useful info

```
systeminfo
```

List updates / hotfixes

```
wmic qfe list
```

#### Interesting Files

##### Linux

setuid root files

```
find / -type f -perm -4000 -u root
```

Files with "secret" in the name (for example)

```
find / -type f -iname "*secret*"
```

Files that get created after you have just done something

```bash
touch /tmp/f
# Then do a thing
find / -newer /tmp/f
```

Find a file containing a specific phrase, even if it's a binary file

```
grep -air "password"
```

##### Windows

List drives

```
wmic logicaldisk get caption
```

Find all files with "secret" in the name on C:\

```
dir /a /s /b c:\*secret*
```

Find all files containing "password"

```
findstr /si password *
```

## Appendix C: Background Information Gathering & Open Source

### C1 Registration Records

- ACE: MC
- ICE: MC
- confidence: 5

> Information contained within IP and domain registries (WHOIS).

Compared with what this was when the syllabus was written, this is dead.

*However* you can determine ownership of IP blocks by organisation through WHOIS still. This provides an attack surface.

### C2 Domain Name Server (DNS)

- ACE: MC
- ICE: MC, P
- confidence: 3

> DNS queries and responses
>
> DNS zone transfers
>
> Structure, interpretation and analysis of DNS records:
>
> - SOA
>
> - MX
>
> - TXT
>
> - A
>
> - NS
>
> - PTR
>
> - HINFO
>
> - CNAME
>

### C3 Customer Web Site Analysis

- ACE: MC, P
- ICE: MC
- confidence: 5

> Analysis of information from a target web site, both from displayed content and from within the HTML source.
>

### C4 Google Hacking and Web Enumeration

- ACE: MC
- ICE: MC
- confidence: 5

> Effective use of search engines and other public data sources to gain information about a target.

Determine presence of backup files, login pages, backdoors previously installed etc.

### C5 NNTP Newsgroups and Mailing Lists

- ACE: MC
- ICE: MC
- confidence: 4

> Searching newsgroups or mailing lists for useful information about a target.

User agent, source IP

### C6 Information Leakage from Mail & News Headers

- ACE: MC
- ICE: MC
- confidence: 4

> Analysing news group and e-mail headers to identify internal system information.

Bounced email

- Leaked mail filter software
- Internal hostnames

## Appendix D: Networking Equipment

### D1 Management Protocols

- ACE: MC
- ICE: MC, P
- confidence: 3

> Weaknesses in the protocols commonly used for the remote management of devices:
>
> - Telnet
>
> - Web based protocols
>
> - SSH
>
> - SNMP (covering network information enumeration and common attacks against Cisco configurations)
>
> - TFTP
>
> - Cisco Reverse Telnet
>
> - NTP
>

### D2 Network Traffic Analysis

- ACE: MC
- ICE: MC
- confidence: 4

> Techniques for local network traffic analysis.
>
> Analysis of network traffic stored in PCAP files.

### D3 Networking Protocols

- ACE: MC
- ICE: MC, P
- confidence: 2

> Security issues relating to the networking protocols:
>
> - ARP
>
> - DHCP
>
> - CDP
>
> - HSRP
>
> - VRRP
>
> - VTP
>
> - STP
>
> - TACACS+
>

### D4 IPSec

- ACE: MC
- ICE: MC, P
- confidence: 3

> Enumeration and fingerprinting of devices running IPSec services.

- Integrated into IPv6
- Every packet is authenticated and encrypted
- OSI layer 3 (network)
- Internet Key Exchange (IKE) over UDP 500

### D5 VoIP

- ACE: MC
- ICE: MC, P
- confidence: 2
- todo: List common ports config, SIP methods

> Enumeration and fingerprinting of devices running VoIP services.
>
> Knowledge of the SIP protocol.
>

### D6 Wireless

- ACE: MC
- ICE: MC
- confidence: 3
- todo: re-read some of the attacks

> Enumeration and fingerprinting of devices running Wireless (802.11) services.
>
> Knowledge of various options for encryption and authentication, and the relative methods of each.
>
> - WEP
>- TKIP
> - WPA/WPA2
>- EAP/LEAP/PEAP
> 

 - WEP
   - Replay attacks
   - Forged ARP packets
   - Fragmentation attack
   - ChopChop attack
   - -> Crack key
 - WPA2 PSK
   - Deauth / handshake capture
   - Rogue AP / handshake capture
 - WPA2 Ent
   - hostapd-wpe rogue AP
   - EAP relay

### D7 Configuration Analysis

- ACE: MC
- ICE: MC, P
- confidence: 2

> Analysing configuration files from the following types of Cisco equipment:
>
> - Routers
>
> - Switches
>
>
> Interpreting the configuration of other manufacturers’ devices
>

## Appendix E: Microsoft Windows Security Assessment

### E1 Domain Reconnaissance

- ACE: MC
- ICE: MC, P
- confidence: 2

> Identifying domains/workgroups and domain membership within the target network.
>
> Identifying key servers within the target domains.
>
> Identifying and analysing internal browse lists.
>
> Identifying and analysing accessible SMB shares

### E2 User Enumeration

- ACE: MC
- ICE: MC, P
- confidence: 2

> Identifying user accounts on target systems and domains using NetBIOS, SNMP and LDAP.
>

### E3 Active Directory

- ACE: MC
- ICE: MC, P
- confidence: 2

> Active Directory Roles (Global Catalogue, Master Browser, FSMO)
>
> Reliance of AD on DNS and LDAP
>
> Group Policy (Local Security Policy)

### E4 Windows Passwords

- ACE: MC, P
- ICE: MC, P
- confidence: 3

> Password policies (complexity, lockout policies)
>
> Account Brute Forcing
>
> Hash Storage (merits of LANMAN, NTLMv1 / v2)
>
> Offline Password Analysis (rainbow tables / hash brute forcing)

### E5 Windows Vulnerabilities

- ACE: MC, P
- ICE: MC, P
- confidence: 3

> Knowledge of remote windows vulnerabilities, particularly those for which robust exploit code exists in the public domain.
>
> Knowledge of local windows privilege escalation vulnerabilities and techniques.
>
> Knowledge of common post exploitation activities:
>
> - obtain password hashes, both from the local SAM and cached credentials
> - obtaining locally-stored clear-text passwords
> - crack password hashes
>
> - check patch levels
>
> - derive list of missing security patches
>
> - reversion to previous state
>

### E6 Windows Patch Management Strategies

- ACE: MC
- ICE: MC, P
- confidence: 2

> Knowledge of common windows patch management strategies:
>
> - SMS
>
> - SUS
>
> - WSUS
>
> - MBSA
>

### E7 Desktop Lockdown

- ACE: MC
- ICE: MC, P
- confidence: 3

> Knowledge and understanding of techniques to break out of a locked down Windows desktop / Citrix environment.
>
> Privilege escalation techniques.

### E8 Exchange

- ACE: MC
- ICE: MC
- confidence: 3

> Knowledge of common attack vectors for Microsoft Exchange Server.
>

### E9 Common Windows Applications

- ACE: MC
- ICE: MC, P
- confidence: 2

> Knowledge of significant vulnerabilities in common windows applications for which there is public exploit code available.

## Appendix F: Unix Security Assessment

### F1 User enumeration

- ACE: MC
- ICE: MC, P
- confidence: 3
- todo: some bashfu for these archaic services

> Discovery of valid usernames from network services commonly running by default:
>
> - rusers
>
> - rwho
>
> - SMTP
>
> - finger
>
>
> Understand how finger daemon derives the information that it returns, and hence how it can be abused.

### F2 Unix vulnerabilities

- ACE: MC
- ICE: MC, P
- confidence: 3
- todo: Fricken solaris vulns, seriously

> Recent or commonly-found Solaris vulnerabilities, and in particular those for which there is exploit code in the public domain.
>
> Recent or commonly-found Linux vulnerabilities, and in particular those for which there is exploit code in the public domain.
>
> Use of remote exploit code and local exploit code to gain root access to target host 
>
> Common post-exploitation activities:
>
> - exfiltrate password hashes
>
> - crack password hashes
>
> - check patch levels
>
> - derive list of missing security patches
>
> - reversion to previous state
>

### F3 FTP

- ACE: MC
- ICE: MC, P
- confidence: 3

> FTP access control
>
> Anonymous access to FTP servers
>
> Risks of allowing write access to anonymous users.

### F4 Sendmail / SMTP

- ACE: MC
- ICE: MC, P
- confidence: 4

> Valid username discovery via EXPN and VRFY
>
> Awareness of recent Sendmail vulnerabilities; ability to exploit them if possible
>
> Mail relaying

### F5 Network File System (NFS)

- ACE: MC
- ICE: MC, P
- confidence: 3

> NFS security: host level (exports restricted to particular hosts) and file level (by UID and GID).
>
> Root squashing, nosuid and noexec options.
>
> File access through UID and GID manipulation.

### F6 R* services

- ACE: MC
- ICE: MC, P
- confidence: 2

> Berkeley r* service:
>
> - access control (/etc/hosts.equiv and .rhosts)
>
> - trust relationships
>
>
> Impact of poorly-configured trust relationships.

### F7 X11

- ACE: MC
- ICE: MC, P
- confidence: 2

> X Windows security and configuration; hostbased vs. user-based access control.
>

### F8 RPC services

- ACE: MC
- ICE: MC, P
- confidence: 2

> RPC service enumeration
>
> Common RPC services
>
> Recent or commonly-found RPC service vulnerabilities.

### F9 SSH

- ACE: MC
- ICE: MC, P
- confidence: 4

> Identify the types and versions of SSH software in use
>
> Securing SSH
>
> Versions 1 and 2 of the SSH protocol
>
> Authentication mechanisms within SSH

## Appendix G: Web Technologies

### G1 Web Server Operation

- ACE: MC
- ICE: MC
- confidence: 5

> How a web server functions in terms of the client/server architecture.
>
> Concepts of virtual hosting and web proxies.

### G2 Web Servers & their Flaws

- ACE: MC, P
- ICE: MC, P
- confidence: 4
- todo: Probably some ancient CVEs for Apache and IIS that nobody ever sees any more

> Common web servers and their fundamental differences and vulnerabilities associated with them:
>
> - IIS
>
> - Apache (and variants)
>

### G3 Web Enterprise Architectures

- ACE: MC
- ICE: MC
- confidence: 5

> Design of tiered architectures.
>
> The concepts of logical and physical separation.
>
> Differences between presentation, application and database layers.

### G4 Web Protocols

- ACE: MC, P
- ICE: MC, P
- confidence: 4

> Web protocols: HTTP, HTTPS, SOAP.
>
> All HTTP web methods and response codes.
>
> HTTP Header Fields relating to security features

### G5 Web Mark-up Languages

- ACE: MC
- ICE: MC
- confidence: 5

> Web mark-up languages: HTML and XML.

### G6 Web Programming Languages

- ACE: MC
- ICE: MC
- confidence: 5

> Common web programming languages: JSP, ASP, PHP, CGI based Perl and JavaScript.
>

### G7 Web Application Servers

- ACE: MC, P
- ICE: MC
- confidence: 3
- todo: Some ancient CVEs for .NET, J2EE, Coldfusion, Ruby on Rails and AJAX.

> Vulnerabilities in common application frameworks, servers and technologies: .NET, J2EE, Coldfusion, Ruby on Rails and AJAX.
>

### G8 Web APIs

- ACE: MC, P
- ICE: MC
- confidence: 3

> Application interfaces: CGI, ISAPI filters and Apache modules.
>

### G9 Web SubComponents

- ACE: MC, P
- ICE: MC
- confidence: 3

> Web architecture sub-components:
>
> - Thin/Thick web clients, servlets and applets, Active X.
> - Flash Application Testing
> - .Net Thick Clients
> - Java Applets
> - Decompilation of client-side code

## Appendix H: Web Testing Methodologies

### H1 Web Application Reconnaissance

- ACE: MC
- ICE: MC
- confidence: 5

> Benefits of performing application reconnaissance.
>
> Discovering the structure of web applications.
>
> Methods to identify the use of application components defined in G1 to G9.

### H2 Threat Modelling and Attack Vectors

- ACE: MC
- ICE: MC
- confidence: 2
- todo: basic threat modelling techniques

> Simple threat modelling based on customer perception of risk.
>
> Relate functionality offered by the application to potential attack vectors.

### H3 Information Gathering from Web Mark-up

- ACE: MC, P
- ICE: MC
- confidence: 5

> Examples of the type of information available in web page source that may prove useful to an attacker:
>
> - Hidden Form Fields
>
> - Database Connection Strings
>
> - Credentials
>
> - Developer Comments
>
> - Other included files
>
> - Authenticated-only URLs
>

### H4 Authentication Mechanisms

- ACE: MC, P
- ICE: MC
- confidence: 4

> Common pitfalls associated with the design and implementation of application authentication mechanisms.

### H5 Authorisation Mechanisms

- ACE: MC, P
- ICE: MC
- confidence: 4

> Common pitfalls associated with the design and implementation of application authorisation mechanisms.
>

### H6 Input Validation

- ACE: MC, P
- ICE: MC
- confidence: 5

> The importance of input validation as part of a defensive coding strategy.
>
> How input validation can be implemented and the differences between white listing, black listing and data sanitisation.

### H7 Application Fuzzing

- ACE: MC, P
- ICE: MC
- confidence: 5

> Fuzzing and its relevance within web-app penetration testing.
>
> The use of fuzz strings and their potential effects.
>
> Potential dangers of fuzzing web applications.

### H8 Information Disclosure in Error Messages

- ACE: MC
- ICE: MC
- confidence: 5

> How error messages may indicate or disclose useful information.
>

### H9 Use of Cross Site Scripting Attacks

- ACE: MC, P
- ICE: MC
- confidence: 5

> Potential implications of a cross site scripting vulnerability.
>
> Ways in which the technique can be used to benefit an attacker.

### H10 Use of Injection Attacks

- ACE: MC, P
- ICE: MC
- confidence: 4

> Potential implications of injection vulnerabilities:
>
> - SQL injection
> - LDAP injection
> - Code injection
> - XML injection
>
> Ways in which these techniques can be used to benefit an attacker.

### H11 Session Handling

- ACE: MC, P
- ICE: MC
- confidence: 5

> Common pitfalls associated with the design and implementation of session handling mechanisms.

### H12 Encryption

- ACE: MC, P
- ICE: MC
- confidence: 3
- todo: Re-learn all the TLS vulns that I've now forgotten about because they're boring

> Common techniques used for encrypting data in transit and data at rest, either on the client or server side.
>
> Identification and exploitation of Encoded values (e.g. Base64) and Identification and exploitation of Cryptographic values (e.g. MD5 hashes)
>
> Identification of common SSL vulnerabilities

### H13 Source Code Review

- ACE: MC, P
- ICE: MC
- confidence: 4

> Common techniques for identifying and reviewing deficiencies in the areas of security.

## Appendix I: Web Testing Techniques

### I1 Web Site Structure Discovery

- ACE: P
- ICE: MC
- confidence: 4
- todo: Wiki lab

> Spidering tools and their relevance in a web application test for discovering linked content.
>
> Forced browsing techniques to discover default or unlinked content.
>
> Identification of functionality within client-side code

### I2 Cross Site Scripting Attacks

- ACE: P
- ICE: MC
- confidence: 5

> Arbitrary JavaScript execution.
>
> Using Cross Site Scripting techniques to obtain sensitive information from other users.
>
> Phishing techniques.

### I3 SQL Injection

- ACE: P
- ICE: MC
- confidence: 4
- todo: MS SQL Server SQLi cheat sheet, tamper scripts

> Determine the existence of an SQL injection condition in a web application.
>
> Determine the existence of a blind SQL injection condition in a web application.
>
> Exploit SQL injection to enumerate the database and its structure.
>
> Exploit SQL injection to execute commands on the target server.

### I4 Session ID Attacks

- ACE: P
- ICE: MC
- confidence: 4

> Investigate session handling within a web application.
>
> Harvest and analyse a number of session identifiers for weaknesses.

### I5 Fuzzing

- ACE: P
- ICE: MC
- confidence: 5

> The concept of fuzzing within a web application testing methodology.
>
> Common fuzzing tools.

### I6 Parameter Manipulation

- ACE: P
- ICE: MC
- confidence: 5

> Parameter manipulation techniques, particularly the use of client side proxies.

### I7 Data Confidentiality & Integrity

- ACE: P
- ICE: MC
- confidence: 3
- todo: TLS vulns cheat sheet

> Identifying weak (or missing) encryption.
>
> Identifying insecure SSL configurations.
>
> Identify insecure use of encoding techniques

### I8 Directory Traversal

- ACE: P
- ICE: MC
- confidence: 4

> Identifying directory traversal vulnerabilities within applications.

### I9 File Uploads

- ACE: P
- ICE: MC
- confidence: 5

> Identifying common vulnerabilities with file upload capabilities within applications.

### I10 Code Injection

- ACE: P
- ICE: MC
- confidence: 5

> Investigate and exploitation of code injection vulnerabilities within web applications

### I11 CRLF Attacks

- ACE: P
- ICE: MC
- confidence: 4

> Assessment of web applications for CRLF vulnerabilities

### I12 Application Logic Flaws

- ACE: P
- ICE: MC
- confidence: 5

> Assessing the logic flow within an application and the potential for subverting the logic.

## Appendix J: Databases

### J1 Microsoft SQL Server

- ACE: MC, P
- ICE: MC, P
- confidence: 4

> Knowledge of common attack vectors for Microsoft SQL Server. Understanding of privilege escalation and attack techniques for a system compromised via database connections.

### J2 Oracle RDBMS

- ACE: MC, P
- ICE: MC, P
- confidence: 3
- todo: Oracle default creds cheat sheet, SQLi cheat sheet

> Derivation of version and patch information from hosts running Oracle software.
>
> Default Oracle accounts.

### J3 Web / App / Database Connectivity

- ACE: MC, P
- ICE: MC, P
- confidence: 4

> Common databases (MS SQL server, Oracle, MySQL and Access) and the connection and authentication methods used by web applications.
>

