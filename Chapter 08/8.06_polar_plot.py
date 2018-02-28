"""
Code illustration: 8.06
    Polar Plot
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, Canvas, W
import math

width = 400
height = 400
x_center = width //2
y_center = height//2
scaling_factor  = 60

def polar_to_cartesian(r, theta, scaling_factor, x_center, y_center):
  x = r * math.cos(theta) * scaling_factor + x_center
  y = r * math.sin(theta) * scaling_factor + y_center
  return(x, y)

root = Tk()
root.title("Polar Plot Demo")
c = Canvas(width=width, height=height, bg='white')
c.pack()

# draw radial lines at interval of 15 degrees
for theta in range(0,360,15):
  r = 180
  x, y = x_center + math.cos(math.radians(theta))*r, \
         y_center - math.sin(math.radians(theta)) *r
  c.create_line(x_center, y_center, x, y, fill='green', dash=(2, 4),\
                activedash=(6, 5, 2, 4) )
  c.create_text(x, y, anchor=W, font="Purisa 8", text=str(theta) + '°')

# draw concentric_circles
for radius in range(1,4):
   x_max = x_center + radius * scaling_factor
   x_min = x_center - radius * scaling_factor
   y_max = y_center + radius * scaling_factor
   y_min = y_center - radius * scaling_factor
   c.create_oval(x_max, y_max, x_min, y_min, width=1, outline='grey', \
                 dash=(2, 4), activedash=(6, 5, 2, 4))


for theta in range(0, 3000):
  r = 2*math.sin(2*theta)
  # a few equations that look good on polar plot -
  # uncomment one line at a time to see the individual plots
  # also change parameters of equations to see their effect on the plots
  # r = 0.0006 * theta
  #r = 1 + 2*math.cos(theta)
  #r = 3 * math.cos(theta)
  #r = 2*math.sin(5*theta)
  #r = 2 * math.cos(3*theta)
  #r = 2 * math.sin(theta)**2
  #r = (4 * math.sin(2*theta))**1/2
  #r = (4 * math.cos(2*theta))**1/2
  x, y = polar_to_cartesian(r, theta, scaling_factor, x_center, y_center)
  c.create_oval(x, y, x, y, width=1, outline='navy')

root.mainloop()
