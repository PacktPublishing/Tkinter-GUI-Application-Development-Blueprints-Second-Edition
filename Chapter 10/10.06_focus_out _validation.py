"""
Code illustration: 10.06
validate='focusout' demo
Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
import re


class FocusOutValidationDemo():

    def __init__(self):
        self.master = tk.Tk()
        self.error_message = tk.Label(text='', fg='red')
        self.error_message.pack()
        tk.Label(text='Enter Email Address').pack()
        vcmd = (self.master.register(self.validate_email), '%P')
        invcmd = (self.master.register(self.invalid_email), '%P')
        self.email_entry = tk.Entry(
            self.master, validate="focusout", validatecommand=vcmd, invalidcommand=invcmd)
        self.email_entry.pack()
        tk.Button(self.master, text="Login").pack()
        tk.mainloop()

    def validate_email(self, P):
        self.error_message.config(text='')
        x = re.match(r"[^@]+@[^@]+\.[^@]+", P)
        return (x != None)

    def invalid_email(self, P):
        self.error_message.config(text='Invalid Email Address')
        self.email_entry.focus_set()

app = FocusOutValidationDemo()
