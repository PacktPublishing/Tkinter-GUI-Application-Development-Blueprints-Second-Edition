"""
Code illustration: 3.10.py

    1. tkinter versus ttk Themed Widgets
    2. new widgets introduced in ttk

Chapter 3 : Programmable Drum Machine
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, Button, Label, Checkbutton, Entry, PanedWindow, \
            Radiobutton, Scale, VERTICAL, HORIZONTAL, W
from tkinter import ttk


root = Tk()

style = ttk.Style()

print(style.theme_names())

# style.theme_use('default')

root.title('Tkinter Versus ttk Themed Widgets')

ttk.Separator(root, orient=VERTICAL).grid(
    row=0, rowspan=8, column=1, sticky="wns")

Label(root, text='Tkinter    Versus').grid(row=0, columnspan=2, sticky='ew')
ttk.Label(root, text='ttk').grid(row=0, column=1)


Button(root, text='tk Button').grid(row=1, column=0)
ttk.Button(root, text='ttk Button').grid(row=1, column=1)


Checkbutton(root, text='tk CheckButton').grid(row=2, column=0)
ttk.Checkbutton(root, text='ttk CheckButton').grid(row=2, column=1)

Entry(root).grid(row=3, column=0)
ttk.Entry(root).grid(row=3, column=1)


PanedWindow(root).grid(row=4, column=0)
ttk.PanedWindow(root).grid(row=4, column=1)

Radiobutton(root, text='tk Radio').grid(row=5, column=0)
ttk.Radiobutton(root, text='ttk Radio').grid(row=5, column=1)


Scale(root, orient=HORIZONTAL).grid(row=6, column=0)
ttk.Scale(root).grid(row=6, column=1)

ttk.Separator(root, orient=HORIZONTAL).grid(row=7, columnspan=2, sticky="ew")
ttk.Label(root, text='NEW WIDGETS INTRODUCED IN ttk').grid(row=8, columnspan=2)
ttk.Separator(root, orient=HORIZONTAL).grid(row=9, columnspan=2, sticky="ew")

ttk.Combobox(root).grid(row=11, column=0)


my_notebook = ttk.Notebook(root)
my_notebook.grid(row=12, column=1)
frame_1 = ttk.Frame(my_notebook)
frame_2 = ttk.Frame(my_notebook)
my_notebook.add(frame_1, text='Tab One')
my_notebook.add(frame_2, text='Tab Two')

ttk.Progressbar(root, length=140, value=65).grid(row=13, column=0)

my_tree = ttk.Treeview(root, height=2, columns=2)
my_tree.grid(row=14, columnspan=2)
my_tree.heading('#0', text='Column A', anchor=W)
my_tree.heading(2, text='Column B', anchor=W)
my_tree.column(2, stretch=0, width=70)


root.mainloop()
