"""
Code illustration: 6.08
    
    New methods added here:
        draw_text()
        draw_text_options()
        on_create_text_button_clicked()
        delete_item()
        fill_item()
        fill_item_options()
        duplicate_item()
        get_all_configurations_for_item()
        canvas_function_wrapper()
        move_to_top()
        drag_item()
        drag_item_update_x_y(self, event):
        enlarge_item_size()
        reduce_item_size()
    
        
@ Tkinter GUI Application Development Blueprints
"""
import math
import cmath
import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
import framework
from supershapes import *


class PaintApplication(framework.Framework):

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    current_item = None
    fill = "red"
    outline = "red"
    width = 2.0
    number_of_spokes = 5
    arrow = None
    dash = None
    background = 'white'
    foreground = 'red'
    selected_super_shape = "shape A"

    tool_bar_functions = (
        "draw_line", "draw_oval", "draw_rectangle", "draw_arc",
        "draw_triangle", "draw_star", "draw_irregular_line", "draw_super_shape", "draw_text", "delete_item", "fill_item", "duplicate_item", "move_to_top", "drag_item", "enlarge_item_size", "reduce_item_size"
    )
    selected_tool_bar_function = tool_bar_functions[0]

    def draw_text(self):
        pass

    def draw_text_options(self):
        tk.Label(self.top_bar, text='Text:').pack(side="left")
        self.text_entry_widget = tk.Entry(self.top_bar, width=20)
        self.text_entry_widget.pack(side="left")
        tk.Label(self.top_bar, text='Font size:').pack(side="left")
        self.font_size_spinbox = tk.Spinbox(
            self.top_bar, from_=14, to=100, width=3)
        self.font_size_spinbox.pack(side="left")
        self.create_fill_options_combobox()
        self.create_text_button = tk.Button(
            self.top_bar, text="Go", command=self.on_create_text_button_clicked)
        self.create_text_button.pack(side="left", padx=5)

    def on_create_text_button_clicked(self):
        entered_text = self.text_entry_widget.get()
        center_x = self.canvas.winfo_width() / 2
        center_y = self.canvas.winfo_height() / 2
        font_size = self.font_size_spinbox.get()
        self.canvas.create_text(
            center_x, center_y, font=("", font_size), text=entered_text, fill=self.fill)

    def delete_item(self):
        self.current_item = None
        self.canvas.delete("current")

    def fill_item(self):
        try:
            self.canvas.itemconfig(
                "current", fill=self.fill, outline=self.outline)
        except TclError:
            self.canvas.itemconfig("current", fill=self.fill)

    def fill_item_options(self):
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()

    def duplicate_item(self):
        try:
            function_name = "create_" + self.canvas.type("current")
        except TypeError:
            return
        coordinates = tuple(
            map(lambda i: i + 10, self.canvas.coords("current")))
        configurations = self.get_all_configurations_for_item()
        self.canvas_function_wrapper(
            function_name, coordinates, configurations)

    def get_all_configurations_for_item(self):
        configuration_dict = {}
        for key, value in self.canvas.itemconfig("current").items():
            if value[-1] and value[-1] not in ["0", "0.0", "0,0", "current"]:
                configuration_dict[key] = value[-1]
        return configuration_dict

    def canvas_function_wrapper(self, function_name, *arg, **kwargs):
        func = getattr(self.canvas, function_name)
        func(*arg, **kwargs)

    def move_to_top(self):
        self.current_item = None
        self.canvas.tag_raise("current")

    def drag_item(self):
        self.canvas.move(
            "current", self.end_x - self.start_x, self.end_y - self.start_y)
        self.canvas.bind("<B1-Motion>", self.drag_item_update_x_y)

    def drag_item_update_x_y(self, event):
        self.start_x, self.start_y = self.end_x, self.end_y
        self.end_x, self.end_y = event.x, event.y
        self.drag_item()

    def enlarge_item_size(self):
        self.current_item = None
        if self.canvas.find_withtag("current"):
            self.canvas.scale("current", self.end_x, self.end_y, 1.2, 1.2)
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def reduce_item_size(self):
        self.current_item = None
        if self.canvas.find_withtag("current"):
            self.canvas.scale("current", self.end_x, self.end_y, .8, .8)
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def draw_irregular_line(self):
        self.current_item = self.canvas.create_line(
            self.start_x, self.start_y, self.end_x, self.end_y, fill=self.fill, width=self.width)
        self.canvas.bind("<B1-Motion>", self.draw_irregular_line_update_x_y)

    def draw_irregular_line_update_x_y(self, event=None):
        self.start_x, self.start_y = self.end_x, self.end_y
        self.end_x, self.end_y = event.x, event.y
        self.draw_irregular_line()

    def draw_irregular_line_options(self):
        self.create_fill_options_combobox()
        self.create_width_options_combobox()

    def on_tool_bar_button_clicked(self, button_index):
        self.selected_tool_bar_function = self.tool_bar_functions[button_index]
        self.remove_options_from_top_bar()
        self.display_options_in_the_top_bar()
        self.bind_mouse()

    def draw_super_shape(self):
        points = self.get_super_shape_points(
            *super_shapes[self.selected_super_shape])
        self.current_item = self.canvas.create_polygon(points, outline=self.outline,
                                                       fill=self.fill, width=self.width)

    def draw_super_shape_options(self):
        self.create_super_shapes_options_combobox()
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()
        self.create_width_options_combobox()

    def create_super_shapes_options_combobox(self):
        tk.Label(self.top_bar, text='Select shape:').pack(side="left")
        self.super_shape_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=8)
        self.super_shape_combobox.pack(side="left")
        self.super_shape_combobox['values'] = tuple(
            shape for shape in super_shapes.keys())
        self.super_shape_combobox.bind(
            '<<ComboboxSelected>>', self.set_selected_super_shape)
        self.super_shape_combobox.set(self.selected_super_shape)

    def set_selected_super_shape(self, event=None):
        self.selected_super_shape = self.super_shape_combobox.get()

    def get_super_shape_points(self, a, b, m, n1, n2, n3):
        # https://en.wikipedia.org/wiki/Superformula
        points = []
        for i in self.float_range(0, 2 * math.pi, 0.01):
            raux = (abs(1 / a * abs(math.cos(m * i / 4))) ** n2 +
                    abs(1 / b * abs(math.sin(m * i / 4))) ** n3)
            r = abs(raux) ** (-1 / n1)
            x = self.end_x + r * math.cos(i)
            y = self.end_y + r * math.sin(i)
            points.extend((x, y))
        return points

    def float_range(self, x, y, step):
        while x < y:
            yield x
            x += step

    def set_foreground_color(self, event=None):
        self.foreground = self.get_color_from_chooser(
            self.foreground, "foreground")
        self.color_palette.itemconfig(
            self.foreground_palette, width=0, fill=self.foreground)

    def set_background_color(self, event=None):
        self.background = self.get_color_from_chooser(
            self.background, "background")
        self.color_palette.itemconfig(
            self.background_palette, width=0, fill=self.background)

    def get_color_from_chooser(self, initial_color, color_type="a"):
        color = colorchooser.askcolor(
            color=initial_color,
            title="select {} color".format(color_type)
        )[-1]
        if color:
            return color
        # dialog has been cancelled
        else:
            return initial_color

    def try_to_set_fill_after_palette_change(self):
        try:
            self.set_fill()
        except:
            pass

    def try_to_set_outline_after_palette_change(self):
        try:
            self.set_outline()
        except:
            pass

    def display_options_in_the_top_bar(self):
        self.show_selected_tool_icon_in_top_bar(
            self.selected_tool_bar_function)
        options_function_name = "{}_options".format(
            self.selected_tool_bar_function)
        func = getattr(self, options_function_name, self.function_not_defined)
        func()

    def draw_line_options(self):
        self.create_fill_options_combobox()
        self.create_width_options_combobox()
        self.create_arrow_options_combobox()
        self.create_dash_options_combobox()

    def draw_oval_options(self):
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()
        self.create_width_options_combobox()

    def draw_rectangle_options(self):
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()
        self.create_width_options_combobox()

    def draw_arc_options(self):
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()
        self.create_width_options_combobox()

    def draw_triangle_options(self):
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()
        self.create_width_options_combobox()

    def draw_star_options(self):
        self.create_number_of_spokes_options_combobox()
        self.create_fill_options_combobox()
        self.create_outline_options_combobox()
        self.create_width_options_combobox()

    def create_fill_options_combobox(self):
        tk.Label(self.top_bar, text='Fill:').pack(side="left")
        self.fill_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=5)
        self.fill_combobox.pack(side="left")
        self.fill_combobox['values'] = ('none', 'fg', 'bg', 'black', 'white')
        self.fill_combobox.bind('<<ComboboxSelected>>', self.set_fill)
        self.fill_combobox.set(self.fill)

    def create_number_of_spokes_options_combobox(self):
        tk.Label(self.top_bar, text='Number of Edges:').pack(side="left")
        self.number_of_spokes_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=3)
        self.number_of_spokes_combobox.pack(side="left")
        self.number_of_spokes_combobox[
            'values'] = tuple(i for i in range(5, 50))
        self.number_of_spokes_combobox.bind(
            '<<ComboboxSelected>>', self.set_number_of_spokes)
        self.number_of_spokes_combobox.set(self.number_of_spokes)

    def create_outline_options_combobox(self):
        tk.Label(self.top_bar, text='Outline:').pack(side="left")
        self.outline_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=5)
        self.outline_combobox.pack(side="left")
        self.outline_combobox['values'] = (
            'none', 'fg', 'bg', 'black', 'white')
        self.outline_combobox.bind('<<ComboboxSelected>>', self.set_outline)
        self.outline_combobox.set(self.outline)

    def create_width_options_combobox(self):
        tk.Label(self.top_bar, text='Width:').pack(side="left")
        self.width_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=3)
        self.width_combobox.pack(side="left")
        self.width_combobox['values'] = (
            1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0)
        self.width_combobox.bind('<<ComboboxSelected>>', self.set_width)
        self.width_combobox.set(self.width)

    def create_dash_options_combobox(self):
        tk.Label(self.top_bar, text='Dash:').pack(side="left")
        self.dash_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=5)
        self.dash_combobox.pack(side="left")
        self.dash_combobox['values'] = ('none', 'small', 'medium', 'large')
        self.dash_combobox.bind('<<ComboboxSelected>>', self.set_dash)
        self.dash_combobox.current(0)

    def create_arrow_options_combobox(self):
        tk.Label(self.top_bar, text='Arrow:').pack(side="left")
        self.arrow_combobox = ttk.Combobox(
            self.top_bar, state='readonly', width=5)
        self.arrow_combobox.pack(side="left")
        self.arrow_combobox['values'] = ('none', 'first', 'last', 'both')
        self.arrow_combobox.bind('<<ComboboxSelected>>', self.set_arrow)
        self.arrow_combobox.current(0)

    def set_fill(self, event=None):
        fill_color = self.fill_combobox.get()
        if fill_color == 'none':
            self.fill = ''  # transparent
        elif fill_color == 'fg':
            self.fill = self.foreground
        elif fill_color == 'bg':
            self.fill = self.background
        else:
            self.fill = fill_color

    def set_outline(self, event=None):
        outline_color = self.outline_combobox.get()
        if outline_color == 'none':
            self.outline = ''  # transparent
        elif outline_color == 'fg':
            self.outline = self.foreground
        elif outline_color == 'bg':
            self.outline = self.background
        else:
            self.outline = outline_color

    def set_width(self, event):
        self.width = float(self.width_combobox.get())

    def set_number_of_spokes(self, event):
        self.number_of_spokes = int(self.number_of_spokes_combobox.get())

    def set_arrow(self, event):
        self.arrow = self.arrow_combobox.get()

    def set_dash(self, event):
        '''Dash takes value from 1 to 255'''
        dash_size = self.dash_combobox.get()
        if dash_size == 'none':
            self.dash = None
        elif dash_size == 'small':
            self.dash = 1
        elif dash_size == 'medium':
            self.dash = 15
        elif dash_size == 'large':
            self.dash = 100

    def create_color_palette(self):
        self.color_palette = tk.Canvas(self.tool_bar, height=55, width=55)
        self.color_palette.grid(row=10, column=1, columnspan=2, pady=5, padx=3)
        self.background_palette = self.color_palette.create_rectangle(
            15, 15, 48, 48, outline=self.background, fill=self.background)
        self.foreground_palette = self.color_palette.create_rectangle(
            1, 1, 33, 33, outline=self.foreground, fill=self.foreground)
        self.bind_color_palette()

    def bind_color_palette(self):
        self.color_palette.tag_bind(
            self.background_palette, "<Button-1>", self.set_background_color)
        self.color_palette.tag_bind(
            self.foreground_palette, "<Button-1>", self.set_foreground_color)

    def create_current_coordinate_label(self):
        self.current_coordinate_label = tk.Label(
            self.tool_bar, text='x:0\ny: 0 ')
        self.current_coordinate_label.grid(
            row=13, column=1, columnspan=2, pady=5, padx=1, sticky='w')

    def show_current_coordinates(self, event=None):
        x_coordinate = event.x
        y_coordinate = event.y
        coordinate_string = "x:{0}\ny:{1}".format(x_coordinate, y_coordinate)
        self.current_coordinate_label.config(text=coordinate_string)

    def function_not_defined(self):
        pass

    def execute_selected_method(self):
        self.current_item = None
        func = getattr(
            self, self.selected_tool_bar_function, self.function_not_defined)
        func()

    def draw_line(self):
        self.current_item = self.canvas.create_line(
            self.start_x, self.start_y, self.end_x, self.end_y, fill=self.fill, width=self.width, arrow=self.arrow, dash=self.dash)

    def draw_oval(self):
        self.current_item = self.canvas.create_oval(
            self.start_x, self.start_y, self.end_x, self.end_y, outline=self.outline, fill=self.fill, width=self.width)

    def draw_rectangle(self):
        self.current_item = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.end_x, self.end_y, outline=self.outline, fill=self.fill, width=self.width)

    def draw_arc(self):
        self.current_item = self.canvas.create_arc(
            self.start_x, self.start_y, self.end_x, self.end_y, outline=self.outline, fill=self.fill, width=self.width)

    def draw_triangle(self):
        dx = self.end_x - self.start_x
        dy = self.end_y - self.start_y
        z = complex(dx, dy)
        radius, angle0 = cmath.polar(z)
        edges = 3
        points = list()
        for edge in range(edges):
            angle = angle0 + edge * (2 * math.pi) / edges
            points.append(self.start_x + radius * math.cos(angle))
            points.append(self.start_y + radius * math.sin(angle))
        self.current_item = self.canvas.create_polygon(
            points, outline=self.outline, fill=self.fill,
            width=self.width)

    def draw_star(self):
        dx = self.end_x - self.start_x
        dy = self.end_y - self.start_y
        z = complex(dx, dy)
        radius_out, angle0 = cmath.polar(z)
        radius_in = radius_out / 2
        points = list()
        for edge in range(self.number_of_spokes):
            angle = angle0 + edge * (2 * math.pi) / self.number_of_spokes
            points.append(self.start_x + radius_out * math.cos(angle))
            points.append(self.start_y + radius_out * math.sin(angle))
            angle += math.pi / self.number_of_spokes
            points.append(self.start_x + radius_in * math.cos(angle))
            points.append(self.start_y + radius_in * math.sin(angle))
        self.current_item = self.canvas.create_polygon(
            points, outline=self.outline, fill=self.fill,
            width=self.width)

    def create_tool_bar_buttons(self):
        for index, name in enumerate(self.tool_bar_functions):
            icon = tk.PhotoImage(file='icons/' + name + '.gif')
            self.button = tk.Button(
                self.tool_bar, image=icon, command=lambda index=index: self.on_tool_bar_button_clicked(index))
            self.button.grid(
                row=index // 2, column=1 + index % 2, sticky='nsew')
            self.button.image = icon

    def remove_options_from_top_bar(self):
        for child in self.top_bar.winfo_children():
            child.destroy()

    def show_selected_tool_icon_in_top_bar(self, function_name):
        display_name = function_name.replace("_", " ").capitalize() + ":"
        tk.Label(self.top_bar, text=display_name).pack(side="left")
        photo = tk.PhotoImage(
            file='icons/' + function_name + '.gif')
        label = tk.Label(self.top_bar, image=photo)
        label.image = photo
        label.pack(side="left")

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
        self.execute_selected_method()

    def on_mouse_button_pressed_motion(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.delete(self.current_item)
        self.execute_selected_method()

    def on_mouse_button_released(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

    def on_mouse_unpressed_motion(self, event):
        self.show_current_coordinates(event)

    def __init__(self, root):
        super().__init__(root)
        self.create_gui()
        self.bind_mouse()

    def create_gui(self):
        self.create_menu()
        self.create_top_bar()
        self.create_tool_bar()
        self.create_tool_bar_buttons()
        self.create_drawing_canvas()
        self.create_color_palette()
        self.create_current_coordinate_label()
        self.bind_menu_accelrator_keys()
        self.show_selected_tool_icon_in_top_bar("draw_line")
        self.draw_line_options()

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
