"""
Code illustration: 8.05
    Embedding Matplotlib graph on tkinter
Tkinter GUI Application Development Blueprints
"""

import tkinter as tk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

root = tk.Tk()

# creating the graph
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(-1.0, 1.0, 0.001)
s = t * sin(1 / t)
a.plot(t, s)

# embedding matplotlib figure f on a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# creating toolbar
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()

root.mainloop()
