## Unsolved

The file given if **AD1** file so I open it using **FTK Imager**. There is non default user **ayaya** so I extracted it.

![Screenshot 2024-11-05 022221](https://github.com/user-attachments/assets/ffbd4d40-dbe4-41d7-878e-ca2461de65a9)

There is **Secret-file.zip** that needs password to be extracted.

![image](https://github.com/user-attachments/assets/0eeedf84-9403-4929-bd8a-48b54d2e5874)

From description we know that the flag is in another computer. I also found **Remote Desktop Connection (.rdp)** file.

![Screenshot 2024-11-05 022344](https://github.com/user-attachments/assets/27f55f7f-f5e2-40ff-ae60-10b9290f5532)

We can found cache file of windows RDP in \AppData\Local\Microsoft\Terminal Server Client\Cache

![Screenshot 2024-11-05 022614](https://github.com/user-attachments/assets/3038bc6b-84b5-4326-b34d-a79f39162ad5)

I used [bmc-tools.py](https://github.com/ANSSI-FR/bmc-tools) to parse cache file into some BMP files.

![Screenshot 2024-11-05 023221](https://github.com/user-attachments/assets/df41bc4f-ef43-448c-8fc5-d8cafd8e9afa)

It looks like the content of parsed file contain **Secret-file.zip** password.

Key = Selamat_ngerjain_hacktoday_yaaa

The extracted file is .docm formatted (macro enabled) so I tried to use [olevba](https://github.com/decalage2/oletools) tool.



