# File Kosong
## Forensics - unsolved

The `flag.txt` was provided but the content is empty. I check the file with hexedior and this is what I found.

![image](https://github.com/user-attachments/assets/d9398790-8dba-4b36-9d5b-8954053ab7da)

There some space character (\x20). Let's try to convert space character to 1 and the others to 0 (binary). Then convert it to ascii characters. We can use python script or cyberchef

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

### Flag : FindITCTF{K0K_F1l3ny4_K050ng_s1H?_f73ghyg478}
