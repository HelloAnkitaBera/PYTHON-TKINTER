import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validate_inputs(name, age, email):
    if not name or not age or not email:
        return "All fields are required."
    if not age.isdigit():
        return "Age must be a number."
    if "@" not in email or "." not in email:
        return "Invalid email format."
    return None

def clear_form():
    name_var.set("")
    age_var.set("")
    email_var.set("")
    gender_var.set("")
    course_var.set("")

def save_to_file(data):
    with open("registrations.txt", "a") as file:
        file.write(data + "\n")

def register_student():
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    course = course_var.get()
    email = email_var.get()

    error = validate_inputs(name, age, email)
    if error:
        messagebox.showerror("Validation Error", error)
        return

    entry = f"{name}, {age}, {gender}, {course}, {email}"
    save_to_file(entry)
    messagebox.showinfo("Success", "Student registered successfully.")
    clear_form()

# Setup window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("854x480")

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")
course_var = tk.StringVar()
email_var = tk.StringVar()

# Form Frame
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(fill="both", expand=True)

# Form layout
tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Age:").grid(row=1, column=0, sticky="e")
tk.Entry(form_frame, textvariable=age_var).grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Gender:").grid(row=2, column=0, sticky="e")
gender_frame = tk.Frame(form_frame)
gender_frame.grid(row=2, column=1, pady=5, sticky="w")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")

tk.Label(form_frame, text="Course:").grid(row=3, column=0, sticky="e")
ttk.Entry(form_frame, textvariable=course_var).grid(row=3, column=1, pady=5)

tk.Label(form_frame, text="Email:").grid(row=4, column=0, sticky="e")
tk.Entry(form_frame, textvariable=email_var).grid(row=4, column=1, pady=5)

# Buttons
button_frame = tk.Frame(root, pady=10)
button_frame.pack()

tk.Button(button_frame, text="Register", command=register_student).pack(side="left", padx=10)
tk.Button(button_frame, text="Clear", command=clear_form).pack(side="left", padx=10)

root.mainloop()
