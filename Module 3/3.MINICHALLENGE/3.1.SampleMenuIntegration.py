import tkinter as tk
from tkinter import messagebox

def about():
    messagebox.showinfo("About", "This is a sample Tkinter app")

root = tk.Tk()
root.title("Menu Demo")
root.geometry("854x480")

menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Open View")
view_menu.add_command(label="Explorer")
menu_bar.add_cascade(label="View", menu=view_menu)

# Help Menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
