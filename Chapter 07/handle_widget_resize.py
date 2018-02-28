'''

Chapter 7

Handling Widget Resize


'''


from tkinter import Tk, Label, Pack

root= Tk()

label  = Label(root, text = 'I am a Frame', bg='red')
label.pack(fill='both', expand=True)


def on_label_resized(event):
    print('New Width', label.winfo_width())
    print('New Height', label.winfo_height())


label.bind("<Configure>", on_label_resized)

root.mainloop()
