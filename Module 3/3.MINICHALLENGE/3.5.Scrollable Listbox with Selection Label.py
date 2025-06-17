import tkinter as tk

def show_selection(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        value = listbox.get(index)
        selection_label.config(text=f"Selected: {value}")


root = tk.Tk()
root.title("Listbox with Scrollbar")
root.geometry("854x480")


list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill="both", expand=True)


scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")


listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=10)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)


items = [f"Item {i}" for i in range(1, 31)]
for item in items:
    listbox.insert(tk.END, item)


listbox.bind("<<ListboxSelect>>", show_selection)


selection_label = tk.Label(root, text="Selected: None", font=("Arial", 12))
selection_label.pack(pady=10)

root.mainloop()
