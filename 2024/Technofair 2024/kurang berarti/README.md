# kurang berarti

### Status : Solved

## Category
Digital Forensic

## Solve
We got a jpg file (chall.jpg) and a python script (enc.py)

enc.py :

```python
def insert_plaintext_into_image(input_file, output_file, plaintext,
offset):
    with open(input_file, 'rb') as file:
        file_bytes = bytearray(file.read())

    plaintext_binary = ''.join(format(ord(char), '08b') for char in
    plaintext)

    plaintext_index = 0
    plaintext_length = len(plaintext_binary)
    for i in range(offset, len(file_bytes)):
        if plaintext_index < plaintext_length:
            original_byte = file_bytes[i]

            plaintext_bit = int(plaintext_binary[plaintext_index])

            new_byte = (original_byte & 0xFE) | plaintext_bit

            file_bytes[i] = new_byte

            plaintext_index += 1
        else:
            break

    with open(output_file, 'wb') as file:
        file.write(file_bytes)
        
    print(f"{output_file}")

input_file = ''
output_file = 'chall.jpg'
plaintext = "flag"
offset = 0x00000D00
insert_plaintext_into_image(input_file, output_file, plaintext, offset)
```

this codes is a script that used for inserting a plaintext to image bytes starting from determined offset. The step is :
1. read image bytes
2. convert plaintext to binary
3. starting from offset, convert the bytes with operation (new_byte = (original_byte & 0xFE) | plaintext_bit)

We can retrieve the plaintext bit from operation. xor the new_byte with 1, if the result < new_byte so the plaintext bit is 1 and vice versa. So I create a script to retrieve plaintext from chall.jpg.

```python
def decode(input_file, offset):
    with open(input_file, 'rb') as file:
        file_bytes = bytearray(file.read())
    
    plaintext_binary = ''
    plaintext = ''

    for i in range(offset, len(file_bytes)):
    
        enc_byte = file_bytes[i]

        original_byte = enc_byte ^ 1

        if original_byte < enc_byte:
            plaintext_binary += '1'
        else:
            plaintext_binary += '0'

    for i in range(0, 800, 8):
        char_binary = plaintext_binary[i:i+8]
        plaintext += chr(int(char_binary, 2))
    
    print(plaintext)

input_file = 'chall.jpg'
offset = 0x00000D00
decode(input_file, offset)
```

![image](https://github.com/user-attachments/assets/f1abd068-9cdc-495c-8082-5a936571e32f)

### Flag : TechnoFair11{patenkalikaubang}
