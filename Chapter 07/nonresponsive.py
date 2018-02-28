'''
Chapter 7
A note on responsiveness

This is an example of nonresponsive widgets
Run this program and resize the window. 
Notice that the buttons remain fixed in size.
If the window size is made smaller, some of the buttons disappear from view

'''
from tkinter import Tk, Button

root = Tk()

for x in range(10):
    btn = Button(root, text=x )
    btn.grid(column=x, row=1, sticky='nsew')

root.mainloop()
