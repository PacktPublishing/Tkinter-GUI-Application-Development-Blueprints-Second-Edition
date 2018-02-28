'''

Chapter 7

A demonstration of a responsive window
using Grid.rowconfigure and Grid.columnconfigure

'''
from tkinter import Tk, Button, Grid

root = Tk()

for x in range(10):
    btn = Button(root, text=x )
    btn.grid(column=x, row=1, sticky='nsew')
    Grid.rowconfigure(root, 2, weight=x)
    Grid.columnconfigure(root, 2, weight=x)


root.mainloop()
