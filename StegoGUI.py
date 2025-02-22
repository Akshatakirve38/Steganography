import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Global variable for image path
image_path = ""

def select_image_encrypt():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        label_selected_image_encrypt.config(text=f"Selected: {os.path.basename(image_path)}", fg="lightgreen")

def encrypt_message():
    global image_path
    if not image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return

    msg = entry_message.get()
    password = entry_passcode.get()

    if not msg or not password:
        messagebox.showerror("Error", "Please enter both message and passcode!")
        return

    d = {chr(i): i for i in range(256)}

    img[0, 0, 0] = len(password)
    img[0, 0, 1] = len(msg)

    n, m = 0, 1  

    for char in password:
        img[n, m, 0] = d[char]
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

    for char in msg:
        img[n, m, 1] = d[char]
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

    save_path = "encryptedImage.png"
    cv2.imwrite(save_path, img)
    messagebox.showinfo("Success", f"Message encrypted successfully!\nSaved as {save_path}")
    os.system(f"start {save_path}")

def select_image_decrypt():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        label_selected_image_decrypt.config(text=f"Selected: {os.path.basename(image_path)}", fg="lightgreen")

def decrypt_message():
    global image_path
    if not image_path:
        messagebox.showerror("Error", "Please select an encrypted image first!")
        return

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return

    password_length = img[0, 0, 0]
    message_length = img[0, 0, 1]

    c = {i: chr(i) for i in range(256)}

    n, m = 0, 1  

    stored_password = ""
    for _ in range(password_length):
        stored_password += c[img[n, m, 0]]
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1

    user_password = entry_passcode_decrypt.get()

    if user_password == stored_password:
        message = ""
        for _ in range(message_length):
            message += c[img[n, m, 1]]
            m += 1
            if m >= img.shape[1]:  
                m = 0
                n += 1

        text_decrypted_message.delete("1.0", tk.END)
        text_decrypted_message.insert(tk.END, message)
    else:
        text_decrypted_message.delete("1.0", tk.END)
        text_decrypted_message.insert(tk.END, "❌ Incorrect passcode! Decryption failed.")

# GUI Setup
root = tk.Tk()
root.title("🔐 Image Steganography - Encrypt & Decrypt")
root.geometry("700x900")  # Set window size
root.configure(bg="#1E1E2E")  # Dark Purple Background

style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=10)

# ---------------- Encryption Section ----------------
frame_encrypt = tk.Frame(root, bg="#3A3A5D", padx=15, pady=15)
frame_encrypt.pack(pady=20, fill="both")

tk.Label(frame_encrypt, text="🔒 Encryption", font=("Arial", 16, "bold"), fg="white", bg="#3A3A5D").pack()

btn_select_encrypt = ttk.Button(frame_encrypt, text="Select Image", command=select_image_encrypt)
btn_select_encrypt.pack(pady=8)

label_selected_image_encrypt = tk.Label(frame_encrypt, text="No image selected", font=("Arial", 12), fg="red", bg="#3A3A5D")
label_selected_image_encrypt.pack()

tk.Label(frame_encrypt, text="Enter Secret Message:", fg="white", bg="#3A3A5D", font=("Arial", 12)).pack(pady=5)
entry_message = tk.Entry(frame_encrypt, width=50, font=("Arial", 12))
entry_message.pack()

tk.Label(frame_encrypt, text="Enter Passcode:", fg="white", bg="#3A3A5D", font=("Arial", 12)).pack(pady=5)
entry_passcode = tk.Entry(frame_encrypt, width=50, show="*", font=("Arial", 12))
entry_passcode.pack()

btn_encrypt = ttk.Button(frame_encrypt, text="Encrypt & Save", command=encrypt_message)
btn_encrypt.pack(pady=15)

# ---------------- Decryption Section ----------------
frame_decrypt = tk.Frame(root, bg="#5D3A69", padx=15, pady=15)
frame_decrypt.pack(pady=20, fill="both")

tk.Label(frame_decrypt, text="🔓 Decryption", font=("Arial", 16, "bold"), fg="white", bg="#5D3A69").pack()

btn_select_decrypt = ttk.Button(frame_decrypt, text="Select Encrypted Image", command=select_image_decrypt)
btn_select_decrypt.pack(pady=8)

label_selected_image_decrypt = tk.Label(frame_decrypt, text="No image selected", font=("Arial", 12), fg="red", bg="#5D3A69")
label_selected_image_decrypt.pack()

tk.Label(frame_decrypt, text="Enter Passcode:", fg="white", bg="#5D3A69", font=("Arial", 12)).pack(pady=5)
entry_passcode_decrypt = tk.Entry(frame_decrypt, width=50, show="*", font=("Arial", 12))
entry_passcode_decrypt.pack()

btn_decrypt = ttk.Button(frame_decrypt, text="Decrypt", command=decrypt_message)
btn_decrypt.pack(pady=15)

tk.Label(frame_decrypt, text="Decrypted Message:", fg="white", bg="#5D3A69", font=("Arial", 12)).pack()
text_decrypted_message = tk.Text(frame_decrypt, height=1,width=50, font=("Arial", 12))
text_decrypted_message.pack(pady=10)

# Run the main loop
root.mainloop()
