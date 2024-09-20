# Write Up Challenge
## Forensics - Solved

There is a jpg file with no further information. So i check it with some comment.

![image](https://github.com/user-attachments/assets/a72d4c12-fa01-45ac-98bf-54adfb050769)

![image](https://github.com/user-attachments/assets/f37e81ca-fb3e-4e11-8a1f-9870f13d8b3d)

![image](https://github.com/user-attachments/assets/971987ba-c7ba-4976-9d4b-927bb8e9f3fe)

We can know that there is something in this file according to binwalk result. I assume that file is using steghide to embed a secret but i don't have the passphrase. But when I checked the strings of file I can see there is a base64 encoded like strings. So I tried to decode it.

![image](https://github.com/user-attachments/assets/7953c7e3-fe00-49b2-991e-e22c002c99d2)

The result is `menyala` and I used it as passphrase. 

![image](https://github.com/user-attachments/assets/11d74308-f805-453c-83ce-de3a9fbecb2d)

### Flag : TechnoFair11{Ez_Pz_L3m0n_SqU3Zy}
