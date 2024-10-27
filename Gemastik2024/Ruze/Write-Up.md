## Unsolved

The format of given file is AD1 so we need to check it with FTK Imager.

![image](https://github.com/user-attachments/assets/2106c011-7c08-4a26-83fa-5607aa1864de)

There is non-default user **sand-4ECC834FCF** so I tried to analyze it.
In description '.. when he installs something suddenly his device reboots and his files suddenly disappear .. ', we can assume the ransomware need to reboot/login for got executed. In windows you can set what device will do everytime user got login in Registry Key. 

I used Registry Explorer tool to check on registry HCKU:SOFTWARE\Microsoft\Windows\CurrentVersion\Run for malicious entry via NTUSER.DAT

![image](https://github.com/user-attachments/assets/6c1ba36e-b037-41ca-b6dc-cfc2b13853db)

We can know that there is file named **console.bat** was executed. The content of that file is encoded powershell code.

![image](https://github.com/user-attachments/assets/ffd3caf0-fc14-454c-b14d-28582ce9bf3c)

I used powerdecode tool to decode and deobfuscate it and this is the result.

poweshell

