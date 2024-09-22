# malicious
## Forensics - unsolved

They gave me a zip contain 3 files (file1.jpg, file2.png, file3.pdf). The description said that we must assemble flag parts from that 3 files. 


file1.jpg :

I have no idea with file1.jpg unless there is a probability of embedded file on file1.jpg using steghide but I don't have the passphrase.

This is what happen when I open file3.pdf using adobe pdf reader

![Screenshot 2024-09-21 054104](https://github.com/user-attachments/assets/b34937c0-2e99-4c73-a141-899abc9923d9)

There is interesting word "m4ybeyouNeedme" so I assume that as steghide passphrase on file1.jpg

![image](https://github.com/user-attachments/assets/0bebe1eb-5622-4d20-aaa8-b6f45cd949b8)

Yup my assumption is correct and its contain the last part of the flag.


file2.png :

I checked file2.png using pngcheck and its looks like the png file is corrupt.

![image](https://github.com/user-attachments/assets/bd7ee6df-10ab-48fb-baba-687ec0764e16)

So I checked the bytes using hexeditor.

![image](https://github.com/user-attachments/assets/122aa69e-f2fa-4f23-8e3a-c37ea21195f5)
![image](https://github.com/user-attachments/assets/e212f53c-95aa-4494-ac82-890a723af2ca)

The header and tail is doesn't sem right so I fixed it (reference : [link](https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73)

Then I checked it again using pngcheck

![image](https://github.com/user-attachments/assets/bf2f0f05-eb7e-4925-8522-d89155bb8ed4)

I tried to replace the IHDR chunk as pngcheck result said but it doesn't works. So I used a script to resize the image according the IHDR chunk.

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
reference : [link](https://ctftime.org/writeup/31187)

![image](https://github.com/user-attachments/assets/26378364-9f67-416d-9390-c516e48812da)

The result is found, so I replace size of image from bytes using hexeditor.

![image](https://github.com/user-attachments/assets/4c380c11-62c3-45a7-868e-a44471739ea1)

Then I checked it again using pngcheck.

![image](https://github.com/user-attachments/assets/f2eb6f77-cbb7-4567-901e-fd44b3e4904c)

The png still error because of unkown "HDAT" chunk, it should be "IDAT" so I fixed it again using hexeditor

![image](https://github.com/user-attachments/assets/74a3a081-1912-4a0f-b50e-f12c7c7b0016)

Here is the result

![file2](https://github.com/user-attachments/assets/7cfe2970-a329-4e11-97b4-0f7ba7225f10)


file3.pdf :

I tried to open this file using ms word and there is a moveable object. There is something behind it.

![Screenshot 2024-09-21 054228](https://github.com/user-attachments/assets/87b9c3df-706d-4282-90e8-9260f2e36efe)

Thats looks like the first part of the flag. So The flag parts now is complete.

### Flag : TechnoFair11{Welc0m3_4_Gr34t_Hack3rrr_00}}
