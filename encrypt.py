import qrcode
from PIL import Image
from cryptography.fernet import Fernet
import cv2

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        fileContents = file.read()
    encryptedFileContents = f.encrypt(fileContents)
    with open(filename, "wb") as file:
        file.write(encryptedFileContents)

filename = input("What file do you want to encrypt > ")
imgFilename = input("What do you want the output file to be called (optional, ex. \"qrcode\" for qrcode.png) > ")
if imgFilename == "": imgFilename = "qrcode"

imgFilename += ".png"

key = Fernet.generate_key().decode("utf-8")
print("key: %s" % (key))
encrypt(filename, key)

img = qrcode.make(key)
img.save(imgFilename)
img = cv2.imread(imgFilename)
cv2.imshow("QR Code (key)", img)
cv2.waitKey(0)
