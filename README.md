# Secure Data Hiding in Images using Steganography

This project demonstrates a simple implementation of image steganography using Python and OpenCV. The application allows users to hide (encrypt) a secret message inside an image and later retrieve (decrypt) the message using a simple UI built with Tkinter.

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
