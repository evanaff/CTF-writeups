# basicforen
## Hology CTF 2024

7z contains 2 file (part1.7z & part3.jpg). So I assummed that the flag consist of 3 parts with part2 somewhere.

Part 1 : 

`part1.7z` can't be extracted because of an error. Then I found something interesting when examining the hex value of `part1.7z` using hexeditor.

![image](https://github.com/user-attachments/assets/d7740cfc-00e8-4c33-b67a-aeb154ecf5c6)

It looks like the real format of file is not 7z. sRGB and IDAT are usually found in PNG file. So I fix the signature of file using this references [https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73](https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73).

![image](https://github.com/user-attachments/assets/75d99533-ff05-4589-ad41-338cca58b4fa)

The result of fixed `part1.png` is a barcode. I extract the barcode using zbarimg tools and the result is a link. `QR-Code:https://pastebin.com/4XD0gPdF`

That link contains a string that looks like encoded. `BFDREB5M4aXWvmXmnyXd2jxne8st28SDU`

After some try, I found that the string is encoded using base58 method and contains first part of the flag.

``part 1 : HOLOGY7{s1Mpl3_``

Part 2 :

Where is the second part? I tried to analyze part1.png again.

![image](https://github.com/user-attachments/assets/73511501-ea56-4931-bfec-f512b9d5daf9)

![image](https://github.com/user-attachments/assets/8145aec5-3d14-4b6e-b2fb-31303554c10a)

Then I found there is another png file in part1.png. So I extracted it using cyberchef.

![part2](https://github.com/user-attachments/assets/00863c60-a56e-4f7c-9fd0-5d4abcb22963)

There is something weird about the pixels of image. I tried to analyzed it using stegsolve. Then I found the second part.

![image](https://github.com/user-attachments/assets/679c3dcf-ca2d-4ae0-9a63-56165b266052)

``part 2 : 3nG3_no?}``

Part 3 : 

I don't have any hint about third part. But part3.jpg is a jpg format image. There is common steganography method called steghide. So I have an idea to bruteforce steghide password using rockyou.txt.

steghideBruteforce.py :

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

``part 3 : cL4Ss1C_cH4LL``

### Flag : part 1 : HOLOGY7{s1Mpl3_cL4Ss1C_cH4LL3nG3_no?}
