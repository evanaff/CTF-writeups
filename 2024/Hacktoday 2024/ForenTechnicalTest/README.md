# Foren Technical Test

### Status : Upsolved

## Category
Forensics

## Description
Supaya kalian semua tetap dalam jalan yang benar probset yg baik ini memberikan kalian objektif soal. moga bermanfaat :)
 
Objective:
 
1.disk image adalah hasil export dari drive C sebuah folder
2.membuka file archive yang ber password
3.password disimpan oleh probset di computer lain
4.flag terdapat pada file yg ada di dalam archive
 
Pass :
1525c14e72decafd007be7af71194c7cf0354

[chall.zip](https://drive.google.com/file/d/1z03F9_CNWDHvvi0gMP0qmScGShRlT7lT/view?usp=sharing)

## Solution
The given file was an `AD1 image`, so I opened it using `FTK Imager`. Inside, I noticed a non-default user account named `ayaya`, so I extracted its contents.

![Screenshot 2024-11-05 022221](https://github.com/user-attachments/assets/ffbd4d40-dbe4-41d7-878e-ca2461de65a9)

I found `Secret-file.zip`, which required a password.

![image](https://github.com/user-attachments/assets/0eeedf84-9403-4929-bd8a-48b54d2e5874)

From the description, I knew the password was stored on another computer. I also found a `Remote Desktop Connection (.rdp)` file.

![Screenshot 2024-11-05 022344](https://github.com/user-attachments/assets/27f55f7f-f5e2-40ff-ae60-10b9290f5532)

Inside `\AppData\Local\Microsoft\Terminal Server Client\Cache`, I located the RDP cache files.

![Screenshot 2024-11-05 022614](https://github.com/user-attachments/assets/3038bc6b-84b5-4326-b34d-a79f39162ad5)

I used [bmc-tools.py](https://github.com/ANSSI-FR/bmc-tools) to parse the cache into several BMP images.

![Screenshot 2024-11-05 023221](https://github.com/user-attachments/assets/df41bc4f-ef43-448c-8fc5-d8cafd8e9afa)

From the parsed images, I was able to recover the password for `Secret-file.zip`:
```
Key = Selamat_ngerjain_hacktoday_yaaa
```
After extracting, the file turned out to be a `.docm` (macro-enabled Word document). I analyzed it using [olevba](https://github.com/decalage2/oletools).

![image](https://github.com/user-attachments/assets/8dcbf375-f333-4a0d-b487-be8141dbd575)

The macros revealed that the flag was split into three parts. By concatenating part1, part2, and part3, I obtained the final flag.

## Flag
hacktoday{jangan_lupa_disubmit_flagnya}






