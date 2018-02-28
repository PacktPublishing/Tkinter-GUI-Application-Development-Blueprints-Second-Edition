"""
Code illustration: 8.08
    Mandelbrot Set
    *** This may take some time to compute ***
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Canvas
import math

image_width = 512
image_height = 512
max_number_of_iterations = 50
min_real, max_real, min_imaginary, max_imaginary = -1.5, 0.7, -1.0, 1.0

root = Tk()
canvas = Canvas(root, height=image_height, width=image_width)
canvas.pack()

def mandelbrot_set_check(real, imaginary):
  iteration_count = 0
  z_real = 0.0
  z_imaginary = 0.0
  while iteration_count < max_number_of_iterations and \
        z_real * z_real + z_imaginary * z_imaginary < 4.0:
    temp = z_real * z_real - z_imaginary * z_imaginary + real
    z_imaginary = 2.0 * z_real * z_imaginary + imaginary
    z_real = temp
    iteration_count += 1
  return iteration_count


def get_color(num_iterations):
  if num_iterations == max_number_of_iterations:
    r,g,b = (0, 0, 0)
  elif num_iterations < max_number_of_iterations//8:
    r,g,b = (num_iterations * 2)%255, 0, 0
  elif num_iterations < max_number_of_iterations//7:
    r,g,b = (num_iterations * 4) % 255, 0, 0
  elif num_iterations < max_number_of_iterations//6:
    r,g,b = (num_iterations * 8) % 255, 0, 0
  elif (num_iterations < max_number_of_iterations//5):
    r,g,b = 255, (num_iterations * 16) % 255 , 0
  elif (num_iterations < max_number_of_iterations//4):
    r,g,b = 255, (num_iterations * 64) % 255, 0
  elif (num_iterations < max_number_of_iterations//3):
    r,g,b = 255, (num_iterations * 128) % 255, 0
  elif (num_iterations < max_number_of_iterations//2):
    r,g,b = (255, (num_iterations * 256) % 255 , 0)
  else:
    r, g, b = (255, 255, 0)
  rgb = '#%02x%02x%02x' % (r, g, b)
  return rgb


def map_pixels_to_real(x):
  real_range = max_real - min_real
  return x * (real_range / image_width) + min_real


def map_pixels_to_imaginary(y):
  imaginary_range = max_imaginary - min_imaginary
  return y * (imaginary_range / image_height) + min_imaginary


for y in range(image_height):
  for x in range(image_width):
    real = map_pixels_to_real(x)
    imaginary = map_pixels_to_imaginary(y)
    num_iterations = mandelbrot_set_check(real, imaginary)
    rgb = get_color(num_iterations)
    canvas.create_rectangle([x, y, x, y], fill=rgb, width=0)


root.mainloop()
