# DUMPling

### Status : Upsolved

## Category
Digital Forensic

## Solution
The challenge provided a `chall.raw` file, which turned out to be a `Windows memory dump`. I analyzed it using [volatility3](https://github.com/volatilityfoundation/volatility3)

![image](https://github.com/user-attachments/assets/14e2b0d8-da6d-4cea-ab67-d05a321fed3f)

From the scan results, I noticed an interesting clue called `clue.txt` and decided to dump it.

![image](https://github.com/user-attachments/assets/980585cd-5def-426d-9aeb-1a8ba391e351)
![image](https://github.com/user-attachments/assets/c072427c-b517-4300-b0f9-079bc3c48c9a)

The clue revealed that the flag was split into two files: `flag1.png` and `flag2.png`. Using the addresses from the scan results, I dumped both files.

![image](https://github.com/user-attachments/assets/7ec8d370-8867-4808-b895-c4a7f56ccfc3)
![image](https://github.com/user-attachments/assets/6a80d19d-09cd-4c81-b6eb-379c736c3774)
![image](https://github.com/user-attachments/assets/ff26037d-5345-4781-a2cd-42be70f46c39)
![image](https://github.com/user-attachments/assets/04c2ab12-1ed2-4012-b652-776976f6f07f)

Contents of the extracted files:

<img width="223" alt="flag1" src="https://github.com/user-attachments/assets/dcf0ec1d-3bab-4908-81da-e5fcd8132555">
<img width="226" alt="flag2" src="https://github.com/user-attachments/assets/c6182f6e-06ae-4f61-a91e-7191c6ae63db">

## Flag
TechnoFair11{You_fiNd_THe_fLaG}
