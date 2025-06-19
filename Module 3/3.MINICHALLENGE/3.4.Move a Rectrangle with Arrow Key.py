
import tkinter as tk


MOVE_AMOUNT = 10

def move_up(event):
    canvas.move(rect_id, 0, -MOVE_AMOUNT)

def move_down(event):
    canvas.move(rect_id, 0, MOVE_AMOUNT)

def move_left(event):
    canvas.move(rect_id, -MOVE_AMOUNT, 0)

def move_right(event):
    canvas.move(rect_id, MOVE_AMOUNT, 0)


root = tk.Tk()
root.title("Move Shape with Arrow Keys")
root.geometry("854x480")


canvas = tk.Canvas(root, width=600, height=400, bg="pink")
canvas.pack()


rect_id = canvas.create_rectangle(100, 100, 110, 110, fill="blue")


root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)


canvas.focus_set()

root.mainloop()
