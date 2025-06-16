import tkinter as tk

def greet():
    name = name_entry.get()
    greeting_label.config(text=f"{name}!")

root = tk.Tk()
root.geometry("854x480")
root.title("Greeter")

tk.Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Greet", command=greet).grid(row=1, column=1, padx=10, pady=10, columnspan=2)


greeting_label = tk.Label(root, text="")
greeting_label.grid(row=2, column=1, columnspan=2, pady=10)


root.mainloop()
