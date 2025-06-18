import tkinter as tk

def summit_action():
     summit_label.config(text=f"Summited: name: {name_var.get()} \n Email: {email_var.get()} \n Age: {age_var.get()} \n PhoneNo: {phoneNo_var.get()}")


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

label = tk.Label(from_frame, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(from_frame, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=10, pady=10)

label = tk.Label(from_frame, text="Email").grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry = tk.Entry(from_frame, textvariable=email_var)
email_entry.grid(row=1, column=1, padx=10, pady=10)

label = tk.Label(from_frame, text="Age").grid(row=2, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(from_frame, textvariable=age_var)
age_entry.grid(row=2, column=1, padx=10, pady=10)

label = tk.Label(from_frame, text="Phone No").grid(row=3, column=0, padx=10, pady=10, sticky="e")
phoneNo_entry = tk.Entry(from_frame, textvariable=phoneNo_var)
phoneNo_entry.grid(row=3, column=1, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(padx= 10)

summit_button = tk.Button(button_frame,text="Summit",command=summit_action, fg="black", background="green")
summit_button.pack(padx=10, side="left")
clear_button = tk.Button(button_frame,text="Clear",command=clear_action, fg="black", background="red")
clear_button.pack(padx=10, side="left")

summit_label = tk.Label(root, text="", fg="Orange")
summit_label.pack(pady=5)

root.mainloop()