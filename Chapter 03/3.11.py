"""
Code illustration: 3.11.py
    ttk widgets styling and theming explained

Chapter 3 : Programmable Drum Machine
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk
from tkinter import ttk
root = Tk()

style = ttk.Style()
# defining the global style - applied when no other style is defined
style.configure('.', font='Arial 14', foreground='brown', background='yellow')
# this label inherits the global style as style option not specified for it
ttk.Label(root, text='I have no style of my own').pack()
# defining a new style named danger and configuring its style only for the
# button widget
style.configure('danger.TButton', font='Times 12', foreground='red', padding=1)
ttk.Button(root, text='Styled Dangerously', style='danger.TButton').pack()
# Different  styling for different widget states
style.map("new_state_new_style.TButton", foreground=[
          ('pressed', 'red'), ('active', 'blue')])
ttk.Button(text="Different Style for different states",
           style="new_state_new_style.TButton").pack()
# Overriding current theme styles for the Entry widget
current_theme = style.theme_use()
style.theme_settings(
    current_theme,
    {"TEntry":
     {"configure":
      {"padding": 10},
      "map": {
          "foreground": [("focus", "red")]
      }
      }
     }
)
print(style.theme_names())
print(style.theme_use())
# this is effected by change of themes even though no style specified
ttk.Entry().pack()
root.mainloop()
