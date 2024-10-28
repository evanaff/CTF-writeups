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

   First part : hacktoday{j3_

   
   
   


