import tkinter as tk

def create_contact_form(root):
    name_var = tk.StringVar()
    email_var = tk.StringVar()

    tk.Label(root, text="Name").pack()
    tk.Entry(root, textvariable=name_var).pack()

    tk.Label(root, text="Email").pack()
    tk.Entry(root, textvariable=email_var).pack()

    tk.Button(root, text="Submit", command=lambda: handle_submit(name_var, email_var)).pack()

def handle_submit(name_var, email_var):
    print("Submitted:", name_var.get(), email_var.get())

root = tk.Tk()
create_contact_form(root)
root.title("Structured Contact Form")
root.geometry("854x480")


root.mainloop()
