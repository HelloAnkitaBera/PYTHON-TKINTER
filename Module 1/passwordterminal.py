import tkinter as tk

def toggle_password():
    if show_var.get():
        password_entry.config(show="")  # Show actual text
    else:
        password_entry.config(show="*")  # Mask input

def check_password_field(*args):
    if password_var.get():
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

def submit_password():
    print("Submitted Password:", password_var.get())

root = tk.Tk()
root.title("Password Entry")
root.geometry("854x480")

# StringVar to track password input
password_var = tk.StringVar()
password_var.trace_add("write", check_password_field)

# BooleanVar to track checkbox state
show_var = tk.BooleanVar()

# Widgets
tk.Label(root, text="Enter Password:").pack(pady=5)

password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.pack(pady=5)

show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_checkbox.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", state="disabled", command=submit_password)
submit_btn.pack(pady=10)

root.mainloop()