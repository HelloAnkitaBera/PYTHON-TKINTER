import tkinter as tk

def update_feedback(*args):
    name = name_var.get()
    gender = gender_var.get()
    terms_accepted = "Yes" if terms_var.get() else "No"

    output_text = (
        f"Hello {name}!\n"
        f"Gender: {gender}\n"
        f"Accepted Terms: {terms_accepted}"
    )
    output_label.config(text=output_text)


root = tk.Tk()
root.title("Live Feedback Form")
root.geometry("854x480")


name_var = tk.StringVar()
gender_var = tk.StringVar(value="Not selected")
terms_var = tk.BooleanVar()


name_var.trace_add("write", update_feedback)
gender_var.trace_add("write", update_feedback)
terms_var.trace_add("write", update_feedback)


tk.Label(root, text="Your Name:").pack(anchor="w", padx=10, pady=5)
tk.Entry(root, textvariable=name_var).pack(fill="x", padx=10)


tk.Label(root, text="Gender:").pack(anchor="w", padx=10, pady=5)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", command=update_feedback).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", command=update_feedback).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", command=update_feedback).pack(anchor="w", padx=20)


tk.Checkbutton(root, text="Accept Terms and Conditions", variable=terms_var).pack(anchor="w", padx=10, pady=5)


feedback_label = tk.Label(root, text="", justify="left", fg="green")
feedback_label.pack(padx=10, pady=10, anchor="w")


output_frame = tk.LabelFrame(root, text="Output", padx=10, pady=10)
output_frame.pack(padx=10, pady=10, fill="x")

output_label = tk.Label(output_frame, text="", fg="Black", justify="left")
output_label.pack(anchor="w")


root.mainloop()
