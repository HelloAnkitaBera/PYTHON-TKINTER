import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("854x480")

# Login function
def login():
	username = username_entry.get()
	password = password_entry.get()
	#print(f"Username: {username}, Password: {password}")
	login_label.config(text=f"Username: {username}, Password: {password}")


# Username row
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password row
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)


# Login label (define before login function uses it)
login_label = tk.Label(root, text="")
login_label.grid(row=3, column=0, columnspan=2, pady=10)
root.mainloop()
