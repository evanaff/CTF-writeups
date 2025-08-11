# forcry
## Hacktoday 2025

The challenge description mentioned that the PNG was encrypted and the pattern looked repetitive. So I checked the hexdump and noticed a pattern.

![alt text](image.png)

Signature of PNG is `89 50 4E 47`. I found that the encryption substracted the first 4 bytes by `0x04`. However the next 4 bytes was correct. Then the next 4 bytes were incorrect again with the same change as the first 4 bytes followed by another 4 correct bytes again.

Based on this repeating pattern, I wrote a python script to decrypt the PNG file:

```python
#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("Usage: python fix_png.py <input_file> <output_file>")
    sys.exit(1)

inp = sys.argv[1]
out = sys.argv[2]

with open(inp, "rb") as f:
    data = bytearray(f.read())

for i in range(len(data)):
    block = (i // 4)
    if (block % 2) == 0:
        data[i] = (data[i] + 4) & 0xFF

with open(out, "wb") as f:
    f.write(data)

print(f"Written fixed file to {out}")
```

![alt text](fixed.png)

## Flag
hacktoday{wh3n_y0u_sh1ft_3very_f0ur_byte5_l3ft_4nd_sk1p_th3_n3xt_f0ur_thin9s_bre4k}
