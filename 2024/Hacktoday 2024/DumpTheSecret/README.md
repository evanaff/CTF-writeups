# DumpTheSecret

### Status : Solved

## Category
Digital Forensic

## Description
Teman saya memberi sebuah memory dump dan berkata ada sebuah rahasia di dalamnya. [file](https://drive.google.com/file/d/1YSmW_WQMl_jFbGpZ6_nLQ-Mks3PynGod/view?usp=drive_link)
 
pass rar : letusstartthegame

## Solve
First, I check the type of **chall.raw** file.

![image](https://github.com/user-attachments/assets/49c045cf-0791-4a7c-84de-4d798110c71a)

Windows Event Trace Log file can be analyzed using volatility. First command I used is `windows.filescan` to scan all files in memory dumps.

![image](https://github.com/user-attachments/assets/e7dd176b-c606-4259-bcf0-ba529e3cf57f)

I found interesting file from filescan result named `secret.rar` so I dump it using windows.dumpfiles.

![image](https://github.com/user-attachments/assets/b0e2b22e-133c-405d-b24c-f7bd32437209)

![image](https://github.com/user-attachments/assets/4468834c-10db-4b1e-a008-6cd7d6bbb3ce)

![image](https://github.com/user-attachments/assets/7c26ee3e-b0f3-4642-9242-7b83e05e69c6)

It looks like the rar file needs a password to be extracted. So I try to find something in filescan result them I found `hint.txt`

![image](https://github.com/user-attachments/assets/0b15296b-f328-4058-9986-176466481fa8)

![image](https://github.com/user-attachments/assets/5026a376-5a7d-4fc4-a303-ecf1ea6cac11)

![image](https://github.com/user-attachments/assets/4cb181c1-d7cd-42f0-8984-6f661fedc819)

It said the rar password maybe same as pc password. So I find it using windows.hashdump then crack user password (Afif) on [Crackstation](https://crackstation.net/)

![image](https://github.com/user-attachments/assets/4ae1cc72-3e06-41da-8f69-97783ef8ca65)

![image](https://github.com/user-attachments/assets/89153c0d-daa2-4295-8f95-2bfa875e6f99)

Just open the rar file with cracked password and we found the flag.

![flag](https://github.com/user-attachments/assets/793f8b67-d936-44e7-95c6-02848eb38b73)

## Flag
hacktoday{mA5qu3R4de_0f_Gu1lTy}

