"""
Code illustration: 10.02
Widget Traversal
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Text, NSEW, Frame,Entry, Button, Radiobutton, Scale, X,\
        Label, END, HORIZONTAL


class TraversalDemo:

    def __init__(self, root):
        frame = Frame(
            root, takefocus=1, highlightthickness=2, highlightcolor='red')
        entry = Entry(frame)
        entry.pack(fill=X, expand=1)
        entry.insert(END, 'Tabs jumps to next widget')
        frame.pack(fill=X, expand=1)
        frame.focus_force()

        frame = Frame(root, highlightthickness=2,  highlightcolor='red')
        for button_text, column_number in (('A', 1), ('B', 2), ('C', 3), ('D', 4)):
            Button(frame, text=button_text, highlightthickness=2).grid(
                padx=10, pady=6, row=0, column=column_number, sticky=NSEW)
        frame.pack(fill=X, expand=1)

        frame = Frame(
            root, takefocus=1, highlightthickness=2,  highlightcolor='red')
        for i in range(4):
            Radiobutton(frame, text=i, value=i).grid(
                padx=10, pady=6, row=1, column=i, sticky=NSEW)
        frame.pack(fill=X, expand=1)

        frame = Frame(
            root, takefocus=1, highlightthickness=2,  highlightcolor='red')
        text = Text(frame, height=4)
        text.insert(
            END, 'Tabs does not jump to the next widget from inside the Text widget.\nUse Ctrl + Tab to traverse')
        text.grid(row=0, column=1, columnspan=3)
        frame.pack(fill=X, expand=1)

        frame = Frame(root, takefocus=0)
        Label(frame, text='use left/right key').pack()
        Scale(frame, from_=0.0, to=100.0, orient=HORIZONTAL, takefocus=1,
              highlightthickness=2,  highlightcolor='red').pack()
        frame.pack(fill=X, expand=1)


root = Tk()
app = TraversalDemo(root)
root.mainloop()
