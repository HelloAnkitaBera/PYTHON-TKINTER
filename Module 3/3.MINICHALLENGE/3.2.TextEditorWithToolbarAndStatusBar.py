import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, content)
                update_status("File opened")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")
            update_status("Failed to open file")

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save File",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", tk.END).strip())
                update_status("File saved")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
            update_status("Failed to save file")

def clear_text():
    confirm = messagebox.askyesno("Confirm", "Clear all text?")
    if confirm:
        text_area.delete("1.0", tk.END)
        update_status("Text cleared")

def update_status(message):
    status_label.config(text=message)


root = tk.Tk()
root.title("Text Editor with Toolbar and Status Bar")
root.geometry("854x480")


toolbar = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar, text="Open", command=open_file).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Save", command=save_file).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Clear", command=clear_text).pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill="x")


text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=5, pady=5)


status_label = tk.Label(root, text="Ready", bd=1, relief="sunken", anchor="w")
status_label.pack(side="bottom", fill="x")

root.mainloop()
