import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    filepath = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if filepath:
        try:
            with open(filepath, "r") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file:\n{e}")
    else:
        messagebox.showwarning("No Selection", "No file was selected.")

def clear_text():
    confirm = messagebox.askyesno("Confirm Clear", "Are you sure you want to clear the text?")
    if confirm:
        text_area.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("File Reader")
root.geometry("854x480")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Browse File", command=browse_file).pack(side="left", padx=10)
tk.Button(button_frame, text="Clear", command=clear_text).pack(side="left", padx=10)

# Text widget to show file contents
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)



root.mainloop()
