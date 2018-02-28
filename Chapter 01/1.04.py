"""
Code illustration: 1.04
A demonstration of some of pack() options
Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
root = tk.Tk()

frame = tk.Frame(root)
# demo of side and fill options
tk.Label(frame, text="Pack Demo of side and fill").pack()
tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="C").pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text="D").pack(side=tk.TOP, fill=tk.BOTH)
frame.pack()  # note the top frame does not expand nor does it fill in
#X or Y directions

# demo of expand options - best understood by expanding the root widget
# and seeing the effect on all the three buttons below.
tk.Label(root, text="Pack Demo of expand").pack()
tk.Button(root, text="I do not expand").pack()
tk.Button(root, text="I do not fill x but I expand").pack(expand=1)
tk.Button(root, text="I fill x and expand").pack(fill=tk.X, expand=1)

root.mainloop()
