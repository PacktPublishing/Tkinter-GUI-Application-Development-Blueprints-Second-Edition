"""
Code illustration: 8.11
    Chaos Game
Tkinter GUI Application Development Blueprints
"""
import random
from tkinter import Tk, Canvas
import math


WIDTH = 800
HEIGHT = 500

v1 = (float(WIDTH/2), 0.0)
v2 = (0.00, float(HEIGHT))
v3 = (float(WIDTH), float(HEIGHT))


last_point = None

root = Tk()
canvas = Canvas(root, background="#660099", width = WIDTH, height = HEIGHT)
canvas.pack()

def midway_point(p1, p2):
    x = p1[0] + (p2[0] - p1[0]) //2
    y = p1[1] + (p2[1] - p1[1]) //2
    return (x,y)


def random_point_inside_triangle(v1, v2, v3):
    a = random.random()
    b = random.random()
    if a + b > 1:
        a = 1-a
        b = 1-b
    c = 1 - a -b
    x = (a*v1[0])+(b*v2[0])+(c*v3[0]);
    y = (a*v1[1])+(b*v2[1])+(c*v3[1]);
    return (x,y)

last_point = random_point_inside_triangle(v1, v2, v3)

def get_next_point():
    global last_point
    roll = random.choice(range(6))+1
    mid_point = None
    if roll == 1 or roll == 2:
      mid_point = midway_point(last_point, v1)
    elif roll == 3 or roll == 4:
      mid_point = midway_point(last_point, v2)
    elif roll == 5 or roll == 6:
      mid_point = midway_point(last_point, v3)
    last_point = mid_point
    return mid_point

def update():
   x,y  = get_next_point()
   canvas.create_rectangle(x, y, x, y, outline="#FFFF33")
   root.after(1, update)

update()
root.mainloop()
