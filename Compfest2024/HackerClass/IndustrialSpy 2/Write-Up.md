# IndustialSpy 2
## Forensic

They provide a pcapng file traffic.pcapng. I forgot the description of the challenge but the point is to figure out what is an attacker/spy doing in a computer that captured by the pcapng file. Here is the overview of the pcapng file.

![Screenshot from 2024-09-03 00-10-39](https://github.com/user-attachments/assets/91e73699-dccb-42f9-83b9-1d3abdc3c8ae)

I tried to search for USB protocol and I found a website called usb.org. I downloaded a pdf file from document library called hut1_5.pdf and I found something interesting.

![Screenshot from 2024-09-03 00-16-58](https://github.com/user-attachments/assets/a2f9d95f-1621-4464-85f4-ab8f109b86ca)

Starting from the 7th packet, it contain HID Data. There is a hex value (0x06). According to key codes I found before, 0x06 represents “c”. The next packet doesn’t contain HID Data but the next 4 packet does. With this information, I tried to write a script that I used to find out if the characters form a sentence. I also make a dictionary from the key codes.

`from scapy.all import *

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

print(typing)`
