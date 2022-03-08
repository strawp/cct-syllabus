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
- confidence: 4

> Analysis of output from tools used to map the route between the engagement point and a number of targets.
>
> Network sweeping techniques to prioritise a target list and the potential for false negatives.

#### Network Routes

`traceroute` / `tracert`: Adjust TTL value of IP header to elicit an ICMP `TIME_EXCEEDED` response from each gateway along the route to the host.

Can be blocked by firewalls not allowing ICMP, unlikely UDP ports. Anti filtering connection methods (`-M`):

| Name    | Flag       | Description                                                  |
| ------- | ---------- | ------------------------------------------------------------ |
| default |            | UDP datagrams using unlikely ports, host determined by ICMP "unreach port" |
| icmp    | `-I`       | ICMP echo packets, only works if you can ping host           |
| tcp     | `-T`       | TCP `SYN` probes, reliable way of bypassing firewall if you can view an open port on the other side of it. (e.g. `-T -p 80`) |
| tcpconn |            | Full TCP connection, not recommended                         |
| udp     | `-U`       | UDP datagram to known open port. Application always sees this (as no handshake with UDP). You never get to see the final hop. |
| udplite | `-UL`      | As above but for UDP-Lite datagrams                          |
| dccp    | -D         | Creates "half open" connections as with TCP                  |
| raw     | `-P proto` | Creates a raw IP packet with the correct protocol number but no protocol-specific headers |

#### Host Discovery

| Name             | Flag                | Description                                                  |
| ---------------- | ------------------- | ------------------------------------------------------------ |
| List scan        | `-sL`               | Just output list of hosts without touching the network (for sanity check). Can be used with `-R` to reverse DNS lookup en masse |
| No port scan     | `-sn`               | Don't scan ports, just discover hosts. Uses ICMP echo, TCP SYN on 443, TCP ACK on 80, ICMP timestamp. Privileged users on a local network will use ARP requests. |
| No ping          | `-Pn`               | Skip host discovery entirely. Privileged users on local network will still get an ARP scan though. |
| TCP SYN ping     | `-PS <ports>`       | Define ports to attempt TCP SYN to. If either RST or SYN/ACK is returned, you know there's a host there. |
| TCP ACK ping     | `-PA <ports>`       | As above but with TCP ACK, which a live host should always respond with RST. Good if firewalls are blocking SYN |
| UDP ping         | `-PU <ports>`       | Target a specifically **closed** port in order to get back an ICMP port unreachable packet |
| SCTP ping        | `-PY <ports>`       | List TCP but `INIT` instead of `SYN`, `ABORT` instead of `RST` and `INIT-ACK` instead of `SYN/ACK`. No idea when this would be any use. Telecoms infra probably. |
| ICMP pings       | `-PE`, `-PP`, `-PM` | Echo, timestamp and address mask queries. Don't use them though as they probably won't work. |
| IP Protocol ping | `-PO <proto>`       | Use a specific IP protocol, look for a response on the same protocol or an ICMP response |

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
- confidence: 4

> Determining server types and network application versions from application banners.
>
> Evaluation of responsive but unknown network applications.

#### TCP Top 40

Greetings pop pickers, it's time for the TCP/IP nmap top 40 (ish)...

