## Unsolved (just missing the second part lol)

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



   
   

   
   
   


