import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.png")

# Retrieve stored lengths
password_length = img[0, 0, 0]
message_length = img[0, 0, 1]

# Mapping pixel values back to ASCII
c = {i: chr(i) for i in range(256)}
n, m = 0, 1  

# Retrieve the stored passcode
stored_password = ""
for _ in range(password_length):
    stored_password += c[img[n, m, 0]]
    m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Ask the user for passcode 
user_password = input("Enter passcode for Decryption: ")

# Check automatically with stored passcode
if user_password == stored_password:
    # Retrieve the message
    message = ""
    for _ in range(message_length):
        message += c[img[n, m, 1]]
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

    print("Decryption message:", message)
else:
    print("Incorrect passcode! Decryption failed.")
