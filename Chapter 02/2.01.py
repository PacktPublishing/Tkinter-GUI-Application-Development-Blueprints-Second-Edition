"""
Code illustration: 2.01
Text Editor Code
Step 1: Adding Top-level
Step 2: Add Menubuttons

@Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Menu


PROGRAM_NAME = "Footprint Editor"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

menu_bar = Menu(root)  # menu begins

file_menu = Menu(menu_bar, tearoff=0)
# all file menu-items will be added here next
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About',  menu=about_menu)

root.config(menu=menu_bar)  # menu ends

root.mainloop()
