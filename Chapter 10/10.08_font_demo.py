"""
Code illustration: 10.08
        font Demo
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, Label, Pack, font

root = Tk()
label = Label(root, text="Humpty Dumpty was pushed")
label.pack()
current_font = font.Font(font=label['font'])
print ('Actual :', str(current_font.actual()))
print ('Family : ', current_font.cget("family"))
print ('Weight : ', current_font.cget("weight"))
print ('Text width of Dumpty : {}'.format(current_font.measure("Dumpty")))
print ('Metrics:', str(current_font.metrics()))
current_font.config(size=14)
label.config(font=current_font)
print ('New Actual :', str(current_font.actual()))
root.mainloop()
