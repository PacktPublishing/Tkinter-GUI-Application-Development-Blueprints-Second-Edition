"""
Code illustration: 5.08

@Tkinter GUI Application Development Blueprints
"""

import tkinter as tk

class Seekbar(tk.Canvas):

    def __init__(self, parent, **options):
        tk.Canvas.__init__(self, parent, options)
        self.parent = parent
        self.width = options['width']
        self.red_rectangle = self.create_rectangle(0, 0, 0, 0, fill="red")
        self.seekbar_knob_image = tk.PhotoImage(file="../icons/seekbar_knob.gif")
        self.seekbar_knob = self.create_image(
            0, 0, image=self.seekbar_knob_image)
        self.bind_mouse_button()

    def bind_mouse_button(self):
        self.bind('<Button-1>', self.on_seekbar_clicked)
        self.bind('<B1-Motion>', self.on_seekbar_clicked)
        self.tag_bind(
            self.red_rectangle, '<B1-Motion>', self.on_seekbar_clicked)
        self.tag_bind(
            self.seekbar_knob, '<B1-Motion>', self.on_seekbar_clicked)

    def on_seekbar_clicked(self, event=None):
        if event.x > 0 and event.x < self.width:
            self.slide_to_position(event.x)

    def slide_to_position(self, new_position):
        self.coords(self.red_rectangle, 0, 0, new_position, new_position)
        self.coords(self.seekbar_knob, new_position, 0)
        self.event_generate("<<SeekbarPositionChanged>>", x=new_position)


class TestSeekBar():

    def __init__(self):
        root = tk.Tk()
        root.bind("<<SeekbarPositionChanged>>", self.seek_new_position)
        frame = tk.Frame(root)
        frame.grid(row=1, pady=10, padx=10)
        c = Seekbar(
            frame, background="blue", width=360, height=10)
        c.grid(row=2, columnspan=10, sticky='ew', padx=5)
        root.mainloop()

    def seek_new_position(self, event):
        print("Dragged to x:", event.x)

if __name__ == '__main__':
    TestSeekBar()

