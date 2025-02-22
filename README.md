# Secure Data Hiding in Images using Steganography

This project implements steganography — the technique of hiding secret messages within digital images. Using a python and OpenCV with the help of graphical user interface (GUI) built with Tkinter, users can encrypt a secret message into an image and later decrypt it using a passcode. 

## Features

- **Encryption:-**  
  Allows users to select an image for hiding data.Takes a secret message and passcode as input.Stores the passcode and message length in the image’s first pixel values.Embeds the message securely into the image’s pixel values without altering its visual quality.Saves the encrypted image in a secure format (PNG) to prevent data loss

- **Decryption:-**  
  Accepts an encrypted image and passcode as input.Validates the user-entered passcode with the stored passcode which was entered in encryption process.Extracts and displays the hidden message directly in the application’s GUI.

- **Graphical User Interface (GUI):-**  
  Simple and attractive interface for both encryption and decryption.
  - Takes a cover image from user.
  - User Enters the secret message and passcode.
  - Encrypts the message in the image.
  - Generates an encrypted image.
  - Decrypts the hidden message from encrypted image.

## Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)

  Install via pip:  
  ```bash
  pip install opencv-python

## Screenshot
![Image]()
