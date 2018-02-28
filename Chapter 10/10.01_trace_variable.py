"""
Code illustration: 10.01
Tkinter Trace Variable Demo
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, Label, Entry, StringVar
root = Tk()

my_variable = StringVar()


def trace_when_my_variable_written(var, indx, mode):
    print ("Traced variable {}".format(my_variable.get()))

my_variable.trace_variable("w", trace_when_my_variable_written)


Label(root, textvariable=my_variable).pack(padx=5, pady=5)
Entry(root, textvariable=my_variable).pack(padx=5, pady=5)


root.mainloop()
