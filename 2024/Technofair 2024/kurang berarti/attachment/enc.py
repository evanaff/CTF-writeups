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