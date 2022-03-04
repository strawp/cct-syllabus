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

### A3 Scoping

- ACE: MC
- ICE: MC

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

> Knowledge of additional risks that penetration testing can present.
>
> Levels of risk relating to penetration testing, the usual outcomes of such risks materialising and how to mitigate the risks.
>
> Effective planning for potential DoS conditions.

### A5 Record Keeping, Interim Reporting & Final Results

- ACE: MC, P
- ICE: MC, P

> Understanding reporting requirements.
>
> Understanding the importance of accurate and structured record keeping during the engagement.



## Appendix B: Core Technical Skills

### B1 IP Protocols

- ACE: MC
- ICE: MC

> IP protocols: IPv4 and IPv6, TCP, UDP and ICMP.
>
> Awareness that other IP protocols exist.

### B2 Network Architectures

- ACE: MC
- ICE: MC

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

> Network routing protocols RIP, OSPF, and IGRP/EIGRP.

### B4 Network Mapping & Target Identification

- ACE: MC, P
- ICE: MC, P

> Analysis of output from tools used to map the route between the engagement point and a number of targets.
>
> Network sweeping techniques to prioritise a target list and the potential for false negatives.

### B5 Interpreting Tool Output

- ACE: MC
- ICE: MC

> Interpreting output from port scanners, network sniffers and other network enumeration tools.

### B6 Filtering Avoidance Techniques

- ACE: MC
- ICE: MC

> The importance of egress and ingress filtering, including the risks associated with outbound connections.

### B7 Packet Crafting

- ACE: MC
- ICE: MC

> Packet crafting to meet a particular requirement:
>
> - Modifying source ports
>
> - Spoofing IP addresses
>
> - Manipulating TTL’s
>
> - Fragmentation
>
> - Generating ICMP packets
>

### B8 OS Fingerprinting

- ACE: MC
- ICE: MC, P

> Remote operating system fingerprinting; active and passive techniques.

### B9 Application Fingerprinting and Evaluating Unknown Services

- ACE: MC
- ICE: MC, P

> Determining server types and network application versions from application banners.
>
> Evaluation of responsive but unknown network applications.

### B10 Network Access Control Analysis

- ACE: MC
- ICE: MC

> Reviewing firewall rule bases and network access control lists.

### B11 Cryptography

- ACE: MC, P
- ICE: MC

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

> SSL, IPsec, SSH, PGP
>
> Common wireless (802.11) encryption protocols: WEP, WPA, TKIP

### B13 File System Permissions

- ACE: MC
- ICE: MC

> File permission attributes within Unix and Windows file systems and their security implications.
>
> Analysing registry ACLs.

### B14 Audit Techniques

- ACE: MC
- ICE: MC, P

> Listing processes and their associated network sockets (if any).
>
> Assessing patch levels.
>
> Finding interesting files.

## Appendix C: Background Information Gathering & Open Source

### C1 Registration Records

- ACE: MC
- ICE: MC

> Information contained within IP and domain registries (WHOIS).

### C2 Domain Name Server (DNS)

- ACE: MC
- ICE: MC, P

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

> Analysis of information from a target web site, both from displayed content and from within the HTML source.

### C4 Google Hacking and Web Enumeration

- ACE: MC
- ICE: MC

> Effective use of search engines and other public data sources to gain information about a target.

### C5 NNTP Newsgroups and Mailing Lists

- ACE: MC
- ICE: MC

> Searching newsgroups or mailing lists for useful information about a target.

### C6 Information Leakage from Mail & News Headers

- ACE: MC
- ICE: MC

> Analysing news group and e-mail headers to identify internal system information.

## Appendix D: Networking Equipment

### D1 Management Protocols

- ACE: MC
- ICE: MC, P

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

> Techniques for local network traffic analysis.
>
> Analysis of network traffic stored in PCAP files.

### D3 Networking Protocols

- ACE: MC
- ICE: MC, P

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

> Enumeration and fingerprinting of devices running IPSec services.
>

### D5 VoIP

- ACE: MC
- ICE: MC, P

> Enumeration and fingerprinting of devices running VoIP services.
>
> Knowledge of the SIP protocol.
>

### D6 Wireless

- ACE: MC
- ICE: MC

