"""
Code illustration: 6.02

    New attributes defined here:
        start_x, start_y
        end_x, end_y

    Methods modified here:
        __init__ (added a call to bind_mouse)
    
    New methods defined here:
        bind_mouse()
        on_mouse_button_pressed()
        on_mouse_button_pressed_motion()
        on_mouse_button_released()
        on_mouse_unpressed_motion()

@ Tkinter GUI Application Development Blueprints
"""

import tkinter as tk
import framework


class PaintApplication(framework.Framework):

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    def bind_mouse(self):
        self.canvas.bind("<Button-1>", self.on_mouse_button_pressed)
        self.canvas.bind(
            "<Button1-Motion>", self.on_mouse_button_pressed_motion)
        self.canvas.bind(
            "<Button1-ButtonRelease>", self.on_mouse_button_released)
        self.canvas.bind("<Motion>", self.on_mouse_unpressed_motion)

    def on_mouse_button_pressed(self, event):
        self.start_x = self.end_x = self.canvas.canvasx(event.x)
        self.start_y = self.end_y = self.canvas.canvasy(event.y)
        print("start_x, start_y = ", self.start_x, self.start_y)

    def on_mouse_button_pressed_motion(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

    def on_mouse_button_released(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        print("end_x, end_y = ", self.end_x, self.end_y)

    def on_mouse_unpressed_motion(self, event):
        pass

    def __init__(self, root):
        super().__init__(root)
        self.create_gui()
        self.bind_mouse()

    def create_gui(self):
        self.create_menu()
        self.create_top_bar()
        self.create_tool_bar()
        self.create_drawing_canvas()
        self.bind_menu_accelrator_keys()

    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        menu_definitions = (
            'File- &New/Ctrl+N/self.on_new_file_menu_clicked, Save/Ctrl+S/self.on_save_menu_clicked, SaveAs/ /self.on_save_as_menu_clicked, sep, Exit/Alt+F4/self.on_close_menu_clicked',
            'Edit- Undo/Ctrl+Z/self.on_undo_menu_clicked, sep',
            'View- Zoom in//self.on_canvas_zoom_in_menu_clicked,Zoom Out//self.on_canvas_zoom_out_menu_clicked',
            'About- About/F1/self.on_about_menu_clicked'
        )
        self.build_menu(menu_definitions)

    def create_top_bar(self):
        self.top_bar = tk.Frame(self.root, height=25, relief="raised")
        self.top_bar.pack(fill="x", side="top", pady=2)

    def create_tool_bar(self):
        self.tool_bar = tk.Frame(self.root, relief="raised", width=50)
        self.tool_bar.pack(fill="y", side="left", pady=3)

    def create_drawing_canvas(self):
        self.canvas_frame = tk.Frame(self.root, width=900, height=900)
        self.canvas_frame.pack(side="right", expand="yes", fill="both")
        self.canvas = tk.Canvas(self.canvas_frame, background="white",
                                width=500, height=500, scrollregion=(0, 0, 800, 800))
        self.create_scroll_bar()
        self.canvas.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

    def create_scroll_bar(self):
        x_scroll = tk.Scrollbar(self.canvas_frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        x_scroll.config(command=self.canvas.xview)
        y_scroll = tk.Scrollbar(self.canvas_frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")
        y_scroll.config(command=self.canvas.yview)
        self.canvas.config(
            xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

    def bind_menu_accelrator_keys(self):
        self.root.bind('<KeyPress-F1>', self.on_about_menu_clicked)
        self.root.bind('<Control-N>', self.on_new_file_menu_clicked)
        self.root.bind('<Control-n>', self.on_new_file_menu_clicked)
        self.root.bind('<Control-s>', self.on_save_menu_clicked)
        self.root.bind('<Control-S>', self.on_save_menu_clicked)
        self.root.bind('<Control-z>', self.on_undo_menu_clicked)
        self.root.bind('<Control-Z>', self.on_undo_menu_clicked)

    def on_new_file_menu_clicked(self, event=None):
        pass

    def on_save_menu_clicked(self, event=None):
        pass

    def on_save_as_menu_clicked(self):
        pass

    def on_canvas_zoom_out_menu_clicked(self):
        pass

    def on_canvas_zoom_in_menu_clicked(self):
        pass

    def on_close_menu_clicked(self):
        pass

    def on_undo_menu_clicked(self, event=None):
        pass

    def on_about_menu_clicked(self, event=None):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = PaintApplication(root)
    root.mainloop()
