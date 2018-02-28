"""
Code illustration: 1.10
A demonstration of events and the information available in it.

@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk

def show_event_details(event):
  print('='*50)
  print("EventKeySymbol=" + str(event.keysym))
  print("EventType=" + str(event.type))
  print("EventWidgetId=" + str(event.widget))
  print("EventCoordinate (x,y)=(" + str(event.x)+","+str(event.y)+")")
  print("Time:", str(event.time))

root = tk.Tk()

button = tk.Button(root, text="tk.Button Bound to: \n Keyboard Enter & Mouse Click") #create button
button.pack(pady=5,padx=4)
button.focus_force()
button.bind("<Button-1>", show_event_details)  #bind button to mouse click
button.bind("<Return>", show_event_details)#bind button to Enter Key


tk.Label(text="tk.Entry is Bound to Mouseclick \n, FocusIn and Keypress Event").pack()
entry = tk.Entry(root) #creating entry widget
entry.pack()


#binding entry widget to mouse click and focus in
entry.bind("<Button-1>", show_event_details) # left mouse click
entry.bind("<Button-2>", show_event_details) # right mouse click
entry.bind("<FocusIn>", show_event_details)

#binding entry widget alphabets and numbers from keyboard
alpha_num_keys = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
for key in alpha_num_keys:
    entry.bind("<KeyPress-%s>"%key, show_event_details)

#binding entry widget to keysym
keysyms = ['Alt_L', 'Alt_R','BackSpace', 'Cancel', 'Caps_Lock','Control_L',
           'Control_R','Delete', 'Down', 'End', 'Escape', 'Execute','F1',
           'F2', 'Home', 'Insert', 'Left','Linefeed','KP_0','KP_1','KP_2',
           'KP_3','KP_4','KP_5','KP_6','KP_7','KP_8','KP_9','KP_Add',
           'KP_Decimal','KP_Divide']
for i in keysyms:
    entry.bind("<KeyPress-%s>"%i, show_event_details)


#binding tk.Canvas widget to Motion Event
tk.Label(text="Canvas Bound to Motion Event\n(Hover over the area \nto see motion event )").pack()
canvas = tk.Canvas(root, background='white',width=100, height=30)
canvas.pack()
canvas.bind('<Motion>', show_event_details)


tk.Label(text="Entry Widget Bound to \n<Any KeyPress>").pack()
entry_1 = tk.Entry(root) #creating entry widget
entry_1.pack(pady=7)
#binding entry widget to mouse click and focus in
entry_1.bind("<Any KeyPress>", show_event_details) # right mouse click


root.mainloop()