> Enumeration and fingerprinting of devices running Wireless (802.11) services.
>
> Knowledge of various options for encryption and authentication, and the relative methods of each.
>
> - WEP
>
> - TKIP
>
> - WPA/WPA2
>
> - EAP/LEAP/PEAP
>

### D7 Configuration Analysis

- ACE: MC
- ICE: MC, P

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

> Identifying user accounts on target systems and domains using NetBIOS, SNMP and LDAP.
>

### E3 Active Directory

- ACE: MC
- ICE: MC, P

> Active Directory Roles (Global Catalogue, Master Browser, FSMO)
>
> Reliance of AD on DNS and LDAP
>
> Group Policy (Local Security Policy)

### E4 Windows Passwords

- ACE: MC, P
- ICE: MC, P

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

> Knowledge and understanding of techniques to break out of a locked down Windows desktop / Citrix environment.
>
> Privilege escalation techniques.

### E8 Exchange

- ACE: MC
- ICE: MC

> Knowledge of common attack vectors for Microsoft Exchange Server.
>

### E9 Common Windows Applications

- ACE: MC
- ICE: MC, P

> Knowledge of significant vulnerabilities in common windows applications for which there is public exploit code available.

## Appendix F: Unix Security Assessment

### F1 User enumeration

- ACE: MC
- ICE: MC, P

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

> FTP access control
>
> Anonymous access to FTP servers
>
> Risks of allowing write access to anonymous users.

### F4 Sendmail / SMTP

- ACE: MC
- ICE: MC, P

> Valid username discovery via EXPN and VRFY
>
> Awareness of recent Sendmail vulnerabilities; ability to exploit them if possible
>
> Mail relaying

### F5 Network File System (NFS)

- ACE: MC
- ICE: MC, P

> NFS security: host level (exports restricted to particular hosts) and file level (by UID and GID).
>
> Root squashing, nosuid and noexec options.
>
> File access through UID and GID manipulation.

### F6 R* services

- ACE: MC
- ICE: MC, P

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

> X Windows security and configuration; hostbased vs. user-based access control.
>

### F8 RPC services

- ACE: MC
- ICE: MC, P

> RPC service enumeration
>
> Common RPC services
>
> Recent or commonly-found RPC service vulnerabilities.

### F9 SSH

- ACE: MC
- ICE: MC, P

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

> How a web server functions in terms of the client/server architecture.
>
> Concepts of virtual hosting and web proxies.

### G2 Web Servers & their Flaws

- ACE: MC, P
- ICE: MC, P

> Common web servers and their fundamental differences and vulnerabilities associated with them:
>
> - IIS
>
> - Apache (and variants)
>

### G3 Web Enterprise Architectures

- ACE: MC
- ICE: MC

> Design of tiered architectures.
>
> The concepts of logical and physical separation.
>
> Differences between presentation, application and database layers.

### G4 Web Protocols

- ACE: MC, P
- ICE: MC, P

> Web protocols: HTTP, HTTPS, SOAP.
>
> All HTTP web methods and response codes.
>
> HTTP Header Fields relating to security features

### G5 Web Mark-up Languages

- ACE: MC
- ICE: MC

> Web mark-up languages: HTML and XML.

### G6 Web Programming Languages

- ACE: MC
- ICE: MC

> Common web programming languages: JSP, ASP, PHP, CGI based Perl and JavaScript.
>

### G7 Web Application Servers

- ACE: MC, P
- ICE: MC

> Vulnerabilities in common application frameworks, servers and technologies: .NET, J2EE, Coldfusion, Ruby on Rails and AJAX.
>

### G8 Web APIs

- ACE: MC, P
- ICE: MC

> Application interfaces: CGI, ISAPI filters and Apache modules.
>

### G9 Web SubComponents

- ACE: MC, P
- ICE: MC

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

> Benefits of performing application reconnaissance.
>
> Discovering the structure of web applications.
>
> Methods to identify the use of application components defined in G1 to G9.

### H2 Threat Modelling and Attack Vectors

- ACE: MC
- ICE: MC

> Simple threat modelling based on customer perception of risk.
>
> Relate functionality offered by the application to potential attack vectors.

### H3 Information Gathering from Web Mark-up

