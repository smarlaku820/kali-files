# Windows Registry

## HKEY_CURRENT_USER (HKCU)
- Contains the root of the configuration information for the user who is currently logged on. 
- The user's folders, screen colors, and Control Panel settings are stored here. This information is associated with the user's profile. This key is sometimes abbreviated as HKCU.

## HKEY_USERS (HKU)
- Contains all the actively loaded user profiles on the computer. 
- HKEY_CURRENT_USER is a subkey of HKEY_USERS. HKEY_USERS is sometimes abbreviated as HKU.

## HKEY_LOCAL_MACHINE (HKLM)
- Contains configuration information particular to the computer (for any user). This key is sometimes abbreviated as HKLM.

## HKEY_CLASSES_ROOT 
- Is a subkey of HKEY_LOCAL_MACHINE\Software. The information that is stored here makes sure that the correct program opens when you open a file by using Windows Explorer. This key is sometimes abbreviated as HKCR.
- Starting with Windows 2000, this information is stored under both the HKEY_LOCAL_MACHINE and HKEY_CURRENT_USER keys. The HKEY_LOCAL_MACHINE\Software\Classes key contains default settings that can apply to all users on the local computer. The HKEY_CURRENT_USER\Software\Classes key has settings that override the default settings and apply only to the interactive user.
- The HKEY_CLASSES_ROOT key provides a view of the registry that merges the information from these two sources. HKEY_CLASSES_ROOT also provides this merged view for programs that are designed for earlier versions of Windows. To change the settings for the interactive user, changes must be made under HKEY_CURRENT_USER\Software\Classes instead of under HKEY_CLASSES_ROOT.
- To change the default settings, changes must be made under HKEY_LOCAL_MACHINE\Software\Classes .If you write keys to a key under HKEY_CLASSES_ROOT, the system stores the information under HKEY_LOCAL_MACHINE\Software\Classes
- If you write values to a key under HKEY_CLASSES_ROOT, and the key already exists under HKEY_CURRENT_USER\Software\Classes, the system will store the information there instead of under HKEY_LOCAL_MACHINE\Software\Classes.

## HKEY_CURRENT_CONFIG
- Contains information about the hardware profile that is used by the local computer at system startup.

## Offline access of registry hives
- C:\Windows\System32\Config
DEFAULT (mounted on HKEY_USERS\DEFAULT)
SAM (mounted on HKEY_LOCAL_MACHINE\SAM)
SECURITY (mounted on HKEY_LOCAL_MACHINE\Security)
SOFTWARE (mounted on HKEY_LOCAL_MACHINE\Software)
SYSTEM (mounted on HKEY_LOCAL_MACHINE\System)
- Apart from these hives, two other hives containing user information can be found in the User profile directory. For Windows 7 and above, a user’s profile directory is located in C:\Users\<username>\ where the hives are:
NTUSER.DAT (mounted on HKEY_CURRENT_USER when a user logs in)
USRCLASS.DAT (mounted on HKEY_CURRENT_USER\Software\CLASSES)
- The USRCLASS.DAT hive is located in the directory C:\Users\<username>\AppData\Local\Microsoft\Windows. 
- The NTUSER.DAT hive is located in the directory C:\Users\<username>\.
- Apart from these files, there is another very important hive called the AmCache hive. This hive is located in C:\Windows\AppCompat\Programs\Amcache.hve. Windows creates this hive to save information on programs that were recently run on the system.

## Tracking Changes/Edits to Reg Hives | Performing Backup's of Reg Hives
- Some other very vital sources of forensic data are the registry transaction logs and backups. The transaction logs can be considered as the journal of the changelog of the registry hive. Windows often uses transaction logs when writing data to registry hives. This means that the transaction logs can often have the latest changes in the registry that haven't made their way to the registry hives themselves. The transaction log for each hive is stored as a .LOG file in the same directory as the hive itself. It has the same name as the registry hive, but the extension is .LOG. For example, the transaction log for the SAM hive will be located in C:\Windows\System32\Config in the filename SAM.LOG. Sometimes there can be multiple transaction logs as well. In that case, they will have .LOG1, .LOG2 etc., as their extension. It is prudent to look at the transaction logs as well when performing registry forensics.

- Registry backups are the opposite of Transaction logs. These are the backups of the registry hives located in the C:\Windows\System32\Config directory. These hives are copied to the C:\Windows\System32\Config\RegBack directory every ten days. It might be an excellent place to look if you suspect that some registry keys might have been deleted/modified recently.

