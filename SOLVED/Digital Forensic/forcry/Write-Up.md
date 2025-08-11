# forcry
## Hacktoday 2025

The challenge description mentioned that the PNG was encrypted and the pattern looked repetitive. So I checked the hexdump and noticed a pattern.

<img width="644" height="129" alt="Screenshot From 2025-08-11 23-48-56" src="https://github.com/user-attachments/assets/ed2e8fb5-b657-4a0f-8998-adb164b36ae2" />

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

<img width="618" height="499" alt="fixed" src="https://github.com/user-attachments/assets/047c7229-d778-433e-b1c7-98d7cf9d1e13" />

## Flag
hacktoday{wh3n_y0u_sh1ft_3very_f0ur_byte5_l3ft_4nd_sk1p_th3_n3xt_f0ur_thin9s_bre4k}
