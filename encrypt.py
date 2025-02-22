import cv2
import os

# Load the image
img = cv2.imread("cat.jpg")  

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# ASCII mapping
d = {chr(i): i for i in range(256)}

# Store password length and message length 
img[0, 0, 0] = len(password)
img[0, 0, 1] = len(msg)

n, m = 0, 1  

# Store the passcode 
for char in password:
    img[n, m, 0] = d[char]
    m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Store the message 
for char in msg:
    img[n, m, 1] = d[char]
    m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Save encrypted image 
cv2.imwrite("encryptedImage.png", img)
print("Message encrypted successfully!")
os.system("start encryptedImage.png")  # Open image on Windows
