---
ref: SYL_CCT_V2.0
version: 2.2
status: Public Release
issue date: 2017-05-17
issued by: CREST Technical Committee and Assessors Panel
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

| Version | Date | Authors | Status |
| ------- | ---- | ------- | ------ |
| 1.0     | 27 May 2016 | Technical Committee and Assessors Panel | Internal Review |
| 2.0 | 3 June 2016 | Technical Committee and Assessors Panel | Public Release | 
| 2.1 | 30 September 2016 | Technical Committee and Assessors Panel | Public Release |
| 2.2 | 16 May 2017 | Technical Committee and Assessors Panel | Public Release |


## Document Review

| Reviewer | Position |
| -------- | -------- |
| Chair    | Technical Committee / Assessors Panel |
| Chair    | CREST Board |


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

## Appendix A:

Soft Skills and Assessment Management

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

A1

Engagement
Lifecycle

Benefits and utility of penetration testing to the
client.

MC

MC

MC

MC

MC

MC

MC

MC

MC

MC

P

P

Structure of penetration testing, including the
relevant processes and procedures.
Concepts of infrastructure testing and
application testing, including black box and white
box formats.
Project closure and debrief
A2

Law &
Compliance

Knowledge of pertinent UK legal issues:


Computer Misuse Act 1990



Human Rights Act 1998



Data Protection Act 1998



Police and Justice Act 2006

Impact of this legislation on penetration testing
activities.
Awareness of sector-specific regulatory issues.
A3

Scoping

Understanding client requirements.
Scoping project to fulfil client requirements.
Accurate timescale scoping.
Resource planning.

A4

Understanding
Explaining and
Managing Risk

Knowledge of additional risks that penetration
testing can present.
Levels of risk relating to penetration testing, the
usual outcomes of such risks materialising and
how to mitigate the risks.
Effective planning for potential DoS conditions.

A5

Record Keeping,
Interim
Reporting &
Final Results

Version: 2.2

Understanding reporting requirements.
Understanding the importance of accurate and
structured record keeping during the
engagement.

Page 5 of 19

Date: 17th May 2017



## Appendix B: Core Technical Skills

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

B1

IP Protocols

IP protocols: IPv4 and IPv6, TCP, UDP and
ICMP.

MC

MC

MC

MC

Awareness that other IP protocols exist.
B2

Network
Architectures

Varying networks types that could be
encountered during a penetration test:


CAT 5 / Fibre



10/100/1000baseT



Token ring



Wireless (802.11)

Security implications of shared media,
switched media and VLANs.
B3

Network Routing

Network routing protocols RIP, OSPF, and
IGRP/EIGRP.

MC

MC

B4

Network Mapping
& Target
Identification

Analysis of output from tools used to map the
route between the engagement point and a
number of targets.

MC

MC

P

P

Network sweeping techniques to prioritise a
target list and the potential for false
negatives.
B5

Interpreting Tool
Output

Interpreting output from port scanners,
network sniffers and other network
enumeration tools.

MC

MC

B6

Filtering
Avoidance
Techniques

The importance of egress and ingress
filtering, including the risks associated with
outbound connections.

MC

MC

B7

Packet Crafting

Packet crafting to meet a particular
requirement:

MC

MC

MC

MC

B8

OS Fingerprinting

Version: 2.2



Modifying source ports



Spoofing IP addresses



Manipulating TTL’s



Fragmentation



Generating ICMP packets

Remote operating system fingerprinting;
active and passive techniques.

Page 6 of 19

P

Date: 17th May 2017

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

B9

Application
Fingerprinting and
Evaluating
Unknown
Services

Determining server types and network
application versions from application
banners.

B10

Network Access
Control Analysis

Reviewing firewall rule bases and network
access control lists.

MC

MC

B11

Cryptography

Differences between encryption and
encoding.

MC

MC

MC

MC
P

Evaluation of responsive but unknown
network applications.

P

Symmetric / asymmetric encryption
Encryption algorithms: DES, 3DES, AES,
RSA, RC4.
Hashes: SHA1 and MD5
Message Integrity codes: HMAC
B12

B13

Applications of
Cryptography

SSL, IPsec, SSH, PGP

File System
Permissions

File permission attributes within Unix and
Windows file systems and their security
implications.

MC

MC

MC

MC

Common wireless (802.11) encryption
protocols: WEP, WPA, TKIP

P

Analysing registry ACLs.
B14

Audit Techniques

Listing processes and their associated
network sockets (if any).

MC

MC
P

Assessing patch levels.
Finding interesting files.

Version: 2.2

Page 7 of 19

