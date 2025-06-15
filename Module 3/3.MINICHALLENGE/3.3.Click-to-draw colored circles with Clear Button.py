import tkinter as tk
import random


def draw_circle(event):
    radius = 10
    x, y = event.x, event.y
    color = random.choice(["red", "green", "blue", "orange", "purple", "black"])
    canvas.create_oval(
        x - radius, y - radius, x + radius, y + radius,
        fill=color, outline=""
    )


def clear_canvas():
    canvas.delete("all")


root = tk.Tk()
root.title("Interactive Drawing Canvas")
root.geometry("854x480")


canvas = tk.Canvas(root, width=480, height=300, bg="white")
canvas.pack(padx=10, pady=10)

canvas.bind("<Button-1>", draw_circle)


tk.Button(root, text="Clear Canvas", command=clear_canvas).pack(pady=10)

root.mainloop()