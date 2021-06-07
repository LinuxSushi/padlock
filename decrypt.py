import cv2
import numpy as np
from pyzbar.pyzbar import decode
from cryptography.fernet import Fernet, InvalidToken

filename = input("What file do you want to decrypt > ")

def decrypt(filename, key):
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            encryptedData = file.read()
        decryptedFileData = f.decrypt(encryptedData)
        with open(filename, "wb") as file:
            encryptedData = file.write(decryptedFileData)
        return decryptedFileData
    except Exception as e:
        print("Error occured whilst decrypting: %s" % (e))
        return None

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    try:
        barcode = decode(gray_img)[0]
    except IndexError as e:
        return None
    barcodeData = barcode.data.decode("utf-8")
    return str(barcodeData)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    barcodeData = decoder(frame)
    if barcodeData != None:
        decryptedFileData = decrypt(filename, barcodeData)
        if decryptedFileData != None:
            print("*** DECRYPTED into file \"%s\" ***" % (filename))
            break
    cv2.imshow('Code scanner', frame)
    cv2.waitKey(10)
