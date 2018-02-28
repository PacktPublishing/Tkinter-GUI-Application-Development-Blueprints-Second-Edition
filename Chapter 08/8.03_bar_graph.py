"""
Code illustration: 8.03 
    Bar graph
Tkinter GUI Application Development Blueprints
"""

import tkinter
import random

root = tkinter.Tk()

canvas_width = 250
canvas_height = 220
bar_width = 20

canv = tkinter.Canvas(
    root, width=canvas_width, height=canvas_height, bg='white')
canv.pack()

plot_data = [random.randint(75, 200) for r in range(12)]

for x, y in enumerate(plot_data):
    x1 = x + x * bar_width
    y1 = canvas_height - y
    x2 = x + x * bar_width + bar_width
    y2 = canvas_height
    canv.create_rectangle(x1, y1, x2, y2, fill="blue")
    canv.create_text(x1 + 3, y1, font=("", 6), text=str(y), anchor='sw')

root.mainloop()
