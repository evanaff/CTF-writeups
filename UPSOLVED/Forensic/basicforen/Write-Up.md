# basicforen
## Hology CTF 2024

7z contains 2 file (part1.7z & part3.jpg). So I assummed that the flag consist of 3 parts with part2 somewhere.

Part 1 : 

`part1.7z` can't be extracted because of an error. Then I found something interesting when examining the hex value of `part1.7z` using hexeditor.

![image](https://github.com/user-attachments/assets/d7740cfc-00e8-4c33-b67a-aeb154ecf5c6)

It looks like the real format of file is not 7z. sRGB and IDAT are usually found in PNG file. So I fix the signature of file using this references [https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73](https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73).

![image](https://github.com/user-attachments/assets/75d99533-ff05-4589-ad41-338cca58b4fa)

The result of fixed `part1.png` is a barcode. I extract the barcode using zbarimg tools and the result is a link. `QR-Code:https://pastebin.com/4XD0gPdF`

That link contains a string that looks like encoded. `BFDREB5M4aXWvmXmnyXd2jxne8st28SDU`

After some try, I found that the string is encoded using base58 method and contains first part of the flag.

``part 1 : HOLOGY7{s1Mpl3_``

Part 2 :

Where is the second part? I try to analyze part1.png again.

![image](https://github.com/user-attachments/assets/73511501-ea56-4931-bfec-f512b9d5daf9)

![image](https://github.com/user-attachments/assets/8145aec5-3d14-4b6e-b2fb-31303554c10a)

Then I found there is another png file in part1.png. So I extracted it using cyberchef.

![part2](https://github.com/user-attachments/assets/00863c60-a56e-4f7c-9fd0-5d4abcb22963)

There is something weird about the pixels of image. I tried to analyzed it using stegsolve. Then I found the second part.

![image](https://github.com/user-attachments/assets/52d0c126-2a57-4398-989f-5ef969c8e42b)

``part 2 : 3nG3

Part 3 : 



### Flag
