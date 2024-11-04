## Unsolved

We got 2 files

![image](https://github.com/user-attachments/assets/078a3c5f-b8af-45a3-9f4c-b4d71fd4f891)

Content of shell source file :

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

That codes encodes the content of file.txt 5 times then echo each character of the result with delay.

For the other file, when we open it using notepad we can know that the file is an API Monitor 64-bit capture that can be analyze with apimonitor tools from [http://www.rohitab.com/apimonitor/](http://www.rohitab.com/apimonitor/).

I found something that caught my attention, an API called **WriteFile**.

![image](https://github.com/user-attachments/assets/9bbb32ab-7236-48e0-904f-3e8e193aa195)

From analyzing the hex buffer we can know that the shellcode before was executed in this terminal (wsl.exe)

![image](https://github.com/user-attachments/assets/45608d5e-c70e-49f4-a0ac-9a263fe085fd)

So I parse the output of program which is encoded flag.txt manually and this is the result.

``VjFaV2ExSXlSblJTV0hCV1lteHdhRlZxUWxwTlZuQlZVMnM1YUZJeFNrbFdSekExVjFVeGNWSnVUbGhpUjFKWVdXdGFkMWRHV25SbApSMFpYVFZad2VsWXdVa3RqTWtwWFdqTndWd3BpVm5CaFZGZDBZVTFXWkVWVWJUbHFVakZhU1ZsclVsTmhRWEJZVWpKb00xZHRlRVpQClZrSlNVRlF3UFE9PQ==``

Then just decode it using base64 5 times.

![image](https://github.com/user-attachments/assets/705079ca-76cc-40d0-974a-01b4d7cb7a5b)

## Flag
hacktoday{catch_meeeeeeeeee_if_u_can_xixixixi}
