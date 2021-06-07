# Notes
This has only been tested on Windows 10. I'll probably test on Mac and Linux soon. Maybe BSD?
# About
This program encrypts and decrypts files, using a QR code as the key using Fernet. This handles text and binary files, as it using binary data instead of strings, and opening files in binary mode instead of text mode.
# Dependencies
- pip install cryptography
- pip install Pillow
- pip install opencv-python
- pip install pyzbar
- pip install qrcode
- download and install [Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-us/download/details.aspx?id=40784)
# How to use
## To encrypt the file
- Run encrypt.py
- Enter the name of the file you want to encrypt.
- The file will be saved in that file.
- Enter the name of the file you want the QR code to be stored in.
- The QR code will show up on the screen. You can take a picture of it on your phone or something.
## To decrypt the file
- Run decrypt.py
- Enter the name of the file you want to decrypt
- Show the QR code in front of the webcam