Date: 17th May 2017

## Appendix C: Background Information Gathering & Open Source

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

C1

Registration
Records

Information contained within IP and domain
registries (WHOIS).

MC

MC

C2

Domain Name
Server (DNS)

DNS queries and responses

MC

MC

DNS zone transfers

P

Structure, interpretation and analysis of DNS
records:

C3



SOA



MX



TXT



A



NS



PTR



HINFO



CNAME

Customer Web
Site Analysis

Analysis of information from a target web
site, both from displayed content and from
within the HTML source.

MC

C4

Google Hacking
and Web
Enumeration

Effective use of search engines and other
public data sources to gain information about
a target.

MC

MC

C5

NNTP
Newsgroups and
Mailing Lists

Searching newsgroups or mailing lists for
useful information about a target.

MC

MC

C6

Information
Leakage from
Mail & News
Headers

Analysing news group and e-mail headers to
identify internal system information.

MC

MC

Version: 2.2

Page 8 of 19

MC

P

Date: 17th May 2017

## Appendix D: Networking Equipment

ID

Skill

Details

D1

Management
Protocols

Weaknesses in the protocols commonly used
for the remote management of devices:

D2

D3

D4

D5

How Examined
CCT ACE
CCT ICE



Telnet



Web based protocols



SSH



SNMP (covering network information
enumeration and common attacks
against Cisco configurations)



TFTP



Cisco Reverse Telnet



NTP

Network Traffic
Analysis

Techniques for local network traffic analysis.

Networking
Protocols

Security issues relating to the networking
protocols:

IPSec

VoIP

MC

MC
P

MC

MC

MC

MC

Analysis of network traffic stored in PCAP
files.



ARP



DHCP



CDP



HSRP



VRRP



VTP



STP



TACACS+

P

Enumeration and fingerprinting of devices
running IPSec services.

MC

Enumeration and fingerprinting of devices
running VoIP services.

MC

MC
P
MC
P

Knowledge of the SIP protocol.

Version: 2.2

Page 9 of 19

Date: 17th May 2017

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

D6

Wireless

Enumeration and fingerprinting of devices
running Wireless (802.11) services.

MC

MC

MC

MC

Knowledge of various options for encryption
and authentication, and the relative methods
of each.

D7

Configuration
Analysis



WEP



TKIP



WPA/WPA2



EAP/LEAP/PEAP

Analysing configuration files from the
following types of Cisco equipment:


Routers



Switches

P

Interpreting the configuration of other
manufacturers’ devices.

Version: 2.2

Page 10 of 19

Date: 17th May 2017

## Appendix E: Microsoft Windows Security Assessment



ID

Skill

Details

How Examined
CCT ACE
CCT ICE

E1

Domain
Reconnaissance

Identifying domains/workgroups and domain
membership within the target network.

MC

MC
P

Identifying key servers within the target
domains.
Identifying and analysing internal browse
lists.
Identifying and analysing accessible SMB
shares
E2

E3

User Enumeration

Active Directory

Identifying user accounts on target systems
and domains using NetBIOS, SNMP and
LDAP.

MC

Active Directory Roles (Global Catalogue,
Master Browser, FSMO)

MC

MC
P
MC
P

Reliance of AD on DNS and LDAP
Group Policy (Local Security Policy)
E4

Windows
Passwords

Password policies (complexity, lockout
policies)

MC

MC

P

P

Account Brute Forcing
Hash Storage (merits of LANMAN, NTLMv1 /
v2)
Offline Password Analysis (rainbow tables /
hash brute forcing)

Version: 2.2

Page 11 of 19

Date: 17th May 2017

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

E5

Windows
Vulnerabilities

Knowledge of remote windows vulnerabilities,
particularly those for which robust exploit
code exists in the public domain.

MC

MC

P

P

MC

MC

Knowledge of local windows privilege
escalation vulnerabilities and techniques.
Knowledge of common post exploitation
activities:

E6

E7

Windows Patch
Management
Strategies

Desktop
Lockdown



obtain password hashes, both from
the local SAM and cached
credentials



obtaining locally-stored clear-text
passwords



crack password hashes



check patch levels



derive list of missing security patches



reversion to previous state

Knowledge of common windows patch
management strategies:


SMS



SUS



WSUS



MBSA

Knowledge and understanding of techniques
to break out of a locked down Windows
desktop / Citrix environment.

P

MC

MC
P

Privilege escalation techniques.
E8

Exchange

Knowledge of common attack vectors for
Microsoft Exchange Server.

MC

MC

E9

Common
Windows
Applications

Knowledge of significant vulnerabilities in
common windows applications for which
there is public exploit code available.

