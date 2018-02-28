"""
Code illustration: 1.12
A demonstration of tkinter styling

@Tkinter GUI Application Development Blueprints
"""

import tkinter as tk
root = tk.Tk()
root.configure(background='#4D4D4D')  #top level styling

# connecting to the external styling optionDB.txt
root.option_readfile('optionDB.txt')

#widget specific styling
text = tk.Text(
    root,
    background='#101010',
    foreground="#D6D6D6",
    borderwidth=18,
    relief='sunken',
    width=17,
    height=5)
text.insert(
    tk.END,
    "Style is knowing who you are,what you want to say, and not giving a damn."
)
text.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

# all the below widgets derive their styling from optionDB.txt file
tk.Button(root, text='*').grid(row=1, column=1)
tk.Button(root, text='^').grid(row=1, column=2)
tk.Button(root, text='#').grid(row=1, column=3)
tk.Button(root, text='<').grid(row=2, column=1)
tk.Button(
    root, text='OK', cursor='target').grid(
        row=2, column=2)  #changing cursor style
tk.Button(root, text='>').grid(row=2, column=3)
tk.Button(root, text='+').grid(row=3, column=1)
tk.Button(root, text='v').grid(row=3, column=2)
tk.Button(root, text='-').grid(row=3, column=3)
for i in range(10):
  tk.Button(
      root, text=str(i)).grid(
          column=3 if i % 3 == 0 else (1 if i % 3 == 1 else 2),
          row=4 if i <= 3 else (5 if i <= 6 else 6))

root.mainloop()
