# 1.7 Mini Project Solution: Login Window with Username/Password C
import tkinter as tk

# Hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "secret"

def validate_fields(*args):
    #Enable login button only if both fields have content
    if username_var.get() and password_var.get():
        login_btn.config(state="normal")
    else:
        login_btn.config(state="disabled")

def login():
    userName = username_var.get()
    passWord = password_var.get()

    if userName == VALID_USERNAME and passWord == VALID_PASSWORD:
        status_label.config(text="Login successful", fg="green")
    else:
        status_label.config(text="Invalid credentials", fg="red")

# GUI setup
root = tk.Tk()
root.title("Login Window")
root.geometry("854x480")

# Variables
username_var = tk.StringVar()
password_var = tk.StringVar()

# Trace input fields
username_var.trace_add("write", validate_fields)
password_var.trace_add("write", validate_fields)

# Widgets
username=tk.Label(root, text="Username:")
username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

username_entry = tk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password=tk.Label(root, text="Password:")
password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_btn = tk.Button(root, text="Login", state="disabled", command=login, fg="black", background="green")
login_btn.grid(row=2, column=0, columnspan=2, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
 
