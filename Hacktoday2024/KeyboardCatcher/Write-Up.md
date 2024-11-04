## Unsolved

We got 2 files

![image](https://github.com/user-attachments/assets/078a3c5f-b8af-45a3-9f4c-b4d71fd4f891)

Content of sh source file :

```shell
#!/bin/bash

content=$(<flag.txt)

for i in {1..5}; do
    content=$(echo -n "$content" | base64)
done

finalContent=$content

for ((i=0; i<${#finalContent}; i++)); do
    char="${finalContent:$i:1}"
    echo -n "$char"
    sleep 0.01
done

echo -e "\nDone"
```
