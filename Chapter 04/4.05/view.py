"""
Code illustration: 4.05

@ Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, Menu, Label, Frame, Canvas, RIGHT, PhotoImage, messagebox
import controller
from configurations import *


class View():

    images = {}
    board_color_1 = BOARD_COLOR_1
    board_color_2 = BOARD_COLOR_2

    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.create_chess_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.start_new_game()

    def create_chess_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_bottom_frame()

    def create_top_menu(self):
        self.menu_bar = Menu(self.parent)
        self.create_file_menu()
        self.create_edit_menu()
        self.create_about_menu()

    def create_bottom_frame(self):
        self.bottom_frame = Frame(self.parent, height=64)
        self.info_label = Label(
            self.bottom_frame, text="   White to Start the Game  ", fg="black")
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side="bottom")

    def on_about_menu_clicked(self):
        messagebox.showinfo("From the Book:",
                            "Tkinter GUI Application\n Development Blueprints")

    def on_new_game_menu_clicked(self):
        pass

    def on_preference_menu_clicked(self):
        pass

    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(
            label="New Game", command=self.on_new_game_menu_clicked)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)

    def create_edit_menu(self):
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(
            label="Preferences", command=self.on_preference_menu_clicked)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.parent.config(menu=self.menu_bar)

    def create_about_menu(self):
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(
            label="About", command=self.on_about_menu_clicked)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.parent.config(menu=self.menu_bar)

    def create_canvas(self):
        canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = Canvas(
            self.parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

    def draw_board(self):
        current_color = BOARD_COLOR_2
        for row in range(NUMBER_OF_ROWS):
            current_color = self.get_alternate_color(current_color)
            for col in range(NUMBER_OF_COLUMNS):
                x1, y1 = self.get_x_y_coordinate(row, col)
                x2, y2 = x1 + DIMENSION_OF_EACH_SQUARE, y1 + DIMENSION_OF_EACH_SQUARE
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,  fill=current_color)
                current_color = self.get_alternate_color(current_color)

    def on_square_clicked(self, event):
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        print("Hey you clicked on", clicked_row, clicked_column)

    def get_clicked_row_column(self, event):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        clicked_row = 7 - (event.y // row_size)
        return (clicked_row, clicked_column)

    def get_x_y_coordinate(self, row, col):
        x = (col * DIMENSION_OF_EACH_SQUARE)
        y = ((7 - row) * DIMENSION_OF_EACH_SQUARE)
        return (x, y)

    def calculate_piece_coordinate(self, row, col):
        x0 = (col * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        y0 = ((7 - row) * DIMENSION_OF_EACH_SQUARE) + \
            int(DIMENSION_OF_EACH_SQUARE / 2)
        return (x0, y0)

    def draw_single_piece(self, position, piece):
        x, y = self.controller.get_numeric_notation(position)
        if piece:
            filename = "../pieces_image/{}_{}.png".format(
                piece.name.lower(), piece.color)
            if filename not in self.images:
                self.images[filename] = PhotoImage(file=filename)
            x0, y0 = self.calculate_piece_coordinate(x, y)
            self.canvas.create_image(x0, y0, image=self.images[
                                     filename], tags=("occupied"), anchor="c")

    def draw_all_pieces(self):
        self.canvas.delete("occupied")
        for position, piece in self.controller.get_all_peices_on_chess_board():
            self.draw_single_piece(position, piece)

    def start_new_game(self):
        self.controller.reset_game_data()
        self.controller.reset_to_initial_locations()
        self.draw_all_pieces()
        self.info_label.config(text="   White to Start the Game  ")

    def get_alternate_color(self, current_color):
        if current_color == self.board_color_2:
            next_color = self.board_color_1
        else:
            next_color = self.board_color_2
        return next_color


def main(controller):
    root = Tk()
    root.title("Chess")
    View(root, controller)
    root.mainloop()


def init_new_game():
    game_controller = controller.Controller()
    main(game_controller)

if __name__ == "__main__":
    init_new_game()
