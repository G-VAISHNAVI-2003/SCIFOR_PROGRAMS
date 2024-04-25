import tkinter as tk
from tkinter import colorchooser

# Global variables
tool = "pen"
color = "black"
size = 2

# Function to handle pen tool
def pen():
    global tool
    tool = "pen"

# Function to handle brush tool
def brush():
    global tool
    tool = "brush"

# Function to handle eraser tool
def eraser():
    global tool
    tool = "eraser"

# Function to choose color
def pick_color():
    global color
    c = colorchooser.askcolor()
    if c:
        color = c[1]

# Function to change brush/pen size
def set_size(val):
    global size
    size = int(val)

# Function to paint on canvas
def paint(event):
    x1, y1 = (event.x - size), (event.y - size)
    x2, y2 = (event.x + size), (event.y + size)
    if tool == "pen":
        canvas.create_line(x1, y1, x2, y2, fill=color, width=size*2)
    elif tool == "brush":
        canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    elif tool == "eraser":
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")

# Main tkinter window
root = tk.Tk()
root.title("Simple Paint")

# Canvas
canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

# Pen button
pen_button = tk.Button(root, text="Pen", command=pen)
pen_button.pack(side=tk.LEFT)

# Brush button
brush_button = tk.Button(root, text="Brush", command=brush)
brush_button.pack(side=tk.LEFT)

# Color button
color_button = tk.Button(root, text="Color", command=pick_color)
color_button.pack(side=tk.LEFT)

# Eraser button
eraser_button = tk.Button(root, text="Eraser", command=eraser)
eraser_button.pack(side=tk.LEFT)

# Size slider
size_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Size", command=set_size)
size_slider.pack(side=tk.LEFT)

# Binding mouse motion event to paint function
canvas.bind("<B1-Motion>", paint)

# Start the Tkinter event loop
root.mainloop()