MC

MC

Version: 2.2

Page 12 of 19

P

Date: 17th May 2017

## Appendix F: Unix Security Assessment



ID

Skill

Details

How Examined
CCT ACE
CCT ICE

F1

User enumeration

Discovery of valid usernames from network
services commonly running by default:


rusers



rwho



SMTP



finger

MC

MC
P

Understand how finger daemon derives the
information that it returns, and hence how it
can be abused.
F2

Unix
vulnerabilities

Recent or commonly-found Solaris
vulnerabilities, and in particular those for
which there is exploit code in the public
domain.

MC

MC
P

Recent or commonly-found Linux
vulnerabilities, and in particular those for
which there is exploit code in the public
domain.
Use of remote exploit code and local exploit
code to gain root access to target host
Common post-exploitation activities:

F3

FTP



exfiltrate password hashes



crack password hashes



check patch levels



derive list of missing security patches



reversion to previous state

FTP access control

MC

Anonymous access to FTP servers

MC
P

Risks of allowing write access to anonymous
users.
F4

Sendmail / SMTP

Valid username discovery via EXPN and
VRFY

MC

MC
P

Awareness of recent Sendmail vulnerabilities;
ability to exploit them if possible
Mail relaying

Version: 2.2

Page 13 of 19

Date: 17th May 2017

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

F5

Network File
System (NFS)

NFS security: host level (exports restricted to
particular hosts) and file level (by UID and
GID).

MC

MC
P

Root squashing, nosuid and noexec options.
File access through UID and GID
manipulation.
F6

R* services

Berkeley r* service:

MC



access control (/etc/hosts.equiv and
.rhosts)



trust relationships

MC
P

Impact of poorly-configured trust
relationships.
F7

F8

X11

RPC services

X Windows security and configuration; hostbased vs. user-based access control.

MC

RPC service enumeration

MC

MC
P

Common RPC services

MC
P

Recent or commonly-found RPC service
vulnerabilities.
F9

SSH

Identify the types and versions of SSH
software in use

MC

MC
P

Securing SSH
Versions 1 and 2 of the SSH protocol
Authentication mechanisms within SSH

Version: 2.2

Page 14 of 19

Date: 17th May 2017

## Appendix G: Web Technologies



ID

Skill

Details

How Examined
CCT ACE
CCT ICE

G1

Web Server
Operation

How a web server functions in terms of the
client/server architecture.

MC

MC

MC

MC

P

P

MC

MC

MC

MC

P

P

Concepts of virtual hosting and web proxies.
G2

G3

Web Servers &
their Flaws

Web Enterprise
Architectures

Common web servers and their fundamental
differences and vulnerabilities associated
with them:


IIS



Apache (and variants)

Design of tiered architectures.
The concepts of logical and physical
separation.
Differences between presentation,
application and database layers.

G4

Web Protocols

Web protocols: HTTP, HTTPS, SOAP.
All HTTP web methods and response codes.
HTTP Header Fields relating to security
features

G5

Web Mark-up
Languages

Web mark-up languages: HTML and XML.

MC

MC

G6

Web
Programming
Languages

Common web programming languages: JSP,
ASP, PHP, CGI based Perl and JavaScript.

MC

MC

G7

Web Application
Servers

Vulnerabilities in common application
frameworks, servers and technologies: .NET,
J2EE, Coldfusion, Ruby on Rails and AJAX.

MC

MC

Web APIs

Application interfaces: CGI, ISAPI filters and
Apache modules.

MC

Web architecture sub-components:
Thin/Thick web clients, servlets and applets,
Active X.

MC

G8

G9

Web SubComponents

P
MC

P
MC

P

Flash Application Testing
.Net Thick Clients
Java Applets
Decompilation of client-side code

Version: 2.2

Page 15 of 19

Date: 17th May 2017

## Appendix H: Web Testing Methodologies



ID

Skill

Details

How Examined
CCT ACE
CCT ICE

H1

Web Application
Reconnaissance

Benefits of performing application
reconnaissance.

MC

MC

MC

MC

MC

MC

Discovering the structure of web applications.
Methods to identify the use of application
components defined in G1 to G9.
H2

H3

H4

H5

H6

Threat Modelling
and Attack
Vectors

Simple threat modelling based on customer
perception of risk.

Information
Gathering from
Web Mark-up

Examples of the type of information available
in web page source that may prove useful to
an attacker:

Relate functionality offered by the application
to potential attack vectors.



Hidden Form Fields



Database Connection Strings



Credentials



Developer Comments



Other included files



Authenticated-only URLs

P

