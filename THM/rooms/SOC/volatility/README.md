# Volatility

## Live Machines Memory Capture
- [RedLine from FireEye](https://fireeye.market/apps/211364)
- [FTK Imager](https://accessdata.com/product-download/ftk-imager-version-4-2-0)
- DumpIt.exe
- win32dd.exe / win64dd.exe - *Has fantastic psexec support, great for IT departments if your EDR solution doesn't support this*
- The above tools usually dump a **.raw** file which contains an image of system memory

## Offline Machines
- %SystemDrive%/hiberfil.sys
- `hiberfil.sys`, better known as the Windows hibernation file contains a compressed memory image from the previous boot. Microsoft Windows systems use this in order to provide faster boot-up times, however, we can use this file in our case for some memory forensics!

## Virtual Machines and Memory Captures
- VMware - .vmem file
- Hyper-V - .bin file
- Parallels - .mem file
- VirtualBox - .sav file
- These files can often be found in the datastores of the hypervisors & can be copied without shutting down the virtual machine infrastructure

## psxview
- It's fairly common for malware to attempt to hide itself and the process associated with it. That being said, we can view intentionally hidden processes via the command `psxview`. 

## netscan
- we can also view active network connections at the time of image creation!

## pslist
- processes within our image. 

## ldrmodules
- In addition to viewing hidden processes via psxview, we can also check this with a greater focus via the command 'ldrmodules'. Three columns will appear here in the middle, InLoad, InInit, InMem. If any of these are false, that module has likely been injected which is a really bad thing.

## apihooks
- Processes aren't the only area we're concerned with when we're examining a machine. Using the 'apihooks' command we can view unexpected patches in the standard system DLLs. If we see an instance where Hooking module: <unknown> that's really bad. This command will take a while to run, however, it will show you all of the extraneous code introduced by the malware.

## malfind
- Injected code can be a huge issue and is highly indicative of very very bad things. We can check for this with the command `malfind`. Using the full command `volatility -f MEMORY_FILE.raw --profile=PROFILE malfind -D <Destination Directory>` we can not only find this code, but also dump it to our specified directory. Let's do this now! We'll use this dump later for more analysis. How many files does this generate?

## dlllist
- Last but certainly not least we can view all of the DLLs loaded into memory. DLLs are shared system libraries utilized in system processes. These are commonly subjected to hijacking and other side-loading attacks, making them a key target for forensics. Let's list all of the DLLs in memory now with the command `dlllist`

- Now that we've seen all of the DLLs running in memory, let's go a step further and pull them out! Do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE --pid=PID dlldump -D <Destination Directory>` where the PID is the process ID of the infected process we identified earlier (questions five and six). How many DLLs does this end up pulling?

## dlldump
- Now that we've seen all of the DLLs running in memory, let's go a step further and pull them out! Do this now with the command `volatility -f MEMORY_FILE.raw --profile=PROFILE --pid=PID dlldump -D <Destination Directory>` where the PID is the process ID of the infected process


## References
- AlienVault Open Threat Exchange (OTX) - An open-source threat tracking system. Create pulses based on your malware analysis work and check out the work of others.
  https://otx.alienvault.com/
- Sans Course - https://www.sans.org/blog/for408-windows-forensic-analysis-has-been-renumbered-to-for500-windows-forensics-analysis/
- https://www.youtube.com/watch?v=dB5852eAgpc
- https://github.com/stuxnet999/MemLabs
