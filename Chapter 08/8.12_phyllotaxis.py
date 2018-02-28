"""
Code illustration: 8.12
    Screensaver
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Canvas
import numpy as np
import random

width = 500
height = 500
number_of_dots = 2000
angle = 137.5
scaling_factor = 4
dot_size = 4
n = np.arange(number_of_dots)
r = np.zeros(number_of_dots)
phi = np.zeros(number_of_dots)
x = np.zeros(number_of_dots)
y = np.zeros(number_of_dots)
dots = []
colors = []

root = Tk()
canvas = Canvas(root, width=width, height=height, bg='grey6')
canvas.pack()

for i in n:
  r = (scaling_factor * np.sqrt(i) * 6) % 256
  color = '#%02x%02x%02x' % (int(r), 0, 0)
  colors.append(color)
  dots.append(
      canvas.create_oval(
          x[i] - dot_size,
          y[i] - dot_size,
          x[i] + dot_size,
          y[i] + dot_size,
          fill=color))


def update():
  global angle
  angle += 0.000001
  phi = angle * n
  r = scaling_factor * np.sqrt(n)
  x = r * np.cos(phi) + width / 2
  y = r * np.sin(phi) + height / 2
  for i in n:
    canvas.coords(dots[i], x[i] - dot_size, y[i] - dot_size, x[i] + dot_size,
                  y[i] + dot_size)
  root.after(15, update)


update()
root.mainloop()
