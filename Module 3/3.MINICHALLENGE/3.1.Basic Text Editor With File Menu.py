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
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")

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
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

def exit_app():
    root.quit()

# Setup window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("854x480")

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Text area
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

root.mainloop()


