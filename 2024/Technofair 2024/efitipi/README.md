# eftipi

### Status : Upsolved

## Category
Digital Forensic

## Solve
They give me a pcapng file (chall.pcapng). I tried analyze it using wireshark. Here is what I found when following tcp stream.

![image](https://github.com/user-attachments/assets/e8e02ff7-8633-4405-befd-5e23bc604a35)

From that we know that there is some file is stored (secret.txt.lst, secret2.png, secret3.zip) so I export it.

secret.txt.lst looks like wordlist that can be used for bruteforcing pass. secret2.png is regular png file contain :

![secret2](https://github.com/user-attachments/assets/989a3235-843e-4e65-9f4d-7cb721c063a3)

secret3.zip is encrypted zip file using AES method.

![image](https://github.com/user-attachments/assets/fc641f92-2a1e-4ee6-964b-aec869a79ab2)

First idea comes to my mind is to brute forcing zip file password using the wordlist. So I make this script :

```python
import pyzipper

def try_password(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        print(f"Password Found : {password}")
        return True
    except:
        return False
    
def dict_attack(zip_filename, wordlist):
    with pyzipper.AESZipFile(zip_filename) as zip_file:
        with open(wordlist, 'r', errors='ignore') as wordlist:
            for password in wordlist:
                password = password.strip()
                if try_password(zip_file, password):
                    return password
    print("Password not found")

dict_attack('secret3.zip', 'secret.txt.lst')
```

![image](https://github.com/user-attachments/assets/024c7221-3062-420b-98fe-efde45ff5ae6)

The content of zip is a file named flag then I checked it using hexeditor.

![image](https://github.com/user-attachments/assets/89ed9152-a0ff-43b4-8263-d1649cf13f2c)

in the beginning of file there is word "DNEI". If we reverse it becomes "IEND" which is the end strings of png file. So I reverse it using [cyberchef](https://gchq.github.io/CyberChef/)

![image](https://github.com/user-attachments/assets/cdcbf751-a0ef-4696-b8f8-e3eb2e4d3de8)

Here is the result

<img width="802" alt="flag" src="https://github.com/user-attachments/assets/990673b0-b06e-4e4f-842f-9683b8f371dd">

### Flag : TechnoFair11{B3_c4R3FuLL_w1tH_sN1ff3r}

