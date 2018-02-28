"""
Code illustration: 1.07
A demonstration of grid() geometry manager options
@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
parent = tk.Tk()
parent.title('Find & Replace')

tk.Label(parent, text="Find:").grid(row=0, column=0, sticky='e')
tk.Entry(parent, width=60).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)

tk.Label(parent, text="Replace:").grid(row=1, column=0, sticky='e')
tk.Entry(parent).grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=9)

tk.Button(parent, text="Find").grid(row=0, column=10, sticky='e'+'w', padx=2, pady=2)
tk.Button(parent, text="Find All").grid(row=1, column=10, sticky='e'+'w', padx=2)
tk.Button(parent, text="Replace").grid(row=2, column=10, sticky='e'+'w', padx=2)
tk.Button(parent, text="Replace All").grid(row=3, column=10, sticky='e'+'w', padx=2)


tk.Checkbutton(parent, text='Match whole word only ').grid(row =2, column=1, columnspan=4,sticky='w')
tk.Checkbutton(parent, text='Match Case').grid(row =3, column=1, columnspan=4,sticky='w')
tk.Checkbutton(parent, text='Wrap around').grid(row =4, column=1, columnspan=4,sticky='w')



tk.Label(parent, text="Direction:").grid(row=2, column=6,sticky='w')
tk.Radiobutton(parent, text='Up',  value=1).grid(row=3, column=6, columnspan=6, sticky='w')
tk.Radiobutton(parent, text='Down',  value=2).grid(row=3, column=7,columnspan=2, sticky='e')


parent.mainloop()
