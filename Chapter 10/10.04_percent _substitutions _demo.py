"""
Code illustration: 10.04

Demonstration of percent substitutions in data validation
Tkinter GUI Application Development Blueprints
"""

import tkinter as tk


class PercentSubstitutionsDemo():

    def __init__(self):
        self.root = tk.Tk()
        tk.Label(text='Type Something Below').pack()
        vcmd = (self.root.register(self.validate), '%d',
                '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        tk.Entry(self.root, validate="all", validatecommand=vcmd).pack()
        self.root.mainloop()

    def validate(self, d, i, P, s, S, v, V, W):
        print("Following Data is received for running our validation checks:")
        print("d:{}".format(d))
        print("i:{}".format(i))
        print("P:{}".format(P))
        print("s:{}".format(s))
        print("S:{}".format(S))
        print("v:{}".format(v))
        print("V:{}".format(V))
        print("W:{}".format(W))
        # returning true for now
        # in actual validation you return true if data is valid else return
        # false
        return True

app = PercentSubstitutionsDemo()
