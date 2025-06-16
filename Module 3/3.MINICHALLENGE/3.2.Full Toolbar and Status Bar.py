import tkinter as tk

def open_file():
    status_label.config(text="Open clicked")

def save_file():
    status_label.config(text="Save clicked")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Toolbar and Status Bar Example")
root.geometry("854x480")


toolbar = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar, text="Open", command=open_file).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Save", command=save_file).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Exit", command=exit_app).pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill="x")


text_area = tk.Text(root)
text_area.pack(expand=True, fill="both")


status_label = tk.Label(root, text="Ready", bd=1, relief="sunken", anchor="w")
status_label.pack(side="bottom", fill="x")

root.mainloop()
