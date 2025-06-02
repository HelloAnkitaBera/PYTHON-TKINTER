import tkinter as tk

def greet():
    name = name_entry.get()
    # print(f"Hello, {name}!")
    greeting_label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.geometry("854x400")
root.title("Greeter")

tk.Label(root, text="Enter your name: ").pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

greet_btn = tk.Button(root, text="Greet", command=greet)
greet_btn.pack(pady=5)

greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=5)

root.mainloop()