- ACE: MC, P
- ICE: MC

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

> Common pitfalls associated with the design and implementation of application authentication mechanisms.

### H5 Authorisation Mechanisms

- ACE: MC, P
- ICE: MC

> Common pitfalls associated with the design and implementation of application authorisation mechanisms.
>

### H6 Input Validation

- ACE: MC, P
- ICE: MC

> The importance of input validation as part of a defensive coding strategy.
>
> How input validation can be implemented and the differences between white listing, black listing and data sanitisation.

### H7 Application Fuzzing

- ACE: MC, P
- ICE: MC

> Fuzzing and its relevance within web-app penetration testing.
>
> The use of fuzz strings and their potential effects.
>
> Potential dangers of fuzzing web applications.

### H8 Information Disclosure in Error Messages

- ACE: MC
- ICE: MC

> How error messages may indicate or disclose useful information.
>

### H9 Use of Cross Site Scripting Attacks

- ACE: MC, P
- ICE: MC

> Potential implications of a cross site scripting vulnerability.
>
> Ways in which the technique can be used to benefit an attacker.

### H10 Use of Injection Attacks

- ACE: MC, P
- ICE: MC

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

> Common pitfalls associated with the design and implementation of session handling mechanisms.

### H12 Encryption

- ACE: MC, P
- ICE: MC

> Common techniques used for encrypting data in transit and data at rest, either on the client or server side.
>
> Identification and exploitation of Encoded values (e.g. Base64) and Identification and exploitation of Cryptographic values (e.g. MD5 hashes)
>
> Identification of common SSL vulnerabilities

### H13 Source Code Review

- ACE: MC, P
- ICE: MC

> Common techniques for identifying and reviewing deficiencies in the areas of security.

## Appendix I: Web Testing Techniques

### I1 Web Site Structure Discovery

- ACE: P
- ICE: MC

> Spidering tools and their relevance in a web application test for discovering linked content.
>
> Forced browsing techniques to discover default or unlinked content.
>
> Identification of functionality within client-side code

### I2 Cross Site Scripting Attacks

- ACE: P
- ICE: MC

> Arbitrary JavaScript execution.
>
> Using Cross Site Scripting techniques to obtain sensitive information from other users.
>
> Phishing techniques.

### I3 SQL Injection

- ACE: P
- ICE: MC

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

> Investigate session handling within a web application.
>
> Harvest and analyse a number of session identifiers for weaknesses.

### I5 Fuzzing

- ACE: P
- ICE: MC

> The concept of fuzzing within a web application testing methodology.
>
> Common fuzzing tools.

### I6 Parameter Manipulation

- ACE: P
- ICE: MC

> Parameter manipulation techniques, particularly the use of client side proxies.

### I7 Data Confidentiality & Integrity

- ACE: P
- ICE: MC

> Identifying weak (or missing) encryption.
>
> Identifying insecure SSL configurations.
>
> Identify insecure use of encoding techniques

### I8 Directory Traversal

- ACE: P
- ICE: MC

> Identifying directory traversal vulnerabilities within applications.

### I9 File Uploads

- ACE: P
- ICE: MC

> Identifying common vulnerabilities with file upload capabilities within applications.

### I10 Code Injection

- ACE: P
- ICE: MC

> Investigate and exploitation of code injection vulnerabilities within web applications

### I11 CRLF Attacks

- ACE: P
- ICE: MC

> Assessment of web applications for CRLF vulnerabilities

### I12 Application Logic Flaws

- ACE: P
- ICE: MC

> Assessing the logic flow within an application and the potential for subverting the logic.

## Appendix J: Databases

### J1 Microsoft SQL Server

- ACE: MC, P
- ICE: MC, P

> Knowledge of common attack vectors for Microsoft SQL Server. Understanding of privilege escalation and attack techniques for a system compromised via database connections.

### J2 Oracle RDBMS

- ACE: MC, P
- ICE: MC, P

> Derivation of version and patch information from hosts running Oracle software.
>
> Default Oracle accounts.

### J3 Web / App / Database Connectivity

- ACE: MC, P
- ICE: MC, P

> Common databases (MS SQL server, Oracle, MySQL and Access) and the connection and authentication methods used by web applications.
>

