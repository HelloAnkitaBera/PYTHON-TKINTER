import tkinter as tk
from tkinter import messagebox, filedialog


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

	
root = tk.Tk()
root.title("Menu Bar")
root.geometry("854x480")


text_area = tk.Text(root, wrap="word")
text_area.pack(expand=1, fill="both")


menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)

def openview_file():
    messagebox.showinfo("Open View", "Open View option selected.")

def explorer_file():
    messagebox.showinfo("Explorer", "Explorer option selected.")

view_menu.add_command(label="Open View", command=openview_file)
view_menu.add_command(label="Explorer", command=explorer_file)

def run_file():
    messagebox.showinfo("Run", "Run option selected.")

view_menu.add_command(label="Run", command=run_file)

menu_bar.add_cascade(label="View", menu=view_menu)


help_menu = tk.Menu(menu_bar, tearoff=0)

def about():
    messagebox.showinfo("About", "Simple Text Editor\nCreated with Tkinter.")

help_menu.add_command(label="Help", command=about)
menu_bar.add_cascade(label="About", menu=help_menu)


root.config(menu=menu_bar)

root.mainloop()