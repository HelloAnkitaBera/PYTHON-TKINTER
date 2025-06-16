import tkinter as tk

def show_input():
    user_input = entry.get()
    text_output = text_box.get("1.0", tk.END).strip()
    # print("Entry Value:", user_input)
    # print("Text Box Content:", text_output)
    summit_label.config(text=f"Entry Value: {user_input}. \n Text Box Content: {text_output}.")
    # summit_label.config(text=f"Text Box Content: {text_output}")


root = tk.Tk()
root.title("Basic Widgets")
root.geometry("854x400")

label = tk.Label(root, text="Welcome to Tkinter Widgets!")
label.pack()

entry = tk.Entry(root)
entry.pack()

text_box = tk.Text(root, height=5, width=30)
text_box.pack()

button = tk.Button(root, text="Submit", command=show_input)
button.pack()

summit_label = tk.Label(root, text="")
summit_label.pack()
root.mainloop()