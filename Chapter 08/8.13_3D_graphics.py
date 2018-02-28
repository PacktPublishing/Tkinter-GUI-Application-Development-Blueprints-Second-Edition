"""
Code illustration: 8.13_3D_graphics
    3D Graphics
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, Canvas, BOTH, YES,ALL
from math import *


class MatrixHelpers:
  def transpose_matrix(self, matrix):
    return list(zip(*matrix))

  def translate_vector(self, x, y, dx, dy):
    return x + dx, y + dy

  def matrix_multiply(self, matrix_a, matrix_b):
    zip_b = list(zip(*matrix_b))
    return [[
        sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
        for col_b in zip_b
    ] for row_a in matrix_a]

  def rotate_along_x(self, x, shape):
    return self.matrix_multiply(
        [[1, 0, 0], [0, cos(x), -sin(x)], [0, sin(x), cos(x)]], shape)

  def rotate_along_y(self, y, shape):
    return self.matrix_multiply(
        [[cos(y), 0, sin(y)], [0, 1, 0], [-sin(y), 0, cos(y)]], shape)

  def rotate_along_z(self, z, shape):
    return self.matrix_multiply(
        [[cos(z), sin(z), 0], [-sin(z), cos(z), 0], [0, 0, 1]], shape)


class Cube(MatrixHelpers):

  last_x = 0
  last_y = 0
  fg_color = 'red'
  bg_color = 'khaki'

  def __init__(self, root):
    self.root = root
    self.init_data()
    self.create_canvas()
    self.draw_cube()
    self.bind_mouse_buttons()
    self.continually_rotate()
    self.epsilon = lambda d: d * 0.01

  def init_data(self):
    self.cube = self.transpose_matrix([[-100, -100, -100], [-100, 100, -100], [
        -100, -100, 100
    ], [-100, 100, 100], [100, -100, -100], [100, 100, -100], [100, -100, 100],
                                       [100, 100, 100]])

  def create_canvas(self):
    self.canvas = Canvas(
        self.root, width=400, height=400, background=self.bg_color)
    self.canvas.pack(fill=BOTH, expand=YES)

  def bind_mouse_buttons(self):
    self.canvas.bind("<Button-1>", self.on_mouse_clicked)
    self.canvas.bind("<B1-Motion>", self.on_mouse_motion)

  def draw_cube(self):
    cube_points = [[0, 1, 2, 4], [3, 1, 2, 7], [5, 1, 4, 7], [6, 2, 4, 7]]
    w = self.canvas.winfo_width() / 2
    h = self.canvas.winfo_height() / 2
    self.canvas.delete(ALL)
    for i in cube_points:
      for j in i:
        self.canvas.create_line(
            self.translate_vector(self.cube[0][i[0]], self.cube[1][i[0]], w,
                                  h),
            self.translate_vector(self.cube[0][j], self.cube[1][j], w, h),
            fill=self.fg_color)

  def continually_rotate(self):
    self.cube = self.rotate_along_x(0.01, self.cube)
    self.cube = self.rotate_along_y(0.01, self.cube)
    self.cube = self.rotate_along_z(0.01, self.cube)
    self.draw_cube()
    self.root.after(15, self.continually_rotate)

  def on_mouse_clicked(self, event):
    self.last_x = event.x
    self.last_y = event.y

  def on_mouse_motion(self, event):
    dx = self.last_y - event.y
    self.cube = self.rotate_along_x(self.epsilon(-dx), self.cube)
    dy = self.last_x - event.x
    self.cube = self.rotate_along_y(self.epsilon(dy), self.cube)
    self.draw_cube()
    self.on_mouse_clicked(event)


def main():
  root = Tk()
  Cube(root)
  root.mainloop()


if __name__ == '__main__':
  main()
