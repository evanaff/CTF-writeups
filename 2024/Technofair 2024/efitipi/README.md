# eftipi

### Status : Upsolved

## Category
Digital Forensic

## Solution
I was given a `.pcapng` file (`chall.pcapng`). I opened it in `Wireshark` and followed the `TCP stream`.

![image](https://github.com/user-attachments/assets/e8e02ff7-8633-4405-befd-5e23bc604a35)

From the stream, I discovered references to files: `secret.txt.lst`, `secret2.png`, and `secret3.zip`. I exported them for further analysis.

- `secret.txt.lst` → looked like a `wordlist`, possibly for brute-forcing.
- `secret2.png` → a normal `PNG` file containing the following image:
- `secret3.zip` → an encrypted `ZIP` file using AES.

![secret2](https://github.com/user-attachments/assets/989a3235-843e-4e65-9f4d-7cb721c063a3)

![image](https://github.com/user-attachments/assets/fc641f92-2a1e-4ee6-964b-aec869a79ab2)

My first idea was to try `brute-forcing` the ZIP password with the provided `wordlist`. I wrote the following script:
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

The extracted content was a file named `flag`. Opening it in a `hex editor` revealed the string `DNEI` at the start. Reversing this gives `IEND`, which is the `PNG` end marker. This suggested the file was **reversed**.

![image](https://github.com/user-attachments/assets/89ed9152-a0ff-43b4-8263-d1649cf13f2c)

I used [cyberchef](https://gchq.github.io/CyberChef/) to reverse the file.

![image](https://github.com/user-attachments/assets/cdcbf751-a0ef-4696-b8f8-e3eb2e4d3de8)

Here’s the recovered `flag` image:

<img width="802" alt="flag" src="https://github.com/user-attachments/assets/990673b0-b06e-4e4f-842f-9683b8f371dd">

## Flag
TechnoFair11{B3_c4R3FuLL_w1tH_sN1ff3r}

