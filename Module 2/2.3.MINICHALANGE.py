import tkinter as tk

def update_feedback(*args):
    name = name_var.get()
    gender = gender_var.get()
    terms_accepted = "Yes" if terms_var.get() else "No"

    feedback_text = (
        f"Hello {name}!\n"
        f"Gender: {gender}\n"
        f"Accepted Terms: {terms_accepted}"
    )
    feedback_label.config(text=feedback_text)

# Root window
root = tk.Tk()
root.title("Live Feedback Form")
root.geometry("854x480")

# Variables
name_var = tk.StringVar()
gender_var = tk.StringVar(value="Not selected")
terms_var = tk.BooleanVar()

# Trace changes
name_var.trace_add("write", update_feedback)
gender_var.trace_add("write", update_feedback)
terms_var.trace_add("write", update_feedback)

# Name input
tk.Label(root, text="Your Name:").pack(anchor="w", padx=10, pady=5)
tk.Entry(root, textvariable=name_var).pack(fill="x", padx=10)

# Gender selection
tk.Label(root, text="Gender:").pack(anchor="w", padx=10, pady=5)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", command=update_feedback).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", command=update_feedback).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", command=update_feedback).pack(anchor="w", padx=20)

# Terms checkbox
tk.Checkbutton(root, text="Accept Terms and Conditions", variable=terms_var).pack(anchor="w", padx=10, pady=5)

# Live feedback label
feedback_label = tk.Label(root, text="", justify="left", fg="green")
feedback_label.pack(padx=10, pady=10, anchor="w")

root.mainloop()
