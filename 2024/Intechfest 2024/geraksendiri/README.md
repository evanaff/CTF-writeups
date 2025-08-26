# geraksendiri

### Status : Solved

## Category
Digital Forensic

## Solve
There pcapng file, so i open it using wireshark. 

![image](https://github.com/user-attachments/assets/d99c0b96-bffb-4031-8075-619800a0e7d2)

After some searching I know that the pcap file contains record of bluetooth keyboard key that pressed by someone. I need created a script to parse all keyboard key that pressed from the pcap file. But before that I need to know hex representative of each keycode value. After some searching I found this [https://usb.org/sites/default/files/documents/hut1_12v2.pdf](https://usb.org/sites/default/files/documents/hut1_12v2.pdf).

![image](https://github.com/user-attachments/assets/d30fc8fb-9e17-4b99-b2a3-2f43009a7c4b)

So I used it to create a dictionary. hex value can be obtained from `usbhid.boot_report.keyboard.keycode_1` value of bthid layer packet. I also need detect if left shift key pressed by accessing hex value from `usbhid.boot_report.keyboard.modifier.left_shift`.

parser.py :

```python
hid_key_map = {
    '04': 'a', '05': 'b', '06': 'c', '07': 'd', '08': 'e', '09': 'f',
    '0a': 'g', '0b': 'h', '0c': 'i', '0d': 'j', '0e': 'k', '0f': 'l',
    '10': 'm', '11': 'n', '12': 'o', '13': 'p', '14': 'q', '15': 'r',
    '16': 's', '17': 't', '18': 'u', '19': 'v', '1a': 'w', '1b': 'x',
    '1c': 'y', '1d': 'z',
    '1e': '1', '1f': '2', '20': '3', '21': '4', '22': '5', '23': '6',
    '24': '7', '25': '8', '26': '9', '27': '0',
    '28': '\n', '2c': ' ', '2d': '-', '2e': '=', '2f': '[', '30': ']',
    '31': '\\', '33': ';', '34': "'", '35': '`', '36': ',', '37': '.',
    '38': '/', '39': 'CapsLock', '00': ' '
}

hid_key_map_shift = {
    '04': 'A', '05': 'B', '06': 'C', '07': 'D', '08': 'E', '09': 'F',
    '0a': 'G', '0b': 'H', '0c': 'I', '0d': 'J', '0e': 'K', '0f': 'L',
    '10': 'M', '11': 'N', '12': 'O', '13': 'P', '14': 'Q', '15': 'R',
    '16': 'S', '17': 'T', '18': 'U', '19': 'V', '1a': 'W', '1b': 'X',
    '1c': 'Y', '1d': 'Z',
    '1e': '!', '1f': '@', '20': '#', '21': '$', '22': '%', '23': '^',
    '24': '&', '25': '*', '26': '(', '27': ')',
    '28': '\n', '2c': ' ', '2d': '_', '2e': '+', '2f': '{', '30': '}',
    '31': '|', '33': ':', '34': '"', '35': '~', '36': '<', '37': '>',
    '38': '?', '39': 'CapsLock', '00': ' '
}

import pyshark

cap = pyshark.FileCapture("chall.pcapng", display_filter="bthid")

typed = []

for pkt in cap:
    try:
        bthid_layer = pkt.bthid
        left_shift = bthid_layer.get('usbhid.boot_report.keyboard.modifier.left_shift')
        keycode = bthid_layer.get('usbhid.boot_report.keyboard.keycode_1')
        
        if keycode and keycode != '0x00':
            code = keycode[2:].lower()
            
            if left_shift == 'True':
                char = hid_key_map_shift.get(code)
            else:
                char = hid_key_map.get(code)

            if char:
                typed.append(char)

    except AttributeError:
        continue

print("Typed output:")
print(''.join(typed))

```

Result :

![image](https://github.com/user-attachments/assets/394dc02f-ede4-45d7-9da5-6f2c335205ec)

There is a link, but when I write this write-up the endpoint cannot be accessed. As far as I remember, that link contains a zip file and video. The zip file needed password to extract. The video show us when someone type the password on computer. The password is the same word as first word in the output `l33t1337dbNl`. The zip file contains flag.
