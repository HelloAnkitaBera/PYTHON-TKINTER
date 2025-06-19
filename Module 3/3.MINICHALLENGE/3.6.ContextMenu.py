import tkinter as tk

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)


root = tk.Tk()
root.title("Text Editor with Right-Click Menu")
root.geometry("854x480")


text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both", padx=10, pady=10)


context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut", command=lambda: text_widget.event_generate("<<Cut>>"))
context_menu.add_command(label="Copy", command=lambda: text_widget.event_generate("<<Copy>>"))
context_menu.add_command(label="Paste", command=lambda: text_widget.event_generate("<<Paste>>"))


text_widget.bind("<Button-3>", show_context_menu)

root.mainloop()
