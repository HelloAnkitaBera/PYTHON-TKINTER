import tkinter as tk

# Logic function to handle login
def handle_login(username_var, password_var, status_label):
    username = username_var.get()
    password = password_var.get()

    if username == "admin" and password == "secret":
        status_label.config(text="Login successful", fg="green")
    else:
        status_label.config(text="Invalid credentials", fg="red")

# UI builder function
def create_login_form(root):
    username_var = tk.StringVar()
    password_var = tk.StringVar()

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    username_entry = tk.Entry(root, textvariable=username_var)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    password_entry = tk.Entry(root, textvariable=password_var, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    status_label = tk.Label(root, text="", fg="red")
    status_label.grid(row=3, column=0, columnspan=2, pady=5)

    login_btn = tk.Button(
        root,
        text="Login",
        command=lambda: handle_login(username_var, password_var, status_label)
    )
    login_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Main block
root = tk.Tk()
root.title("Modular Login Window")
root.geometry("300x180")

create_login_form(root)

root.mainloop()
