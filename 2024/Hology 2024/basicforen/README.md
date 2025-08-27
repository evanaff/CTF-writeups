# basicforen

### Status : Upsolved

## Category
Digital Forensic

## Solution
The archive contains two files (`part1.7z` and `part3.jpg`). I assumed the flag consisted of three parts, with `part2` hidden somewhere.

**Part 1 :** 

`part1.7z` could not be extracted because of an error. After examining the hex values in a `hex editor`, I noticed something interesting:

![image](https://github.com/user-attachments/assets/d7740cfc-00e8-4c33-b67a-aeb154ecf5c6)

The file signature suggested it was not actually a `7z` file. Strings like `sRGB` and `IDAT` are typically found in `PNG` files. I fixed the file signature using this reference: [https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73](https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73).

![image](https://github.com/user-attachments/assets/75d99533-ff05-4589-ad41-338cca58b4fa)

The repaired part1.png showed a barcode. I extracted it using zbarimg, which revealed a link: 
```
QR-Code:https://pastebin.com/4XD0gPdF
```

That link contains a string that looks like encoded.
```
BFDREB5M4aXWvmXmnyXd2jxne8st28SDU
```

I discovered it was base58 encoded, which revealed the first part of the flag:

part 1 : `HOLOGY7{s1Mpl3_`

**Part 2 :**

I suspected the second part was hidden inside `part1.png`. Looking deeper:

![image](https://github.com/user-attachments/assets/73511501-ea56-4931-bfec-f512b9d5daf9)

![image](https://github.com/user-attachments/assets/8145aec5-3d14-4b6e-b2fb-31303554c10a)

I found another `PNG` embedded inside the file. I extracted it using `CyberChef`:

![part2](https://github.com/user-attachments/assets/00863c60-a56e-4f7c-9fd0-5d4abcb22963)

I analyzed it with stegsolve. That revealed the second part of the flag:

![image](https://github.com/user-attachments/assets/679c3dcf-ca2d-4ae0-9a63-56165b266052)

part 2 : `3nG3_no?}`

**Part 3 :** 

For the last part, I turned to `part3.jpg`. Since steganography with steghide is common, I attempted a brute-force attack with` rockyou.txt`.

Here’s the script I used:
```python
import subprocess
import sys
import os

def brute_force_steghide(file_path, wordlist_path, output_file="extracted.txt"):
    with open(wordlist_path, 'r', encoding='utf-8') as wordlist:
        for line in wordlist:
            password = line.strip()
            print(f"[*] Mencoba password: {password}")

            # Buat perintah steghide
            command = [
                "steghide", "extract",
                "-sf", file_path,
                "-p", password,
                "-xf", output_file
            ]

            try:
                result = subprocess.run(
                    command,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                if result.returncode == 0:
                    print(f"[+] Password ditemukan: {password}")
                    print(f"[+] Data disimpan di: {output_file}")
                    return
            except Exception as e:
                print(f"[-] Error saat menjalankan steghide: {e}")

    print("[-] Password tidak ditemukan di wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bruteforce_steghide.py <stego_file> <wordlist_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    wordlist_path = sys.argv[2]

    brute_force_steghide(file_path, wordlist_path)
```

![image](https://github.com/user-attachments/assets/23aa68f9-5ebc-4fd8-8ee3-7081e7469a83)

part 3 : `cL4Ss1C_cH4LL`

## Flag
HOLOGY7{s1Mpl3_cL4Ss1C_cH4LL3nG3_no?}
