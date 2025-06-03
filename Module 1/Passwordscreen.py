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

def password():
    password = password_entry.get()
    #print("Submitted Password:", password_var.get())   
    submit_label.config(text=f"Summited password: {password}")

root = tk.Tk()
root.title("Password Entry")
root.geometry("854x480")

# StringVar to track password input
password_var = tk.StringVar()
password_var.trace_add("write", check_password_field)

# BooleanVar to track checkbox state
show_var = tk.BooleanVar()

# Widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10, sticky="e")

password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_checkbox.grid(row=1, column=1,columnspan=2, padx=10, pady=10)

submit_btn = tk.Button(root, text="Submit", state="disabled", command=password)
submit_btn.grid(row=2, column=0, columnspan=2,padx=10, pady=10)

submit_label = tk.Label(root, text="", fg="green")
submit_label.grid(row=3, column=0, columnspan=2,padx=10, pady=10)


root.mainloop()