import tkinter as tk

def submit_form():
    summit_label.config(
        text=f"Summited: "
             f"Gender: {gender_var.get()}, "
             f"Daily Updates: {'Yes' if daily_var.get() else 'No'}, "
             f"Weekly Summary: {'Yes' if weekly_var.get() else 'No'}, "
             f"Age: {age_spinbox.get()}"
    )
 
 ##print("Gender:", gender_var.get())
   ## print("Daily Updates:", "Yes" if daily_var.get() else "No")
    ##print("Weekly Summary:", "Yes" if weekly_var.get() else "No")
    ##print("Age:", age_spinbox.get())


# Root window
root = tk.Tk()
root.title("User Preferences Form")
root.geometry("854x480")

# Variables
gender_var = tk.StringVar(value="Male")
daily_var = tk.IntVar()
weekly_var = tk.IntVar()

# === Gender Frame ===
gender_frame = tk.LabelFrame(root, text="Select Gender", padx=10, pady=10)
gender_frame.pack(padx=10, pady=5, fill="x")

tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(anchor="w")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(anchor="w")
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(anchor="w")

# === Subscription Frame ===
subs_frame = tk.LabelFrame(root, text="Newsletter Subscription", padx=10, pady=10)
subs_frame.pack(padx=10, pady=5, fill="x")

tk.Checkbutton(subs_frame, text="Daily Updates", variable=daily_var).pack(anchor="w")
tk.Checkbutton(subs_frame, text="Weekly Summary", variable=weekly_var).pack(anchor="w")

# === Age Frame ===
age_frame = tk.Frame(root)
age_frame.pack(padx=10, pady=10, fill="x")

tk.Label(age_frame, text="Select Age:").pack(anchor="w")
age_spinbox = tk.Spinbox(age_frame, from_=18, to=60, width=5)
age_spinbox.pack(anchor="w")

# === Submit Button ===
tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

summit_label = tk.Label(root, text="", fg="green")
summit_label.pack(pady=5)

root.mainloop()

