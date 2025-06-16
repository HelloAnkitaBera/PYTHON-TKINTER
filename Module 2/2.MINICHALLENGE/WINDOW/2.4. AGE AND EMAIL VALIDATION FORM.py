import tkinter as tk

def validate_age(value):
    return value.isdigit() or value == ""

def submit():

    age = age_var.get()
    email = email_var.get()

    ##submit_label.config(text=f"Submitted: Age: {age}, Email: {email}")

    # Clear previous error message
    ##submit_label.config(text="")

    if not age:
        output_label.config(text="Age is required.")
    elif not email:
        output_label.config(text="Email is required.")
    elif "@" not in email or "." not in email:
        output_label.config(text="Invalid email format.", fg="red")
    else:
        output_label.config(text= f"Age: {age}\nEmail: {email}\nForm submitted successfully.", fg="green")


root = tk.Tk()
root.title("Validation Form")
root.geometry("854x480")


age_var = tk.StringVar()
email_var = tk.StringVar()


tk.Label(root, text="Enter Age:").pack(anchor="w", padx=10, pady=(10, 0))
vcmd = (root.register(validate_age), '%P')
tk.Entry(root, textvariable=age_var, validate="key", validatecommand=vcmd).pack(fill="x", padx=10)


tk.Label(root, text="Enter Email:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=email_var).pack(fill="x", padx=10)


tk.Button(root, text="Submit", command=submit, fg="Black", background="Green").pack(pady=10)


error_label = tk.Label(root, text="", fg="red")
error_label.pack()

summit_label = tk.Label(root, text="", fg="green")
summit_label.pack(pady=5)

output_frame = tk.LabelFrame(root, text="Output", padx=10, pady=10)
output_frame.pack(padx=10, pady=10, fill="x")

output_label = tk.Label(output_frame, text="", fg="purple", justify="left")
output_label.pack(anchor="w")


root.mainloop()
