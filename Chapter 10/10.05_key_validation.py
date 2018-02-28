"""
Code illustration: 10.05
validate='key' demo
Tkinter GUI Application Development Blueprints
"""

import tkinter as tk


class KeyValidationDemo():

    def __init__(self):
        root = tk.Tk()
        tk.Label(
            root, text='Enter your name / only alpabets & space allowed').pack()
        vcmd = (root.register(self.validate_data), '%S')
        invcmd = (root.register(self.invalid_name), '%S')
        tk.Entry(root, validate="key", validatecommand=vcmd,
                 invalidcommand=invcmd).pack(pady=5, padx=5)
        self.error_message = tk.Label(root, text='', fg='red')
        self.error_message.pack()
        root.mainloop()

    def validate_data(self, S):
        print("S={}".format(S))
        self.error_message.config(text='')
        return (S.isalpha() or S == ' ')

    def invalid_name(self, S):
        self.error_message.config(
            text='Invalid character %s \n name can only have alphabets and spaces' % S)

app = KeyValidationDemo()