| port | name | info |
| ---- | ---- | ---- |
| 80 | http | |
| 23 | telnet | |
| 443 | https | |
| 21 | ftp | |
| 22 | ssh | |
| 25 | smtp | |
| 3389 | ms-wbt-server | Remote desktop |
| 110 | pop3 | |
| 445 | microsoft-ds | |
| 139 | netbios-ssn | |
| 143 | imap | |
| 53 | domain | |
| 135 | msrpc | |
| 3306 | mysql | |
| 8080 | http-proxy | |
| 1723 | pptp | Point-to-Point Tunneling Protocol |
| 111 | rpcbind | |
| 995 | pop3s | POP over TLS |
| 993 | imaps | TLS version of IMAP |
| 5900 | vnc | |
| 1025 | NFS-or-IIS | |
| 587 | submission | SMTP with StartTLS, generally |
| 8888 | sun-answerbook | |
| 199 | smux | |
| 1720 | h323q931 | |
| 465 | smtps | SMTP implicitly using TLS |
| 548 | afp | |
| 113 | ident | |
| 81 | hosts2-ns | HTTP, more likely |
| 6001 | X11:1 | |
| 10000 | snet-sensor-mgmt | |
| 514 | shell | |
| 5060 | sip | |
| 179 | bgp | |
| 1026 | LSA-or-nterm | |
| 2000 | cisco-sccp | |
| 8443 | https-alt | |
| 8000 | http-alt | |
| 32768 | filenet-tms | |
| 554 | rtsp | |
| 1433 | ms-sql-s | MS SQL Server |
| 2049 | nfs |  |
| 6000 | X11 |  |
| 389 | ldap | Surprised this is so low on nmap's list TBH |

#### UDP Top 40

And for UDP...

| port | name | info |
| ---- | ---- | ---- |
| 631 | ipp | Internet Printing Protocol |
| 161 | snmp | |
| 137 | netbios-ns | |
| 123 | ntp | Network Time Protocol |
| 138 | netbios-dgm | |
| 1434 | ms-sql-m | |
| 445 | microsoft-ds | |
| 135 | msrpc | |
| 67 | dhcps | |
| 53 | domain | |
| 139 | netbios-ssn | |
| 500 | isakmp | |
| 68 | dhcpc | |
| 520 | route | |
| 1900 | upnp | |
| 4500 | nat-t-ike | |
| 514 | syslog | |
| 162 | snmptrap | |
| 69 | tftp | |
| 5353 | zeroconf | |
| 111 | rpcbind | |
| 1701 | L2TP | |
| 998 | puparp | |
| 996 | vsinet | |
| 997 | maitrd | |
| 999 | applix | |
| 3283 | netassistant | |
| 1812 | radius | |
| 136 | profile | |
| 2222 | msantipiracy | |
| 2049 | nfs | |
| 32768 | omad | |
| 5060 | sip | |
| 1025 | blackjack | |
| 1433 | ms-sql-s | |
| 3456 | IISrpc-or-vat | |
| 80 | http | |

#### Golden Oldies

And here are a whole bunch of services that won't be referenced anywhere outside of this exam. Ask your grandad:

| port | name | info |
| ---- | ---- | ---- |
| 1/tcp | tcpmux | Allows anyone to connect to the host and query which services it is running. Hard to firewall, deprecated in 2016 |
| 5/tcp | rje | Remote Job Entry |
| 7/tcp | echo | Literally sends back any data it receives |
| 11/tcp | systat | |
| 13/tcp | daytime | Returns ASCII string of current datetime |
| 15/tcp | netstat | |
| 17/tcp | qotd | Broadcasts a message set by the sysadmin. UDP implementation can be abused for DoS |
| 18/tcp | msp | Message Send Protocol |
| 19/tcp | chargen | Spew random chars. UDP version can be abused for DoS |
| 20/tcp | ftp-data | |
| 24/tcp | priv-mail | |
| 26/tcp | rsftp | |
| 37/tcp | time | Send the time back as a signed int |
| 38/tcp | rap | Route Access Protocol |
| 41/tcp | graphics | |
| 42/tcp | nameserver | |
| 43/tcp | whois | |
| 47/tcp | ni-ftp | |
| 48/tcp | auditd | |
| 49/tcp | tacacs | Terminal Access Control Access Control Server |
| 53/tcp | domain | |
| 63/tcp | via-ftp | |
| 65/tcp | tacacs-ds | |
| 66/tcp | sqlnet | |
| 67/tcp | dhcps | |
| 68/tcp | dhcpc | |
| 69/tcp | tftp | |
| 70/tcp | gopher | |
| 79/tcp | finger | |