Authentication
Mechanisms

Common pitfalls associated with the design
and implementation of application
authentication mechanisms.

MC

Authorisation
Mechanisms

Common pitfalls associated with the design
and implementation of application
authorisation mechanisms.

MC

Input Validation

The importance of input validation as part of
a defensive coding strategy.

MC

MC

P
MC

P
MC

P

How input validation can be implemented and
the differences between white listing, black
listing and data sanitisation.
H7

Application
Fuzzing

Fuzzing and its relevance within web-app
penetration testing.

MC

MC

P

The use of fuzz strings and their potential
effects.
Potential dangers of fuzzing web
applications.

Version: 2.2

Page 16 of 19

Date: 17th May 2017

ID

Skill

Details

How Examined
CCT ACE
CCT ICE

H8

Information
Disclosure in
Error Messages

How error messages may indicate or disclose
useful information.

MC

MC

H9

Use of Cross Site
Scripting Attacks

Potential implications of a cross site scripting
vulnerability.

MC

MC

P

Ways in which the technique can be used to
benefit an attacker.
H10

Use of Injection
Attacks

Potential implications of injection
vulnerabilities:

MC

MC

P

 SQL injection
 LDAP injection
 Code injection
 XML injection
Ways in which these techniques can be used
to benefit an attacker.
H11

H12

Session Handling

Encryption

Common pitfalls associated with the design
and implementation of session handling
mechanisms.

MC

Common techniques used for encrypting data
in transit and data at rest, either on the client
or server side.

MC

MC

P
MC

P

Identification and exploitation of Encoded
values (e.g. Base64) and Identification and
exploitation of Cryptographic values (e.g.
MD5 hashes)
Identification of common SSL vulnerabilities
H13

Source Code
Review

Version: 2.2

Common techniques for identifying and
reviewing deficiencies in the areas of
security.

Page 17 of 19

MC

MC

P

Date: 17th May 2017

## Appendix I: Web Testing Techniques



ID

Skill

Details

How Examined
CCT ACE
CCT ICE

I1

Web Site
Structure
Discovery

Spidering tools and their relevance in a web
application test for discovering linked content.

P

MC

P

MC

P

MC

P

MC

P

MC

Forced browsing techniques to discover default
or unlinked content.
•Identification of functionality within client-side
code

I2

Cross Site
Scripting
Attacks

Arbitrary JavaScript execution.
Using Cross Site Scripting techniques to obtain
sensitive information from other users.
Phishing techniques.

I3

SQL Injection

Determine the existence of an SQL injection
condition in a web application.
Determine the existence of a blind SQL injection
condition in a web application.
Exploit SQL injection to enumerate the database
and its structure.
Exploit SQL injection to execute commands on
the target server.

I4

Session ID
Attacks

Investigate session handling within a web
application.
Harvest and analyse a number of session
identifiers for weaknesses.

I5

Fuzzing

The concept of fuzzing within a web application
testing methodology.
Common fuzzing tools.

I6

Parameter
Manipulation

Parameter manipulation techniques, particularly
the use of client side proxies.

P

MC

I7

Data
Confidentiality &
Integrity

Identifying weak (or missing) encryption.

P

MC

Identifying insecure SSL configurations.
Identify insecure use of encoding techniques

I8

Directory
Traversal

Identifying directory traversal vulnerabilities
within applications.

P

MC

I9

File Uploads

Identifying common vulnerabilities with file
upload capabilities within applications.

P

MC

Version: 2.2

Page 18 of 19

Date: 17th May 2017

ID

Skill

Details

I10

Code Injection

Investigate and exploitation of code injection
vulnerabilities within web applications

P

MC

I11

CRLF Attacks

Assessment of web applications for CRLF
vulnerabilities

P

MC

I12

Application
Logic Flaws

Assessing the logic flow within an application
and the potential for subverting the logic.

P

MC

## Appendix J: Databases

How Examined
CCT ACE
CCT ICE

ID

Skill

Details

J1

Microsoft SQL
Server

Knowledge of common attack vectors for
Microsoft SQL Server. Understanding of
privilege escalation and attack techniques for a
system compromised via database connections.

MC

MC

P

P

Oracle RDBMS

Derivation of version and patch information from
hosts running Oracle software.

MC

MC

P

P

MC

MC

P

P

J2

How Examined
CCT ACE
CCT ICE

Default Oracle accounts.
J3

Web / App /
Database
Connectivity

Version: 2.2

Common databases (MS SQL server, Oracle,
MySQL and Access) and the connection and
authentication methods used by web
applications.

Page 19 of 19

Date: 17th May 2017


