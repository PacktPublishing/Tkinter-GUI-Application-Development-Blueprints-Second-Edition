"""
Code illustration: 10.11
    Reading from the command line
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Text, END
from subprocess import Popen, PIPE
root = Tk()
text = Text(root)
text.pack()
# replace "ls" with "dir" in the next line on windows platform
with Popen(["ls"], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    for line in p.stdout:
        text.insert(END, line)
root.mainloop()
