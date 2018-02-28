"""
Code illustration: 1.11
A demonstration of tkinter Variable Class
IntVar, StringVar & BooleanVar

@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
root = tk.Tk()

def show():
    print( "You entered:")
    print( "Employee Number: "+ str(employee_number.get()))
    print( "Login Password: "+ password.get())
    print( "Remember Me: "+ str(remember_me.get()))
    print( '*'*30)

#demo of IntVar
tk.Label(root, text="Employee Number:").grid(row=1, column=1)
employee_number = tk.IntVar()
tk.Entry(root, width=40, textvariable=employee_number).grid(row=1, column=2, columnspan=2)
employee_number.set("120350")


#demo of StringVar
tk.Label(root, text="Login Password:").grid(row=2, column=1, sticky='w')
password = tk.StringVar() # defines the widget state as string
tk.Entry(root,width=40, show="*",  textvariable=password).grid(row=2, column=2, columnspan=2)
password.set("mysecretpassword")

tk.Button(root,text="Login", command=show).grid(row=3, column=3)

#demo of Boolean var
remember_me = tk.BooleanVar()
tk.Checkbutton(root, text="Remember Me", variable=remember_me).grid(row=3, column=2)
remember_me.set(True)



root.mainloop()
