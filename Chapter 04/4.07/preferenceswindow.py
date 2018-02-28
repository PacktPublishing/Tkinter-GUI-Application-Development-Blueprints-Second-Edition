"""
Code illustration: 4.07

    this entire file added here
    
@ Tkinter GUI Application Development Blueprints
"""


import sys
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.colorchooser import *
from configparser import ConfigParser
import configurations


class PreferencesWindow():

    def __init__(self, view):
        self.parent = view.parent
        self.fill_preference_colors()
        self.view = view
        self.create_prefereces_window()

    def fill_preference_colors(self):
        self.board_color_1 = configurations.BOARD_COLOR_1
        self.board_color_2 = configurations.BOARD_COLOR_2
        self.highlight_color = configurations.HIGHLIGHT_COLOR

    def set_color_1(self):
        self.board_color_1 = askcolor(initialcolor=self.board_color_1)[-1]

    def set_color_2(self):
        self.board_color_2 = askcolor(initialcolor=self.board_color_2)[-1]

    def set_highlight_color(self):
        self.highlight_color = askcolor(initialcolor=self.highlight_color)[-1]

    def create_prefereces_window(self):
        self.pref_window = Toplevel(self.parent)
        self.pref_window.title("set chess preferences")
        self.create_prefereces_list()
        self.pref_window.transient(self.parent)

    def create_prefereces_list(self):
        Label(self.pref_window, text="Board Color 1").grid(
            row=1, sticky=W, padx=5, pady=5)
        Label(self.pref_window, text="Board Color 2").grid(
            row=2, sticky=W, padx=5, pady=5)
        Label(self.pref_window, text="Highlight Color").grid(
            row=3, sticky=W, padx=5, pady=5)
        self.board_color_1_button = Button(
            self.pref_window, text='Select Board Color 1', command=self.set_color_1)
        self.board_color_1_button.grid(
            row=1, column=1, columnspan=2, sticky=E, padx=5, pady=5)
        self.board_color_2_button = Button(
            self.pref_window, text='Select Board Color 2', command=self.set_color_2)
        self.board_color_2_button.grid(
            row=2, column=1, columnspan=2, sticky=E, padx=5, pady=5)
        self.highlight_color_button = Button(
            self.pref_window, text='Select Highlight Color', command=self.set_highlight_color)
        self.highlight_color_button.grid(
            row=3, column=1, columnspan=2, sticky=E, padx=5, pady=5)
        Button(self.pref_window, text="Save", command=self.on_save_button_clicked).grid(
            row=4, column=2, sticky=E, padx=5, pady=5)
        Button(self.pref_window, text="Cancel", command=self.on_cancel_button_clicked).grid(
            row=4, column=1, sticky=E, padx=5, pady=5)

    def on_save_button_clicked(self):
        self.set_new_values()
        self.pref_window.destroy()
        self.view.reload_colors(
            self.board_color_1, self.board_color_2, self.highlight_color)

    def set_new_values(self):
        config = ConfigParser()
        config.read('chess_options.ini')
        config.set('chess_colors', 'board_color_1', self.board_color_1)
        config.set('chess_colors', 'board_color_2', self.board_color_2)
        config.set('chess_colors', 'highlight_color', self.highlight_color)
        configurations.BOARD_COLOR_1 = self.board_color_1
        configurations.BOARD_COLOR_2 = self.board_color_2
        configurations.HIGHLIGHT_COLOR = self.highlight_color
        with open('chess_options.ini', 'w') as config_file:
            config.write(config_file)

    def on_cancel_button_clicked(self):
        self.pref_window.destroy()
