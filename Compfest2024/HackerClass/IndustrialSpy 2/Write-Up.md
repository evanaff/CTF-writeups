# IndustialSpy 2
## Forensic

They provide a pcapng file traffic.pcapng. I forgot the description of the challenge but the point is to figure out what is an attacker/spy doing in a computer that captured by the pcapng file. Here is the overview of the pcapng file.

![Screenshot from 2024-09-03 00-10-39](https://github.com/user-attachments/assets/91e73699-dccb-42f9-83b9-1d3abdc3c8ae)

I tried to search for USB protocol and I found a website called usb.org. I downloaded a pdf file from document library called hut1_5.pdf and I found something interesting.

![Screenshot from 2024-09-03 00-16-58](https://github.com/user-attachments/assets/a2f9d95f-1621-4464-85f4-ab8f109b86ca)
![Screenshot from 2024-09-03 00-20-47](https://github.com/user-attachments/assets/a26ee7e6-2189-46ec-a95f-3d793265f03a)


Starting from the 7th packet, it contain HID Data. There is a hex value (0x06). According to key codes I found before, 0x06 represents “c”. The next packet doesn’t contain HID Data but the next 4 packet does. With this information, I tried to write a script that I used to find out if the characters form a sentence. I also make a dictionary from the key codes.

```python
from scapy.all import *

dictionary = {
    "0x0" : "_",
    "0x1" : "ErrorRollOver1",
    "0x2" : "POSTFail",
    "0x3" : "ErrorUndefined1",
    "0x4" : "a",
    "0x5" : "b",
    "0x6" : "c",
    "0x7" : "d",
    "0x8" : "e",
    "0x9" : "f",
    "0xa" : "g",
    "0xb" : "h",
    "0xc" : "i",
    "0xd" : "j",
    "0xe" : "k",
    "0xf" : "l",
    "0x10" : "m",
    "0x11" : "n",
    "0x12" : "o",
    "0x13" : "p",
    "0x14" : "q",
    "0x15" : "r",
    "0x16" : "s",
    "0x17" : "t",
    "0x18" : "u",
    "0x19" : "v",
    "0x1a" : "w",
    "0x1b" : "x",
    "0x1c" : "y",
    "0x1d" : "z",
    "0x1e" : "1",
    "0x1f" : "2",
    "0x20" : "3",
    "0x21" : "4",
    "0x22" : "5",
    "0x23" : "6",
    "0x24" : "7",
    "0x25" : "8",
    "0x26" : "9",
    "0x27" : "0",
    "0x28" : " [Return] ",
    "0x29" : "ESCAPE",
    "0x2a" : "DELETE",
    "0x2b" : "  ",
    "0x2c" : " ",
    "0x2D" : "-",
    "0x2e" : "=",
    "0x2f" : "[",
    "0x30" : "]",
    "0x31" : "\\",
    "0x32" : "Non-US",
    "0x33" : ";",
    "0x34" : "‘",
    "0x35" : "Grave",
    "0x36" : ",",
    "0x37" : ".",
    "0x38" : "/"
}

packets = rdpcap("traffic.pcapng")

typing = ""

for i in range (6, 649, 4):
    typing += dictionary[f"{hex(packets[i].load[-6])}"]

print(typing)
```

![Screenshot from 2024-09-03 00-32-36](https://github.com/user-attachments/assets/b6e40ab4-5b8f-4f00-b767-321dc2d40fcc)

The output is kinda weird. But there are some words with meaning. “_________16____0__e__m3__s0me______f0rens1_____fd746ec8b3__” looks like a flag. There are so many _ that are represented by 0x0 (reserved). Then I remember that the flag format is COMPFEST16{…}. I realized that caps letters are not detected by the script.

Some HID data have different positions of key codes. That caused the script can’t detect it. 2 packet after it is a packet with HID data with the same posistions of codes but have 0x02 value at the beginning.

![Screenshot from 2024-09-03 00-42-19](https://github.com/user-attachments/assets/23a88f4a-37b4-4a39-84e8-e83829f4ffe4)
![Screenshot from 2024-09-03 00-46-32](https://github.com/user-attachments/assets/8a3df32f-8142-4e77-970c-34dd7d663b59)

I assumed 0x02 represents caps for key codes. From that information, I modified the script. I added a second dictionary to represent caps letters.

```python
from scapy.all import *

dictionary = {
    "0x0" : "_",
    "0x1" : "ErrorRollOver1",
    "0x2" : "POSTFail",
    "0x3" : "ErrorUndefined1",
    "0x4" : "a",
    "0x5" : "b",
    "0x6" : "c",
    "0x7" : "d",
    "0x8" : "e",
    "0x9" : "f",
    "0xa" : "g",
    "0xb" : "h",
    "0xc" : "i",
    "0xd" : "j",
    "0xe" : "k",
    "0xf" : "l",
    "0x10" : "m",
    "0x11" : "n",
    "0x12" : "o",
    "0x13" : "p",
    "0x14" : "q",
    "0x15" : "r",
    "0x16" : "s",
    "0x17" : "t",
    "0x18" : "u",
    "0x19" : "v",
    "0x1a" : "w",
    "0x1b" : "x",
    "0x1c" : "y",
    "0x1d" : "z",
    "0x1e" : "1",
    "0x1f" : "2",
    "0x20" : "3",
    "0x21" : "4",
    "0x22" : "5",
    "0x23" : "6",
    "0x24" : "7",
    "0x25" : "8",
    "0x26" : "9",
    "0x27" : "0",
    "0x28" : " [Return] ",
    "0x29" : "ESCAPE",
    "0x2a" : "DELETE",
    "0x2b" : "  ",
    "0x2c" : " ",
    "0x2D" : "-",
    "0x2e" : "=",
    "0x2f" : "[",
    "0x30" : "]",
    "0x31" : "\\",
    "0x32" : "Non-US",
    "0x33" : ";",
    "0x34" : "‘",
    "0x35" : "Grave",
    "0x36" : ",",
    "0x37" : ".",
    "0x38" : "/"
}

dictionary2 = {
    "0x0" : "",
    "0x1" : "ErrorRollOver1",
    "0x2" : "POSTFail",
    "0x3" : "ErrorUndefined1",
    "0x4" : "A",
    "0x5" : "B",
    "0x6" : "C",
    "0x7" : "D",
    "0x8" : "E",
    "0x9" : "F",
    "0xa" : "G",
    "0xb" : "H",
    "0xc" : "I",
    "0xd" : "J",
    "0xe" : "K",
    "0xf" : "L",
    "0x10" : "M",
    "0x11" : "N",
    "0x12" : "O",
    "0x13" : "P",
    "0x14" : "Q",
    "0x15" : "R",
    "0x16" : "S",
    "0x17" : "T",
    "0x18" : "U",
    "0x19" : "v",
    "0x1a" : "2",
    "0x1b" : "X",
    "0x1c" : "Y",
    "0x1d" : "Z",
    "0x1e" : "!",
    "0x1f" : "@",
    "0x20" : "#",
    "0x21" : "$",
    "0x22" : "%",
    "0x23" : "∧",
    "0x24" : "&",
    "0x25" : "*",
    "0x26" : "(",
    "0x27" : ")",
    "0x28" : "Return",
    "0x29" : "ESCaPE",
    "0x2a" : "DELETE",
    "0x2b" : "Tab",
    "0x2c" : "Spacebar",
    "0x2d" : "_",
    "0x2e" : "+",
    "0x2f" : "{",
    "0x30" : "}",
    "0x31" : "\\",
    "0x32" : "^5",
    "0x33" : ":",
    "0x34" : "“",
    "0x35" : "",
    "0x36" : "<",
    "0x37" : ">",
    "0x38" : "?"
}

packets = rdpcap("traffic.pcapng")

typing = ""

for i in range (6, 649, 4):
    if hex(packets[i].load[-8]) == '0x2':
        typing += dictionary2[f"{hex(packets[i+2].load[-6])}"]
    else:
        typing += dictionary[f"{hex(packets[i].load[-6])}"]

print(typing)
```

![Screenshot from 2024-09-03 01-11-09](https://github.com/user-attachments/assets/a29f495f-5228-4d8f-b6ab-94ef6eb1342b)

Here is the flag : 
COMPFEST16{L0ve_m3_s0me_USB_f0rens1CS_fd746ec8b3}

And I think this is an interesting YouTube link :3 
[youtube.com/watch?v=p7YXXieghto ](https://youtube.com/watch?v=p7YXXieghto )


