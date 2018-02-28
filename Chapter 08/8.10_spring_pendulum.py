"""
Code illustration: 8.10
    Spring Pendulum Simulation
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Canvas
import numpy as np
from scipy.integrate import odeint

UNSTRETCHED_SPRING_LENGHT = 30
SPRING_CONSTANT = 0.1
MASS = 0.3
GRAVITY = 9.8
NUMBER_OF_STEPS_IN_SIMULATION = 500

state_vector = [1, 1, 2, 1]
# 4 values represent 'l', 'dl/dt', 'θ', 'dθ/dt' respectively
# i;e 'spring_length', 'dl/dt - velocity', 'angle', 'anglular velocity'


def differential_functions(state_vector, time):
  func1 = state_vector[1]
  func2 = (UNSTRETCHED_SPRING_LENGHT + state_vector[0]
           ) * state_vector[3]**2 - (SPRING_CONSTANT / MASS * state_vector[0]
                                     ) + GRAVITY * np.cos(state_vector[2])
  func3 = state_vector[3]
  func4 = -(GRAVITY * np.sin(state_vector[2]) +
            2.0 * state_vector[1] * state_vector[3]) / (
                UNSTRETCHED_SPRING_LENGHT + state_vector[0])
  return np.array([func1, func2, func3, func4])


time = np.linspace(0, 37, NUMBER_OF_STEPS_IN_SIMULATION)
ode_solution = odeint(differential_functions, state_vector, time)

x_coordinates = (UNSTRETCHED_SPRING_LENGHT + ode_solution[:, 0]) * np.sin(
    ode_solution[:, 2])
y_coordinates = (UNSTRETCHED_SPRING_LENGHT + ode_solution[:, 0]) * np.cos(
    ode_solution[:, 2])


w = 250
h = 300
plot_step = 0

root = Tk()
canvas = Canvas(root, bg="LemonChiffon3", height=h, width=w)
canvas.pack(side='left')


def update_graph():
  global plot_step
  if plot_step == NUMBER_OF_STEPS_IN_SIMULATION: # simulation ended
    plot_step = 0 # repeat the simulation
  x, y = int(
      x_coordinates[plot_step]) + w / 2, int(y_coordinates[plot_step] + h / 2)
  canvas.delete('all')
  canvas.create_line(w / 2, 0, x, y, dash=(2, 1), width=1, fill="gold4")
  canvas.create_oval(
      x - 10, y - 10, x + 10, y + 10, outline="gold4", fill="lavender")
  plot_step = plot_step + 1
  root.after(15, update_graph)


update_graph()

root.mainloop()
