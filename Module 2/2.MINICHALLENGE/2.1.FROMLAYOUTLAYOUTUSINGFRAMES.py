import tkinter as tk

def summit_action():
     summit_label.config(text=f"summited: name: {name_var.get()}, email: {email_var.get()}, age: {age_var.get()}, phoneNo: {phoneNo_var.get()}")


def clear_action():
    name_var.set("")
    email_var.set("")
    age_var.set("")
    phoneNo_var.set("")

root = tk.Tk()
root.title("Documents")
root.geometry("854x400")

name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()
phoneNo_var = tk.StringVar()

from_frame = tk.Frame(root,bd = 2, relief= "groove", padx= 10, pady= 10)
from_frame.pack(padx= 10, pady= 10)

label = tk.Label(from_frame, text="Name")
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(from_frame, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=10, pady=10)

label = tk.Label(from_frame, text="Email")
label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry = tk.Entry(from_frame, textvariable=email_var)
email_entry.grid(row=1, column=1, padx=10, pady=10)

label = tk.Label(from_frame, text="Age")
label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(from_frame, textvariable=age_var)
age_entry.grid(row=2, column=1, padx=10, pady=10)

label = tk.Label(from_frame, text="Phone No")
label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
phoneNo_entry = tk.Entry(from_frame, textvariable=phoneNo_var)
phoneNo_entry.grid(row=3, column=1, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(padx= 10)

summit_button = tk.Button(button_frame,text="Summit",command=summit_action)
summit_button.pack(padx=10, side="left")
clear_button = tk.Button(button_frame,text="Clear",command=clear_action)
clear_button.pack(padx=10, side="left")

summit_label = tk.Label(root, text="", fg="green")
summit_label.pack(pady=5)

root.mainloop()