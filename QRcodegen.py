import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk, ImageFilter

def generate_qr_code():
    phone_number = entry.get()
    if not phone_number:
        messagebox.showwarning("Input Error", "Please enter a phone number.")
        return

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(f"tel:{phone_number}")
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image file
    # Save the image file
    filename = f"{phone_number}_qr.png"
    img.save(filename)

    # Display the image
    img = Image.open("phone_number_qr.png")
    img = img.resize((200, 200), Image.BICUBIC)
    img = ImageTk.PhotoImage(img)

    qr_label.config(image=img)
    qr_label.image = img

# Create the main window
root = tk.Tk()
root.title("Phone Number QR Code Generator")

# Create and place widgets
tk.Label(root, text="Enter Phone Number:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=20)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
