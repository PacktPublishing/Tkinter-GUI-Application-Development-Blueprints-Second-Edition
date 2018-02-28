"""
Code illustration: 8.02
    Pie chart
Tkinter GUI Application Development Blueprints
"""


import tkinter

root = tkinter.Tk()
total_value_to_represent_by_pie_chart = 1000


def angle(n):
    return 360.0 * n / total_value_to_represent_by_pie_chart

tkinter.Label(root, text='Pie Chart').pack()

canvas = tkinter.Canvas(width=154, height=154)
canvas.pack()

canvas.create_arc((2, 2, 152, 152), fill="#FAF402",
                  outline="#FAF402", start=angle(0), extent=angle(200))
canvas.create_arc((2, 2, 152, 152), fill="#00AC36",
                  outline="#00AC36", start=angle(200), extent=angle(300))
canvas.create_arc((2, 2, 152, 152), fill="#7A0871",
                  outline="#7A0871", start=angle(500), extent=angle(150))
canvas.create_arc((2, 2, 152, 152), fill="#E00022",
                  outline="#E00022", start=angle(650), extent=angle(200))
canvas.create_arc((2, 2, 152, 152), fill="#294994",
                  outline="#294994",  start=angle(850), extent=angle(150))


root.mainloop()
