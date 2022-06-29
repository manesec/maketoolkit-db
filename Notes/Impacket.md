Copy from: [Impacket &ndash; SecureAuth](https://www.secureauth.com/labs/open-source-tools/impacket/)

Update Date: 2022-06-29

# Impacket

Impacket is a collection of Python classes for working with network protocols. Impacket is focused on providing low-level programmatic access to the packets and for some protocols (e.g. SMB1-3 and MSRPC) the protocol implementation itself.

Packets can be constructed from scratch, as well as parsed from raw data, and the object oriented API makes it simple to work with deep hierarchies of protocols. The library provides a set of tools as examples of what can be done within the context of this library.

### The following protocols are featured in Impacket

- Ethernet, Linux “Cooked” capture.
- IP, TCP, UDP, ICMP, IGMP, ARP.
- IPv4 and IPv6 Support.
- NMB and SMB1, SMB2 and SMB3 (high-level implementations).
- MSRPC version 5, over different transports: TCP, SMB/TCP, SMB/NetBIOS and HTTP.
- Plain, NTLM and Kerberos authentications, using password/hashes/tickets/keys.
- Portions/full implementation of the following MSRPC interfaces: EPM, DTYPES, LSAD, LSAT, NRPC, RRP, SAMR, SRVS, WKST, SCMR, DCOM, WMI
- Portions of TDS (MSSQL) and LDAP protocol implementations.

### The following tools are featured in Impacket

#### Remote Execution

- [psexec.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/psexec.py) PSEXEC like functionality example using RemComSvc ([GitHub - kavika13/RemCom: Remote Command Executor: A OSS replacement for PsExec and RunAs - or Telnet without having to install a server. Take your pick :)](https://github.com/kavika13/RemCom)).
- [smbexec.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/smbexec.py) A similar approach to PSEXEC w/o using RemComSvc. The technique is described [here](https://web.archive.org/web/20140625065218/http://blog.accuvant.com/rdavisaccuvant/owning-computers-without-shell-access/). Our implementation goes one step further, instantiating a local smbserver to receive the output of the commands. This is useful in the situation where the target machine does NOT have a writeable share available.
- [atexec.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/atexec.py) This example executes a command on the target machine through the Task Scheduler service and returns the output of the executed command.
- [wmiexec.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/wmiexec.py) A semi-interactive shell, used through Windows Management Instrumentation. It does not require to install any service/agent at the target server. Runs as Administrator. Highly stealthy.
- [dcomexec.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/dcomexec.py) A semi-interactive shell similar to wmiexec.py, but using different DCOM endpoints. Currently supports MMC20.Application, ShellWindows and ShellBrowserWindow objects.

#### Kerberos

- [GetTGT.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/getTGT.py) Given a password, hash or aesKey, this script will request a TGT and save it as ccache.
- [GetST.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/getST.py) Given a password, hash, aesKey or TGT in ccache, this script will request a Service Ticket and save it as ccache. If the account has constrained delegation (with protocol transition) privileges you will be able to use the -impersonate switch to request the ticket on behalf another user.
- [GetPac.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/getPac.py) This script will get the PAC (Privilege Attribute Certificate) structure of the specified target user just having a normal authenticated user credentials. It does so by using a mix of [MS-SFU]’s S4USelf + User to User Kerberos Authentication.
- [GetUserSPNs.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/GetUserSPNs.py) This example will try to find and fetch Service Principal Names that are associated with normal user accounts. Output is compatible with JtR and HashCat.
- [GetNPUsers.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/GetNPUsers.py) This example will attempt to list and get TGTs for those users that have the property ‘Do not require Kerberos preauthentication’ set (UF_DONT_REQUIRE_PREAUTH). Output is compatible with JtR.
- [rbcd.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/rbcd.py): Example script for handling the msDS-AllowedToActOnBehalfOfOtherIdentity property of a target computer.
- [ticketConverter.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_9_24/examples/ticketConverter.py): This script will convert kirbi files, commonly used by mimikatz, into ccache files used by Impacket, and vice versa.
- [ticketer.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/ticketer.py) This script will create Golden/Silver tickets from scratch or based on a template (legally requested from the KDC) allowing you to customize some of the parameters set inside the PAC_LOGON_INFO structure, in particular the groups, ExtraSids, duration, etc.
- [raiseChild.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/raiseChild.py) This script implements a child-domain to forest privilege escalation by (ab)using the concept of Golden Tickets and ExtraSids.

#### Windows Secrets

- [secretsdump.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/secretsdump.py) Performs various techniques to dump secrets from the remote machine without executing any agent there. For SAM and LSA Secrets (including cached creds) we try to read as much as we can from the registry and then we save the hives in the target system (%SYSTEMROOT%\Temp directory) and read the rest of the data from there. For DIT files, we dump NTLM hashes, Plaintext credentials (if available) and Kerberos keys using the DL_DRSGetNCChanges() method. It can also dump NTDS.dit via vssadmin executed with the smbexec/wmiexec approach. The script initiates the services required for its working if they are not available (e.g. Remote Registry, even if it is disabled). After the work is done, things are restored to the original state.
- [mimikatz.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/mimikatz.py) Mini shell to control a remote mimikatz RPC server developed by @gentilkiwi.

#### Server Tools/MiTM Attacks

- [ntlmrelayx.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/ntlmrelayx.py) This script performs NTLM Relay Attacks, setting an SMB, HTTP, WCF and RAW Server and relaying credentials to many different protocols (SMB, HTTP, MSSQL, LDAP, IMAP, POP3, etc.). The script can be used with predefined attacks that can be triggered when a connection is relayed (e.g. create a user through LDAP) or can be executed in SOCKS mode. In this mode, for every connection relayed, it will be available to be used later on multiple times through a SOCKS proxy.
- [karmaSMB.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/karmaSMB.py) A SMB Server that answers specific file contents regardless of the SMB share and pathname specified.
- [smbserver.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/smbserver.py) A Python implementation of an SMB server. Allows to quickly set up shares and user accounts.

#### WMI

- [wmiquery.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/wmiquery.py) It allows to issue WQL queries and get description of WMI objects at the target system (e.g. select name from win32_account).
- [wmipersist.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/wmipersist.py) This script creates/removes a WMI Event Consumer/Filter and link between both to execute Visual Basic based on the WQL filter or timer specified.

#### Known Vulnerabilities

- [goldenPac.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/goldenPac.py) Exploit for MS14-068. Saves the golden ticket and also launches a PSEXEC session at the target.
- [sambaPipe.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/sambaPipe.py) This script will exploit CVE-2017-7494, uploading and executing the shared library specified by the user through the -so parameter.
- [smbrelayx.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/smbrelayx.py) Exploit for CVE-2015-0005 using a SMB Relay Attack. If the target system is enforcing signing and a machine account was provided, the module will try to gather the SMB session key through NETLOGON.

#### SMB/MSRPC

- [smbclient.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/smbclient.py) A generic SMB client that will let you list shares and files, rename, upload and download files and create and delete directories, all using either username and password or username and hashes combination. It’s an excellent example to see how to use impacket.smb in action.
- [addcomputer.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/addcomputer.py): Allows to add a computer to a domain using LDAP or SAMR (SMB).
- [getArch.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/getArch.py) This script will connect against a target (or list of targets) machine/s and gather the OS architecture type installed by (ab)using a documented MSRPC feature.
- [exchanger.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/exchanger.py): A tool for connecting to MS Exchange via RPC over HTTP v2.
- [lookupsid.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/lookupsid.py) A Windows SID brute forcer example through [MS-LSAT] MSRPC Interface, aiming at finding remote users/groups.
- [netview.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/netview.py) Gets a list of the sessions opened at the remote hosts and keep track of them looping over the hosts found and keeping track of who logged in/out from remote servers
- [reg.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/reg.py) Remote registry manipulation tool through the [MS-RRP] MSRPC Interface. The idea is to provide similar functionality as the REG.EXE Windows utility.
- [rpcdump.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/rpcdump.py) This script will dump the list of RPC endpoints and string bindings registered at the target. It will also try to match them with a list of well known endpoints.
- [rpcmap.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/rpcmap.py): Scan for listening DCE/RPC interfaces. This binds to the MGMT interface and gets a list of interface UUIDs. If the MGMT interface is not available, it takes a list of interface UUIDs seen in the wild and tries to bind to each interface.
- [samrdump.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/samrdump.py) An application that communicates with the Security Account Manager Remote interface from the MSRPC suite. It lists system user accounts, available resource shares and other sensitive information exported through this service.
- [services.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/services.py) This script can be used to manipulate Windows services through the [MS-SCMR] MSRPC Interface. It supports start, stop, delete, status, config, list, create and change.
- [smbpasswd.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/smbpasswd.py): This script is an alternative to smbpasswd tool and intended to be used for changing expired passwords remotely over SMB (MSRPC-SAMR)

#### MSSQL / TDS

- [mssqlinstance.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/mssqlinstance.py) Retrieves the MSSQL instances names from the target host.
- [mssqlclient.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/mssqlclient.py) An MSSQL client, supporting SQL and Windows Authentications (hashes too). It also supports TLS.

#### File Formats

- [esentutl.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/esentutl.py) An Extensibe Storage Engine format implementation. Allows dumping catalog, pages and tables of ESE databases (e.g. NTDS.dit)
- [ntfs-read.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/ntfs-read.py) NTFS format implementation. This script provides a mini shell for browsing and extracting an NTFS volume, including hidden/locked contents.
- [registry-read.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/registry-read.py) A Windwows Registry file format implementation. It allows to parse offline registry hives.

#### Other

- [findDelegation.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/findDelegation.py): Simple script to quickly list all delegation relationships (unconstrained, constrained, resource-based constrained) in an AD environment.
- [GetADUsers.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/GetADUsers.py) This script will gather data about the domain’s users and their corresponding email addresses. It will also include some extra information about last logon and last password set attributes.
- [Get-GPPPassword.py](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/Get-GPPPassword.py): This example extracts and decrypts Group Policy Preferences passwords using streams for treating files instead of mounting shares. Additionally, it can parse GPP XML files offline.
- [mqtt_check.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/mqtt_check.py) Simple MQTT example aimed at playing with different login options. Can be converted into a account/password brute forcer quite easily.
- [rdp_check.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/rdp_check.py) [MS-RDPBCGR] and [MS-CREDSSP] partial implementation just to reach CredSSP auth. This example tests whether an account is valid on the target host.
- [sniff.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/sniff.py) Simple packet sniffer that uses the pcapy library to listen for packets in # transit over the specified interface.
- [sniffer.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/sniffer.py) Simple packet sniffer that uses a raw socket to listen for packets in transit corresponding to the specified protocols.
- [ping.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/ping.py) Simple ICMP ping that uses the ICMP echo and echo-reply packets to check the status of a host. If the remote host is up, it should reply to the echo probe with an echo-reply packet.
- [ping6.py:](https://github.com/SecureAuthCorp/impacket/blob/impacket_0_10_0/examples/ping6.py) Simple IPv6 ICMP ping that uses the ICMP echo and echo-reply packets to check the status of a host.

### Source code

- You can check out trunk (development version) at [GitHub - SecureAuthCorp/impacket: Impacket is a collection of Python classes for working with network protocols.](https://github.com/SecureAuthCorp/impacket)
- 0.10.0, updated on May4th, 2022 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_10_0/impacket-0.10.0.tar.gz)
- 0.9.24, updated on Oct 27th, 2021 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_24/impacket-0.9.24.tar.gz)
- 0.9.23, updated on Jun 9th, 2021 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_23/impacket-0.9.23.tar.gz)
- 0.9.22, updated on Nov 23th, 2020 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_22/impacket-0.9.22.tar.gz)
- 0.9.21, updated on Mar 26th, 2020 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_21/impacket-0.9.21.tar.gz)
- 0.9.20, updated on Sep 25th, 2019 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_20/impacket-0.9.20.tar.gz)
- 0.9.19, updated on Apr 1st, 2019 – [gzip’d tarball](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_19/impacket-0.9.19.tar.gz)
- 0.9.18, updated on Dec 5th, 2018 – [gzip’d tarball](https://files.pythonhosted.org/packages/71/a5/f25ac0036c2b85e48aee740a99c3ab82196a05d8a4203fac6e8283ea5b0b/impacket-0.9.18.tar.gz)
- 0.9.17, updated on May 30th, 2018 – [gzip’d tarball](https://files.pythonhosted.org/packages/09/26/de84602349ca97b78d1720045db662c7eb261d2daf4a3b509b7ee387de74/impacket-0.9.17.tar.gz)
- 0.9.15, updated on Jun 28th, 2016 – [gzip’d tarball](https://pypi.python.org/packages/35/72/694c391c7fe29600c2c8d8d4aa97a781562c39bb66a3d20bbee9858ca698/impacket-0.9.15.tar.gz#md5=53fb6d1c375dd3ef8fff4ce2b7ff8f15)
- 0.9.14, updated on Jan 7th, 2016 – [gzip’d tarball](https://pypi.python.org/packages/source/i/impacket/impacket-0.9.14.tar.gz),
- 0.9.13, updated on May 4th, 2015 – [gzip’d tarball](https://pypi.python.org/packages/source/i/impacket/impacket-0.9.13.tar.gz),
- 0.9.12, updated on July 20th, 2014 – [gzip’d tarball](https://pypi.python.org/packages/source/i/impacket/impacket-0.9.12.tar.gz),
- 0.9.11, updated on Feb 3, 2014 – [gzip’d tarball](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/impacket-0.9.11.tar_.gz),
- 0.9.10, updated on May 6, 2013 – [gzip’d tarball](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/impacket-0.9.10.tar_.gz),
- 0.9.9.9, updated on July 20, 2012 – [gzip’d tarball](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/impacket-0.9.9.9.tar_.gz), [zip file](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/impacket-0.9.9.9.zip)
- 0.9.6.0, updated on May 23, 2006 – [gzip’d tarball](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/Impacket-0.9.6.0.tar_.gz)
- 0.9.5.2, updated on Apr 3, 2006 – [gzip’d tarball](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/Impacket-0.9.5.2.tar_.gz), [zip file](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/Impacket-0.9.5.2.zip)
- 0.9.5.1, updated on Dec 16, 2003 – [gzip’d tarball](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/Impacket-0.9.5.1.tar_.gz), [zip file](https://secureauthcorp.wpengine.com/wp-content/uploads/2020/03/Impacket-0.9.5.1.zip)

### Setup

#### Requirements:

- [Python](http://www.python.org/) interpreter (version 3.6, 3.7, 3.8 or 3.9).
- [Third-party](https://github.com/SecureAuthCorp/impacket/blob/master/requirements.txt) packages also needed.

#### Installing:

- Grab the latest stable release ([gzip’d tarbal](https://github.com/SecureAuthCorp/impacket/releases/download/impacket_0_9_24/impacket-0.9.24.tar.gz)), unpack it and run: **python3 -m pip install .**  from the directory where you placed it.  This will install the classes into the default Python modules path; note that you might need special permissions to write there.

#### Docker Support:

- Build Impacket’s image:  **docker build -t “impacket:latest” .**
- Using Impacket’s image:  **docker run -it –rm “impacket:latest”**

### Documentation

We wish we had more documentation available (in progress, help needed!) so most documentation is included in the source as Python’s doc comments. You can also learn a lot about the library functionality through its [test cases](https://github.com/SecureAuthCorp/impacket/tree/master/tests) and [examples](https://github.com/SecureAuthCorp/impacket/tree/master/examples).

### Licensing

This software is provided under a slightly modified version of the Apache Software License. Feel free to review it [here](https://github.com/SecureAuthCorp/impacket/tree/impacket_0_9_24/LICENSE) and compare it to the official Apache Software License.

### Contact Us

Whether you want to report a bug, send a patch or give some suggestions on this package, drop us a few lines at oss@secureauth.com.

**Release date:** 2003-2022#
