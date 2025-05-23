# Image Cropper
## FindIT CTF 2024

Alice found a python script that in its documentation promises to make it easy to crop images to a 1:1 ratio. However, Alice was scammed by that script, which actually removed the input image she inserted and transformed it into another file. Meanwhile, the image holds something important for her. Can you help Alice get that important thing back?

There is wav file (encoded.wav) and a python source code. From the challenge description we now that the file is used for cropping image to 1:1 ratio. Let's try to understand how it works.
1. convert image file to RGB mode
2. crop image to 1:1 ratio
3. there is input text in binary form
4. the input text is inserted to RBG value of image
5. the cropped image with inserted text then converted to wav
   
with tha information we can convert it back to image and extract the inserted text. This is the solver i used 

```python
import numpy as np
import scipy.io.wavfile as wavfile
import math
from PIL import Image
import base64
from Cryptodome.Util.number import long_to_bytes

data = wavfile.read("encoded.wav")[1]

red, green, blue = data[::3], data[1::3], data[2::3]

def rescale_channel(channel):
    return np.round((channel + 1)/2 * 255).astype(np.uint8)

red, green, blue = map(rescale_channel, [red, green, blue])

def reshape_channel(channel):
    length = int(math.sqrt(channel.shape[0]))
    return np.reshape(channel, (length, length))

red, green, blue = map(reshape_channel, [red, green, blue])

pixels = np.dstack([red, green, blue])
image = Image.fromarray(pixels)
pixels = list(image.getdata())

data = ''

for red, green, blue in pixels:
    data += '0' if red % 2 == 0 else '1'
    data += '0' if green % 2 == 0 else '1'
    data += '0' if blue % 4 < 2 else '1'

binary_length = int(data[:16], 2)
binary_text = data[16:16 + binary_length]

print(base64.b64decode(long_to_bytes(int(binary_text, 2)).decode()).decode())
```

the inserted text looks like a base64 encoded strings so I decoded it and found the flag.

### Flag : FindITCTF{d0nt_t12ust_l1b!!_ch3ck_th3_s0urce_c0d3_1ma0_44928}
