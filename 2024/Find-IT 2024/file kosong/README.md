# File Kosong

### Status : Upsolved

## Category
Digital Forensic

## Solution
The challenge provided a file named flag.txt, but its content appeared empty. I opened the file in a hex editor and found something unusual.

![image](https://github.com/user-attachments/assets/d9398790-8dba-4b36-9d5b-8954053ab7da)

There were multiple space characters `0x20`. I was searching for similar challenge on internet and the idea was to treat each space character as `1` and every other character as `0`, effectively creating a binary sequence. Then, by converting the binary into ASCII characters, the flag could be revealed. This can be done using either a Python script or CyberChef.

```python
with open("flag.txt", 'r') as file:
    data = file.read()

binary = ''

for char in data:
    binary += '1' if char == ' ' else '0'

flag = ''

for i in range(0, len(binary), 8):
    flag += chr(int(binary[i:(i+8)], 2))

print(flag)   
```

## Flag
FindITCTF{K0K_F1l3ny4_K050ng_s1H?_f73ghyg478}
