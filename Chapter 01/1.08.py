"""
Code illustration: 1.08
A demonstration of common place() options

@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
root = tk.Tk()
# Absolute positioning
tk.Button(root, text="Absolute Placement").place(x=20, y=10)
# Relative positioning
tk.Button(
    root, text="Relative").place(
        relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor=tk.NE)
root.mainloop()