`netcat / ncat / nc <server> <port>`

`ncat -C --ssl <server> <port>`

`openssl s_client -connect <server>:<port>`

### B10 Network Access Control Analysis

- ACE: MC
- ICE: MC
- confidence: 3

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
- confidence: 3

> Security issues relating to the networking protocols:
>
> - ARP
> - DHCP
> - CDP
> - HSRP
> - VRRP
> - VTP
> - STP
> - TACACS+
> 

| Protocol | Consideration                                                |
| -------- | ------------------------------------------------------------ |
| ARP      | ARP spoofing, ARP cache for host discovery                   |
| DHCP     | Not a security boundary                                      |
| CDP      | Leaks info about network gatways before auth                 |
| HSRP     | Hot Standby Routing Protocol. Not a routing protocol :joy:   |
| VRRP     | Virtual Router Redundancy Protocol. Spoof packets, affect availability |
| VTP      | VLAN Trunking Protocol. Spoof VLAN tags in packets, hop VLANs |
| STP      | Spanning Tree Protocol. Network routing, screw with it to make impossible routes. |
| TACACS+  | Terminal Access Control Access Control Server. Surely not going to be quizzed on this in MC... |

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
- confidence: 4

> Enumeration and fingerprinting of devices running VoIP services.
>
> Knowledge of the SIP protocol.

- nmap will identify SIP just fine
- Ports 5060 TCP and UDP, 5061 TLS (typically)

#### Exploitation:

1. Identify service exists (nmap, sippts, sipvicious - **NB** sipvicious only works over UDP)
2. Scan for extension numbers using tool of choice, identifying which require auth
3. Attempt `REGISTER` or `INVITE` to test auth
4. Also possible to crack auth passwords, out of scope for these notes though!

#### Methods

- **`INVITE`**: Establishes a session with another user
- **`ACK`**: Confirms an INVITE request
- **`BYE`** : Ends a session
- **`CANCEL`**: Cancels establishing of a session
- **`REGISTER`**: Communicates user location (host name, IP)
- **`OPTIONS`**: Communicates information about the capabilities of the calling and receiving SIP phones
- **`PRACK`**: Provisional Acknowledgement
- **`SUBSCRIBE`**: Subscribes for Notification from the notifier
- **`NOTIFY`**: Notifies the subscriber of a new event
- **`PUBLISH`**: Publishes an event to the Server
- **`INFO`**: Sends mid session information
- **`REFER`**: Asks the recipient to issue call transfer
- **`MESSAGE`**: Transports Instant Messages
- **`UPDATE`**: Modifies the state of a session

#### Response Codes

Pretty much the same as HTTP:

- **`1XX`**: Informational responses, such as 180 (ringing)
- **`2XX`**: Success responses
- **`3XX`**: Redirection responses
- **`4XX`**: Request failures
- **`5XX`**: Server errors
- **`6XX`**: Global failures

#### Typical Session Initiation

| Client                | Server        |
| --------------------- | ------------- |
| `REGISTER`            | --->          |
| <---                  | `200 OK`      |
| `INVITE`              | --->          |
| <---                  | `100 TRYING`  |
| <---                  | `180 RINGING` |
| <---                  | `200 OK`      |
| `ACK`                 | --->          |
| <--- `RTP/RTCP comms` | --->          |
| `BYE`                 | --->          |
| <---                  | `200 OK`      |

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
- confidence: 3

> Identifying domains/workgroups and domain membership within the target network.
>
> Identifying key servers within the target domains.
>
> Identifying and analysing internal browse lists.
>
> Identifying and analysing accessible SMB shares

| Command                                  | Description                        |
| ---------------------------------------- | ---------------------------------- |
| `net view /domain`                       | View hosts in current domain       |
| `net user /domain`                       | View users in domain               |
| `net localgroup "Administrators"`        | List local admins                  |
| `net group "Domain Admins" /domain`      | List members of domain admin group |
| `net group "Domain Controllers" /domain` | List domain controllers            |

