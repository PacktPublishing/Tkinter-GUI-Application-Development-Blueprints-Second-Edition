"""
Code illustration: 2.06
A demonstration of different types of top-level window

@Tkinter GUI Application Development Blueprints
"""


from tkinter import Tk, Label, Toplevel

root = Tk()

# top level window
root.title('Toplevel Window')
root.geometry('300x300')
Label(root, text='I am the Main Toplevel window\n All other windows here are my children').pack()


# child toplevel
child_toplevel = Toplevel(root)
Label(child_toplevel, text='I am a child of root\n If i loose focus, I may hide below the top level, \n I am destroyed, if root is destroyed').pack()
child_toplevel.geometry('400x100+300+300')


# transient window
transient_toplevel = Toplevel(root)
Label(transient_toplevel, text='I am a transient window of root\n I always stay on top of my parent\n I get hidden if my parent window is minimized').pack()
transient_toplevel.transient(root)


# no window decoration
no_window_decoration = Toplevel(root, bg='black')
Label(no_window_decoration, text='I am a top-level with no window manager\n I cannot be resized or moved',
      bg='black', fg='white').pack()
no_window_decoration.overrideredirect(1)
no_window_decoration.geometry('250x100+700+500')


root.mainloop()
