"""
Code illustration: 1.05
Where to use pack() options

@Tkinter GUI Application Development Blueprints
"""

import tkinter as tk
root = tk.Tk()
parent = tk.Frame(root)

#placing widgets top-down
tk.Button(parent, text='ALL IS WELL').pack(fill=tk.X)
tk.Button(parent, text='BACK TO BASICS').pack(fill=tk.X)
tk.Button(parent, text='CATCH ME IF U CAN').pack(fill=tk.X)
#placing widgets side by side
tk.Button(parent, text='LEFT').pack(side=tk.LEFT)
tk.Button(parent, text='CENTER').pack(side=tk.LEFT)
tk.Button(parent, text='RIGHT').pack(side=tk.LEFT)
parent.pack()
root.mainloop()