### E2 User Enumeration

- ACE: MC
- ICE: MC, P
- confidence: 3

> Identifying user accounts on target systems and domains using NetBIOS, SNMP and LDAP.

Likelihood of detailed answer for MC = meh

### E3 Active Directory

- ACE: MC
- ICE: MC, P
- confidence: 3

> Active Directory Roles (Global Catalogue, Master Browser, FSMO)
>
> Reliance of AD on DNS and LDAP
>
> Group Policy (Local Security Policy)

Meh, pretty sure I don't need to dive into this for MC

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
- confidence: 3

> Knowledge of common windows patch management strategies:
>
> - SMS
>- SUS
> - WSUS
>- MBSA
> 

#### SMS

- "Systems Management Server"

#### SUS

	- "Software Update Services"
	- Version of Windows Update that is run on the local network

#### WSUS

- "Windows Server Update Services"
- Connects to MS Update
- Numerous other WSUS servers in the network can connect to the upstream WSUS server

#### MBSA

- "MS Baseline Security Analyser"
- Run security audits against:
  - Client versions of Windows, including Windows 7
  - Windows Server, including Windows Server 2008
  - SQL Server
  - Internet Information Server (IIS)
  - Internet Explorer
  - Microsoft Office

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

- [x] Knowledge that metasploit exists
- [x] Knowledge that the MC app exam probably isn't going to even test knowledge of common LOLBINS

## Appendix F: Unix Security Assessment

### F1 User enumeration

- ACE: MC
- ICE: MC, P
- confidence: 3

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
>Understand how finger daemon derives the information that it returns, and hence how it can be abused.

- r* commands: `rusers <host>`
- SMTP: `EXPN` and `VRFY` commands
- finger: TCP/79 , shows you where someone was last seen

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
- confidence: 3

> Berkeley r* service:
>
> - access control (/etc/hosts.equiv and .rhosts)
>
> - trust relationships
>
>Impact of poorly-configured trust relationships.

<https://en.wikipedia.org/wiki/Berkeley_r-commands>

- rcp, rexec, rlogin, rsh, rstat, ruptime, rwho
- No encryption
- Trust relationship based on client's hostname and username, written in `/etc/hosts.equiv` and `.rhosts`
- You can just lie to the server

### F7 X11

- ACE: MC
- ICE: MC, P
- confidence: 3

> X Windows security and configuration; hostbased vs. user-based access control.

#### Host-based

- Specify list of hosts which are allowed to connect

#### User-based

- Actual user proof required, e.g. Kerberos

#### Cookie-based

- Exchange some data which actually authenticates that you should have access

### F8 RPC services

- ACE: MC
- ICE: MC, P
- confidence: 3

> RPC service enumeration
>
> Common RPC services
>
> Recent or commonly-found RPC service vulnerabilities.

- Binaries bound to a register of RPC services
- `rpcinfo <host>` to query RPC services on a host
- Vulns depend on the service
- No inherent auth

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

> Common web servers and their fundamental differences and vulnerabilities associated with them:
>
> - IIS
>- Apache (and variants)
> 

*I've seen things you people wouldn't believe... Unauthenticated unsafe file upload off the web root of a security appliance... I watched C-code compile cleanly through a remote shell on a network gateway... All those moments will be lost in time, like tears in the rain...*

#### IIS

