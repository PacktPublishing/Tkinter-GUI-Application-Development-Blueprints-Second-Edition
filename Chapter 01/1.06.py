"""
Code illustration: 1.06
Simple example of grid Geometry Manager

@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
root = tk.Tk()
tk.Label(root, text="Username").grid(row=0, sticky=tk.W)
tk.Label(root, text="Password").grid(row=1, sticky=tk.W)
tk.Entry(root).grid(row=0, column=1, sticky=tk.E)
tk.Entry(root).grid(row=1, column=1, sticky=tk.E)
tk.Button(root, text="Login").grid(row=2, column=1, sticky=tk.E)
root.mainloop()
