from tkinter import *
from tkinter import messagebox
import pyqrcode 
import re

def generate_QR():
    info1=e1.get()
    if not re.match(r"^[0-9]{10}$", info1):
            messagebox.showinfo("Error", "Please enter a valid mobile number")
            return
    if len(user_input.get())!=0 :
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
        l1.config(image = img)
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    
    

root=Tk()
root.title("QR Code Generator")
root.minsize(width=400,height=400)
root.geometry("500x500")

lbl = Label(root,text="Enter mobile number", bg='Grey',fg="Black")
lbl.pack()
user_input = StringVar()
e1 = Entry(root,textvariable = user_input)
e1.pack(padx=10)



b1 = Button(root, text="Generate QR", command=generate_QR)
b1.pack()

l1=Label(root,text="",bg="Grey",fg="black")
l1.pack()

root.mainloop()

