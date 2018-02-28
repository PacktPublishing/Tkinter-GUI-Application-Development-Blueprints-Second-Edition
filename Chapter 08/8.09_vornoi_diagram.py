"""
Code illustration: 8.09
    Vornoi Diagrams
     *** Warnig - this code takes up to a few minutes to compute ***

Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Canvas
import random
import math

width = 800
height = 500
number_of_attractor_points = 125


def create_voronoi_diagram(canvas, w, h, number_of_attractor_points):
  attractor_points = []
  colors = []
  for i in range(number_of_attractor_points):
    attractor_points.append((random.randrange(w), random.randrange(h)))
    colors.append('#%02x%02x%02x' % (random.randrange(256),
                                     random.randrange(256),
                                     random.randrange(256)))
  for y in range(h):
    for x in range(w):
      minimum_distance = math.hypot(w , h )
      index_of_nearest_attractor_point = -1
      for i in range(number_of_attractor_points):
        distance = math.hypot(attractor_points[i][0] - x, attractor_points[i][1] - y)
        if distance < minimum_distance:
          minimum_distance = distance
          index_of_nearest_attractor_point = i
      canvas.create_rectangle([x, y, x, y],
                        fill=colors[index_of_nearest_attractor_point], width=0)
  for point in attractor_points:
    x, y = point
    dot = [x - 1, y - 1, x + 1, y + 1]
    canvas.create_rectangle(dot, fill='blue', width=1)


root = Tk()
canvas = Canvas(root, height=height, width=width)
canvas.pack()
create_voronoi_diagram(canvas, width, height, number_of_attractor_points)
root.mainloop()
