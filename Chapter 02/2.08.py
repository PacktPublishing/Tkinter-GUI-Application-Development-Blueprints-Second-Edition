"""
Code illustration: 2.08
A demonstration of tkinter.messagebox
showinfo
showwarning
showerror
askquestion
askokcancel
askyesno
askyesnocancel
askretrycancel

@Tkinter GUI Application Development Blueprints
"""


from tkinter import Tk, Frame, Label, Button, BOTH, LEFT

import tkinter.messagebox as tmb

root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side': LEFT, 'padx': 2, 'pady': 3}


# Demo of tkinter.messagebox
Label(fr1, text="Demo of tkinter.messagebox").pack()
Button(fr1, text='info', command=lambda: tmb.showinfo(
    "Show Info", "This is FYI")).pack(opt)
Button(fr1, text='warning', command=lambda: tmb.showwarning(
    "Show Warning", "Don't be silly")).pack(opt)
Button(fr1, text='error', command=lambda: tmb.showerror(
    "Show Error", "It leaked")).pack(opt)
Button(fr1, text='question', command=lambda: tmb.askquestion(
    "Ask Question", "Can you read this ?")).pack(opt)
Button(fr2, text='okcancel', command=lambda: tmb.askokcancel(
    "Ask OK Cancel", "Say Ok or Cancel?")).pack(opt)
Button(fr2, text='yesno', command=lambda: tmb.askyesno(
    "Ask Yes-No", "Say yes or no?")).pack(opt)
Button(fr2, text='yesnocancel', command=lambda: tmb.askyesnocancel(
    "Yes-No-Cancel", "Say yes no cancel")).pack(opt)
Button(fr2, text='retrycancel', command=lambda: tmb.askretrycancel(
    "Ask Retry Cancel", "Retry or what?")).pack(opt)


fr1.pack()
fr2.pack()

root.mainloop()
