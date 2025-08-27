# Keyboard Catcher

### Status : Upsolved

## Category
Forensics

## Description
she say she put keylogger in my wsl. is it true?
[chall.zip](https://drive.google.com/file/d/1dFzJX8Xfxr2XdpojbQr5Fx1_sgQVlCo-/view?usp=sharing)

## Solution
I got 2 files:

![image](https://github.com/user-attachments/assets/078a3c5f-b8af-45a3-9f4c-b4d71fd4f891)

The first one is a shell script:

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

This script encodes the content of `flag.txt` 5 times with `Base64`, then prints the result character by character with a delay.

The second file looked strange in Notepad. After checking, I realized it was an `API Monitor 64-bit` capture, which can be analyzed using [http://www.rohitab.com/apimonitor/](http://www.rohitab.com/apimonitor/).

While analyzing, I found something interesting: an API call to `WriteFile`.

![image](https://github.com/user-attachments/assets/9bbb32ab-7236-48e0-904f-3e8e193aa195)

From the hex buffer, I could see that the shell script had been executed in `wsl.exe`.

![image](https://github.com/user-attachments/assets/45608d5e-c70e-49f4-a0ac-9a263fe085fd)

So, I parsed the captured program output (the encoded `flag.txt`) manually and got this:

```VjFaV2ExSXlSblJTV0hCV1lteHdhRlZxUWxwTlZuQlZVMnM1YUZJeFNrbFdSekExVjFVeGNWSnVUbGhpUjFKWVdXdGFkMWRHV25SbApSMFpYVFZad2VsWXdVa3RqTWtwWFdqTndWd3BpVm5CaFZGZDBZVTFXWkVWVWJUbHFVakZhU1ZsclVsTmhRWEJZVWpKb00xZHRlRVpQClZrSlNVRlF3UFE9PQ==```

Decoding it with `Base64` 5 times revealed the flag.

![image](https://github.com/user-attachments/assets/705079ca-76cc-40d0-974a-01b4d7cb7a5b)

## Flag
hacktoday{catch_meeeeeeeeee_if_u_can_xixixixi}


