# baby-structured
## Forensics - solved

There is just 1 file named zhezhi_______.

![image](https://github.com/user-attachments/assets/c05bb0b3-89bd-4a69-a31a-f62458aca384)

We know that the file is png image but its corrupt so I rename it and checked with pngcheck.

![image](https://github.com/user-attachments/assets/6202a9f6-b07e-4a89-ab4d-c461d398a208)

There is CRC error in IHDR chunk so I change the expected chunk with computed chunk using hexeditor.

![image](https://github.com/user-attachments/assets/3df641ed-440c-4123-99f2-9f90440c122c)

![zhezhi_______](https://github.com/user-attachments/assets/cb99a89c-6fa7-44bd-a2c0-088129030200)

There is nothing I can rely on from the result.

![image](https://github.com/user-attachments/assets/f522ef9b-7334-4d8f-bf10-e117de5bff76)

When I checked it again it says that the image is 49,6% of what it would be. Maybe the problem is about size. So i return the chunk and check the actual size with script from [https://ctftime.org/writeup/31187](https://ctftime.org/writeup/31187)

```python
from pwn import p32
from zlib import crc32


required_crc = 0xa5ae0f88
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

![image](https://github.com/user-attachments/assets/e29b24b6-28e9-4756-94f6-ab5c55169a85)

![image](https://github.com/user-attachments/assets/3e4d0ec6-3052-4517-b797-90c0dd78590f)

![zhezhi_______](https://github.com/user-attachments/assets/deccd0d5-0a17-4d43-bc0b-97331feb1a53)

### Flag : gemastik{g0t_cr0pped_by_structur3}
