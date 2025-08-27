# malicious

### Status : Upsolved

## Category
Digital Forensic

## Solution
I was given a zip file containing three files: `file1.jpg`, `file2.png`, and `file3.pdf`. The challenge description said I needed to assemble the flag parts from these three files. 


**file1.jpg :**
At first, I had no idea what to do with `file1.jpg`, except that there might be an embedded file using `steghide`, but I didn’t know the passphrase.

When I opened `file3.pdf` with Adobe PDF Reader, I noticed an interesting word: `m4ybeyouNeedme`. I assumed this was the `steghide` passphrase for `file1.jpg`.

![Screenshot 2024-09-21 054104](https://github.com/user-attachments/assets/b34937c0-2e99-4c73-a141-899abc9923d9)
![image](https://github.com/user-attachments/assets/0bebe1eb-5622-4d20-aaa8-b6f45cd949b8)

**file2.png :**
I checked `file2.png` using `pngcheck`, and it turned out to be corrupted.

![image](https://github.com/user-attachments/assets/bd7ee6df-10ab-48fb-baba-687ec0764e16)

So I opened it in a hex editor.

![image](https://github.com/user-attachments/assets/122aa69e-f2fa-4f23-8e3a-c37ea21195f5)
![image](https://github.com/user-attachments/assets/e212f53c-95aa-4494-ac82-890a723af2ca)

The header and footer didn’t look right, so I fixed them then checking again with `pngcheck`:

![image](https://github.com/user-attachments/assets/bf2f0f05-eb7e-4925-8522-d89155bb8ed4)

The tool suggested replacing the IHDR chunk, but that didn’t work. Instead, I used a script to brute-force the correct width and height based on the CRC.
```python
from pwn import p32
from zlib import crc32


required_crc = 0x6c20113a
max_dimension = 4000

for width in range(0, max_dimension):
    for height in range(0, max_dimension):
        ihdr = b'\x49\x48\x44\x52' + p32(width, endian='big') + p32(height, endian='big') + b'\x08\x06\x00\x00\x00'
        
        if height % 100 == 0:
            print('ihdr:', ihdr.hex())
        
        crc = crc32(ihdr)
        if crc == required_crc:
            print('FOUND!')
            print(width, height)
            print(hex(width), hex(height))
            exit()
```
reference: [link](https://ctftime.org/writeup/31187)

![image](https://github.com/user-attachments/assets/26378364-9f67-416d-9390-c516e48812da)

I found the correct size and replaced it in the hex editor.

![image](https://github.com/user-attachments/assets/4c380c11-62c3-45a7-868e-a44471739ea1)

Checking again with `pngcheck`:

![image](https://github.com/user-attachments/assets/f2eb6f77-cbb7-4567-901e-fd44b3e4904c)

The PNG still had an error because of an unknown `HDAT` chunk. It should have been `IDAT`, so I fixed it again with the hex editor.

![image](https://github.com/user-attachments/assets/74a3a081-1912-4a0f-b50e-f12c7c7b0016)

Finally, the image was restored:

![file2](https://github.com/user-attachments/assets/7cfe2970-a329-4e11-97b4-0f7ba7225f10)

**file3.pdf :**
When I opened `file3.pdf` in MS Word, I noticed a movable object. Behind it was the first part of the flag.

![Screenshot 2024-09-21 054228](https://github.com/user-attachments/assets/87b9c3df-706d-4282-90e8-9260f2e36efe)

## Flag
TechnoFair11{Welc0m3_4_Gr34t_Hack3rrr_00}
