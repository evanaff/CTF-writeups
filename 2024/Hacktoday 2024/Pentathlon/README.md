# Pentathlon

### Status : Upsolved

## Category
Forensics

## Description
I forgot the detail but in this challange tou must solve 5 challenge from the file given. Here is the file [chall1.png](https://drive.google.com/file/d/1FJfTWcS9Bj2R9b6O7k9x1N1C26BKk8ZA/view?usp=drive_link)

## Solve
Almost got it, just missing the second part lol.

As mentioned in challenge description, we need to solve 5 steps of challenge.

1. Step 1

   ![chall1](https://github.com/user-attachments/assets/63ddeefc-2cc7-4278-aaa4-336d66775a38)
   
   The png file mention about binwalk so i checked using binwalk command and extract it. There is file named **20.png**
   
   ![20](https://github.com/user-attachments/assets/646c4573-036c-4f84-ace0-7784d39fe98a)
   
   I assumed that we need to use binwalk command until we found the flag. So I used script to make things easier.
   ```python
   import subprocess

   path = ""

    for i in range(20, 0, -1):
      index = ""
      if i < 10:
        index = f"0{i}"
      else:
        index = f"{i}"
    
      target_file = path + f"{index}.png"

      print(target_file)

      subprocess.run(['binwalk', '-e', target_file])

      next_path = f"_{index}.png.extracted/"
      path = path + next_path 
   ```
   ![01](https://github.com/user-attachments/assets/94d1ba38-bcf7-4209-b0e3-16b73274d5ca)

   part 1 : hacktoday{j3_

2. Step 2

   The result of last binwalk also give me **chall2.jpg**

   ![chall2](https://github.com/user-attachments/assets/07445bf4-9efc-4a9b-8852-cc40f65a31d9)

   From the text, I assumed that the image is cropped. From [wikipedia](https://en.wikipedia.org/wiki/JPEG) I found that the height value of jpg image is saved in hex value. I also found more 
   spesific of where is the hex value of the height from [here](https://cyberhacktics.com/hiding-information-by-changing-an-images-height/)

   ![image](https://github.com/user-attachments/assets/12bbb1e1-3bdd-4382-a076-3f78ae71518b)
   ![image](https://github.com/user-attachments/assets/2977df10-5f90-470d-b1d6-ed420abbea5b)

   So I change the height value so it becomes higher.

   ![image](https://github.com/user-attachments/assets/d33dcd08-982e-4f52-8c57-d960a04400bf)

   ![chall2](https://github.com/user-attachments/assets/af9d1e46-c143-4f19-b053-e6b7807dc1e5)

   part 2 : cr0is_3n_m0i

3. Step 3

   From the extended file before we know that the next challenge is in file's metadata, so I used exiftool to access it. There is google drive link for next challenge.

   ![image](https://github.com/user-attachments/assets/a0fa22d5-e28e-4069-ba51-3ca3e9b0fda5)

   ![image](https://github.com/user-attachments/assets/d4b72d3d-09ae-492b-b0c8-1d02c5763c09)

   I crack the zipfile using fcrackzip and rockyou.txt

   ![image](https://github.com/user-attachments/assets/c70ca740-bb75-4c9f-8fea-3b53f9aaee6b)

   ![image](https://github.com/user-attachments/assets/72e8697c-fa04-4840-a083-2a1e18860bed)

   part 3 : _for_1_b3li3

4. Step 4

   In this challenge we have a png file **chall4.png** a a **script.py**. It looks like the script encoded a secret message from somewhere to **chall4.png**.
   ```python
   from PIL import Image

   message = open("secret.txt", "r").read()
   msg = [ord(m) for m in message]

   image = Image.open("chall4_original.png")
   pixels = image.load()

   for i in range(len(msg)):
       r, g, b = pixels[i*3,0]
       pixels[i*3,0] = msg[i]^g, g^b, b

   image.save("chall4.png")
   ```
   This script encoded a message to **chall4.png** by modifying rgb values. Each character in message converted into ascii/ord then xorred by g value and saved in r value of image. g value of 
   image also xorred by b value and the b value doesn't change. So we can just xor it back to obtain the message value. I used this script to decode the script message.
   ```python
   from PIL import Image

   image = Image.open('chall4.png')
   pixels = image.load()

   message = ""

   for i in range(120):
       r, g, b = pixels[i*3,0]
       g = g^b
       message += chr(r^g)

   print(message)
   ```
   
   ![image](https://github.com/user-attachments/assets/5beabee3-2ae3-4925-a591-aa83c159baa3)

   part 4 : ve_1n_mys3lf

5. Step 5

   There is a hint

   ![chall5](https://github.com/user-attachments/assets/cdf53c09-1827-41e2-8029-c770c1131062)

   I guess we just need to fix **finish.png**. So I check it first using **pngcheck**.

   ![image](https://github.com/user-attachments/assets/a4514dc4-f882-4e87-b56f-b113b970396b)

   It looks like an error chunk. The correct value also has been showed in the pngcheck result. So I fixed it using hexeditor. Repeat it until the png file fully fixed.

   ![finish](https://github.com/user-attachments/assets/399b3fd3-d6b9-4728-b9f3-16cda5632f54)

   part 5 : _7e6afd6912}

## Flag
hacktoday{j3_cr0is_3n_m0i_for_1_b3li3ve_1n_mys3lf_7e6afd6912}

   



   



   
   

   
   
   