- MS00-057: Path traversal through unicode chars leading to arbitrary file read and RCE in IIS 4.0
- [CVE-2003-0224](https://www.cvedetails.com/cve/CVE-2003-0224/): Server Side Include RCE in IIS 5.0
- [CVE-2010-2730](https://www.cvedetails.com/cve/CVE-2010-2730/): Buffer overflow to RCE in IIS 7.5

#### Apache projects

- [ CVE-2012-0838](https://www.cvedetails.com/cve/CVE-2012-0838/): Apache Struts RCE through OGNL expression
- [CVE-2013-4316](https://www.cvedetails.com/cve/CVE-2013-4316/): Apache Struts dynamic method invocation
- [ CVE-2016-3082](https://www.cvedetails.com/cve/CVE-2016-3082/): Apache Struts stylesheet location parameter RCE
- [CVE-2017-5638](https://www.cvedetails.com/cve/CVE-2017-5638/): Apache Struts Jakarta Multipart Parser RCE

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
- confidence: 4

> Simple threat modelling based on customer perception of risk.
>
> Relate functionality offered by the application to potential attack vectors.

<https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html>

#### Terms

- Threat agent
- Impact
- Likelihood
- Controls
- Preventions
- Mitigations
- Data flow
- Trust boundary

#### DREAD

- **D**amage - how bad would an attack be?
- **R**eproducibility - how easy it is to reproduce the attack?
- **E**xploitability - how much work is it to launch the attack?
- **A**ffected users - how many people will be impacted?
- **D**iscoverability - how easy it is to discover the threat?

Risk Value = (Damage + Affected users) x (Reproducibility + Exploitability + Discoverability).

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
> 


#### SSLv3 Padding Oracle On Downgraded Legacy Encryption Vulnerability (POODLE) 

MitM attackers can decrypt a selected byte of a cipher text in as few as 256 tries if they are able to force a victim application to repeatedly send the same data over newly created SSL 3.0 connections. 


#### TLS Padding Oracle Information Disclosure Vulnerability (TLS POODLE) 

Encrypted TLS traffic can be decrypted. This vulnerability could allow for the decryption of HTTPS traffic by an unauthorized third party. 


#### Weak SSL Cipher Lengths                                      

Messages encrypted with LOW and MEDIUM key lengths&nbsp;(\<128bits) are easy to decrypt in today's climate. NULL ciphers offer no encryption at all and ANONYMOUS ciphers provide no authentication meaning that data can become exposed via a man-in-the-middle attack. 


#### OpenSSL SSL_OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG Session Resume Ciphersuite Downgrade 

The version of OpenSSL on the remote host has been shown to allow resuming session with a weaker cipher than was used when the session was initiated. This means that an appropriately positioned threat actor could manipulate the OpenSSL session cache to cause subsequent resumptions of that session to use a weaker cipher chosen by the attacker. 


#### SSL/TLS EXPORT_RSA \<= 512-bit Cipher Suites Supported (FREAK) 

If a server is willing to negotiate an export ciphersuite, a man-in-the-middle may trick a browser to use a weak export key. By design, export RSA moduli must be less than 512 bits long; hence, they can be factored in less than 12 hours on modern computing hardware 


#### SSL RC4 Cipher Suites Supported (Bar Mitzvah)                

If plaintext is repeatedly encrypted (e.g. HTTP cookies) and an attacker is able to obtain many (i.e. tens of millions) ciphertexts, the attacker may be able to derive the plaintext. 


#### SWEET32 - SSL 64-bit Block Size Cipher Suites Supported      

An appropriately placed network attacker who is able to monitor a long-lived Triple-DES HTTPS connection between a web browser and a website can recover and decrypt data associated with that connection. 


#### SSL/TLS Diffie-Hellman Modulus \<= 1024 Bits (Logjam)        

Diffie-Hellman moduli of \<= 512 bits can easily be cracked by individual attackers, whereas moduli of \<= 1024 would require so-called "nation state" capabilities in order to successfully exploit this vulnerability. 


#### TLS v1.0                                    




#### TLS v1.1 Protocol in Use                                     

TLSv1.1 has been proposed for deprecation by the IETF, with Firefox and Google Chrome having either already removed support for or proposed an intention for removing support for it. Whilst TLSv1.1 does not have any major vulnerability affecting it, it is still recommended that is not used as it lacks support for current and recommended cipher suites. Ciphers that support encryption before MAC computation and authenticated encryption modes such as GCM cannot be used with TLS 1.1. 


#### SSL/TLS Protocol Initialization Vector Implementation Information Disclosure Vulnerability (BEAST) 

A vulnerability exists in SSL 3.0 and TLS 1.0 that could allow information disclosure if an attacker intercepts encrypted traffic served from an affected system. TLS 1.1, TLS 1.2, and all cipher suites that do not use CBC mode are not affected. 


#### Lucky Thirteen                                               

The usage of cipher block chaining (CBC) ciphers with TLS is potentially susceptible to attackers being able to recover the plaintext of encrypted data. The attacks can only be carried out by a determined attacker who is located close to the machine being attacked and who can generate sufficient sessions for the attacks. 


#### Client-Initiated Renegotiation                               

When a new TLS connection is being negotiated, the server will typically spend significantly more CPU resources than the client. Thus, if many new TLS connections are requested per second, denial-of-service attacks (DoS) are possible. If the TLS server supports client-initiated renegotiation, an attacker can force a server to perform many expensive cryptographic operations over a single TCP connection &ndash; making this attack significantly more viable. 


#### HTTP compression (BREACH)                                    

BREACH is an attack against HTTP compression, which can be used to recover parts of the plain-text in a HTTP response. HTTP compression is much more common than TLS-level compression. The attack is agnostic to the version of TLS and works against any cipher suite. 


#### Fallback Signaling Cipher Suite Value (SCSV) Not Supported   

The TLS Fallback Signaling Cipher Suite Value (SCSV) is used to prevent protocol downgrade attacks. It allows the client to indicate to the server when the current connection attempt is a fallback attempt. When present in the TLS client hello message, the server knows that the connecting client can use a better protocol than it is currently connecting with, and can choose to reject the connection. TLS Fallback SCSV gained popularity after the POODLE attack was discovered, since it prevented clients that supported TLS from being forced back to SSLv3 (to be attacked). Nowadays, it is still a good defense-in-depth feature to support, as it will, for example, prevent a client being forced back from TLSv1.2 to TLSv1.1. When not supported, a man-in-the-middle attacker might be able to dictate the protocol version used to communicate. 


#### Return Of Bleichenbacher's Oracle Threat (ROBOT)             

ROBOT is the return of a 19-year-old vulnerability that allows performing RSA decryption and signing operations with the private key of a TLS server. After Bleichenbacher's original attack TLS decided kept the vulnerable encryption modes and added countermeasures. Research since has showed that these countermeasures were incomplete leading to more complicated countermeasures. The affected host - despite being patched and theoretically not vulnerable to known versions of the ROBOT attack - still supports cipher-suites relying on RSA-based encryption schemes. RSA encryption modes currently present a risk since further variations of this attack may reveal new oracles. In addition, these modes also lack forward secrecy. 


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
- confidence: 4

> Derivation of version and patch information from hosts running Oracle software.
>
> Default Oracle accounts.

- Typical listener on 1521/TCP
- I was going to do an exhaustive list of default Oracle accounts but it was exhaust*ing* instead
- Get version with `SELECT * FROM v$version;`

#### The classic default accounts

| Username | Known valid passwords |
| ---------- | ----------- |
| SYSTEM | CHANGE_ON_INSTALL, D_SYSPW, MANAGER, ORACLE, SYSTEMPASS, SYSTEM, MANAG3R, ORACL3, 0RACLE, 0RACL3, ORACLE8, ORACLE9, ORACLE9I, 0RACLE9I, 0RACL39I, D_SYSTPW, ORACLE8I, 0RACLE8, 0RACLE9, 0RACLE8I, 0RACL38, 0RACL39, 0RACL38I |
| SYS | 0RACLE8, 0RACLE9, 0RACLE8I, 0RACL38, 0RACL39, 0RACL38I, CHANGE_ON_INSTALL, D_SYSPW, MANAGER, ORACLE, SYS, SYSPASS, MANAG3R, ORACL3, 0RACLE, 0RACL3, ORACLE8, ORACLE9, ORACLE8I, ORACLE9I, 0RACLE9I, 0RACL39I |
| HR | <UNKNOWN>, CHANGE_ON_INSTALL, HR, UNKNOWN |
| CTXSYS | <UNKNOWN>, CHANGE_ON_INSTALL, CTXSYS, UNKNOWN |
| WKPROXY | WKPROXY, CHANGE_ON_INSTALL, UNKNOWN |
| VRR1 | VRR1, VRR2, UNKNOWN |
| SH | CHANGE_ON_INSTALL, SH, UNKNOWN |
| QS_WS | CHANGE_ON_INSTALL, QS_WS, UNKNOWN |
| QS_OS | CHANGE_ON_INSTALL, QS_OS, UNKNOWN |
| QS_ES | CHANGE_ON_INSTALL, QS_ES, UNKNOWN |
| QS_CS | CHANGE_ON_INSTALL, QS_CS, UNKNOWN |
| QS_CBADM | CHANGE_ON_INSTALL, QS_CBADM, UNKNOWN |
| QS_CB | CHANGE_ON_INSTALL, QS_CB, UNKNOWN |
| QS_ADM | CHANGE_ON_INSTALL, QS_ADM, UNKNOWN |
| QS | CHANGE_ON_INSTALL, QS, UNKNOWN |
| PM | CHANGE_ON_INSTALL, UNKNOWN, PM |
| OE | CHANGE_ON_INSTALL, UNKNOWN, OE |
| MMO2 | MMO2, MMO3, UNKNOWN |
| CDEMO82 | CDEMO82, CDEMO83, UNKNOWN |
| APPLYSYSPUB | FNDPUB, PUB, <UNKNOWN> |
| APPLSYSPUB | APPLSYSPUB, PUB, FNDPUB |
| APPLSYS | APPLSYS, APPS, FND |
| WKSYS | CHANGE_ON_INSTALL, WKSYS |
| TEST | PASSWD, TEST |
| SYSMAN | SYSMAN, OEM_TEMP |
| SYSADMIN | <UNKNOWN>, SYSADMIN |
| SCOTT | TIGER, TIGGER |
| SAP | SAPR3, 06071992 |
| REP_OWNER | DEMO, REP_OWNER |
| PORTAL_DEMO | <UNKNOWN>, PORTAL_DEMO |
| PORTAL30 | PORTAL30, PORTAL31 |
| OWF_MGR | <UNKNOWN>, OWF_MGR |
| OSE$HTTP$ADMIN | Invalid, password, INVALID |
| ORACACHE | <UNKNOWN>, ORACACHE |
| OLAPSYS | MANAGER, OLAPSYS |
| OLAPSVR | INSTANCE, OLAPSVR |
| OCM_DB_ADMIN | <UNKNOWN>, OCM_DB_ADMIN |
| OAS_PUBLIC | OAS_PUBLIC, <UNKNOWN> |
| MDDEMO_MGR | MDDEMO_MGR, MGR |
| MDDEMO_CLERK | CLERK, MGR |
| #INTERNAL | ORACLE, SYS_STNT |
| INTERNAL | ORACLE, SYS_STNT |
| EJSADMIN | EJSADMIN, EJSADMIN_PASSWORD |
| DSGATEWAY | <UNKNOWN>, DSGATEWAY |
| CISINFO | CISINFO, ZWERG |
| CIS | CIS, ZWERG |
| AURORA$ORB$UNAUTHENTICATED | INVALID, <INVALID> |
| AURORA$JIS$UTILITY$ | <INVALID>, INVALID |
| ANONYMOUS | ANONYMOUS, <INVALID> |
| ADMINISTRATOR | ADMIN, ADMINISTRATOR |
| ADMIN | JETSPEED, WELCOME |

### J3 Web / App / Database Connectivity

- ACE: MC, P
- ICE: MC, P
- confidence: 4

> Common databases (MS SQL server, Oracle, MySQL and Access) and the connection and authentication methods used by web applications.
>

