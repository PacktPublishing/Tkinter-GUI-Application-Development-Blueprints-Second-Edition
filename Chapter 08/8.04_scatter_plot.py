"""
Code illustration: 8.04
    Scatter Plot

Tkinter GUI Application Development Blueprints
"""

import tkinter
import random
root = tkinter.Tk()


def motion(event):
    x, y = event.x, event.y
    print("canvas x,y", '{}, {}'.format(x, y))
    print("plot xy", '{}, {}'.format(x - 50, 250 - y))

root.bind('<Motion>', motion)

c = tkinter.Canvas(root, width=350, height=280, bg='white')
c.grid()

# create x-axis
c.create_line(50, 250, 300, 250, width=3)
for i in range(12):
    x = 50 + (i * 20)
    c.create_text(x, 255, font=("", 6), anchor='n', text='{}'.format(20 * i))


# y-axis
c.create_line(50, 250, 50, 20, width=3)
for i in range(12):
    y = 250 - (i * 20)
    c.create_text(45, y, font=("", 6), anchor='e', text='{}'.format(20 * i))


# create scatter plots from random x-y values
for i in range(35):
    x, y = random.randint(0, 160) + 50, 250 - random.randint(50, 220)
    c.create_oval(x - 3, y - 3, x + 3, y + 3, width=1, fill='red')


root.mainloop()
