'''
Chapter 7: Piano Tutor
Tkinter GUI Application Development Blueprints

'''
from tkinter import Tk, Frame, Button, BOTH, Label, PhotoImage, \
    StringVar, OptionMenu, ttk
from constants import *


class PianoTutor:

    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title('Piano Tutor')
        self.build_mode_selector_frame()
        self.build_score_sheet_frame()
        self.build_controls_frame()
        self.build_keyboard_frame()
        self.build_chords_frame()
        self.build_progressions_frame()
        self.build_scales_frame()

    def build_mode_selector_frame(self):
        self.mode_selector_frame = Frame(self.root, width=WINDOW_WIDTH,
                height=MODE_SELECTOR_HEIGHT, background='mint cream')
        self.mode_selector_frame.grid_propagate(False)
        self.mode_selector = ttk.Combobox(self.mode_selector_frame,
                values=CHOICES)
        self.mode_selector.bind('<<ComboboxSelected>>',
                                self.on_mode_changed)
        self.mode_selector.current(0)
        self.mode_selector.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew',
            )
        self.mode_selector_frame.grid(row=0, column=0)

    def build_score_sheet_frame(self):
        self.score_sheet_frame = Frame(self.root, width=WINDOW_WIDTH,
                height=SCORE_DISPLAY_HEIGHT, background='SteelBlue1')
        self.score_sheet_frame.grid_propagate(False)
        Label(self.score_sheet_frame, text='placeholder for score sheet'
              , background='SteelBlue1').grid(row=1, column=1)
        self.score_sheet_frame.grid(row=1, column=0)

    def build_controls_frame(self):
        self.controls_frame = Frame(self.root, width=WINDOW_WIDTH,
                                    height=CONTROLS_FRAME_HEIGHT,
                                    background='cornsilk3')
        self.controls_frame.grid_propagate(False)
        self.controls_frame.grid(row=2, column=0)

    def build_keyboard_frame(self):
        self.keyboard_frame = Frame(self.root, width=WINDOW_WIDTH,
                                    height=KEYBOARD_HEIGHT,
                                    background='LavenderBlush2')
        self.keyboard_frame.grid_propagate(False)
        Label(self.keyboard_frame, text='placeholder for keyboard',
              background='LavenderBlush2').grid()
        self.keyboard_frame.grid(row=4, column=0, sticky='nsew')

    def build_scales_frame(self):
        self.scales_frame = Frame(self.controls_frame,
                                  width=WINDOW_WIDTH,
                                  height=CONTROLS_FRAME_HEIGHT,
                                  bg='SlateBlue3')
        Label(self.scales_frame, text='placeholder for scales frame'
              ).grid(row=1, column=1)
        self.scales_frame.grid(row=1, column=0, sticky='nsew')

    def build_chords_frame(self):
        self.chords_frame = Frame(self.controls_frame,
                                  width=WINDOW_WIDTH,
                                  height=CONTROLS_FRAME_HEIGHT,
                                  bg='cornsilk4')
        self.chords_frame.grid_propagate(False)
        Label(self.chords_frame, text='placeholder for chords frame'
              ).grid(row=1, column=1)
        self.chords_frame.grid(row=1, column=0, sticky='nsew')

    def build_progressions_frame(self):
        self.progressions_frame = Frame(self.controls_frame,
                width=WINDOW_WIDTH, height=CONTROLS_FRAME_HEIGHT,
                bg='plum2')
        self.progressions_frame.grid_propagate(False)
        Label(self.progressions_frame,
              text='placeholder for progression frame').grid(row=1,
                column=1)
        self.progressions_frame.grid(row=1, column=0, sticky='nsew')

    def on_mode_changed(self, event):
        selected_mode = self.mode_selector.get()
        if selected_mode == 'Scales':
            self.show_scales_frame()
        elif selected_mode == 'Chords':
            self.show_chords_frame()
        elif selected_mode == 'Chord Progressions':
            self.show_progressions_frame()

    def show_scales_frame(self):
        self.chords_frame.grid_remove()
        self.progressions_frame.grid_remove()
        self.scales_frame.grid()

    def show_chords_frame(self):
        self.chords_frame.grid()
        self.progressions_frame.grid_remove()
        self.scales_frame.grid_remove()

    def show_progressions_frame(self):
        self.chords_frame.grid_remove()
        self.progressions_frame.grid()
        self.scales_frame.grid_remove()


def run():
    root = Tk()
    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()
    SCREEN_X_CENTER = (SCREEN_WIDTH - WINDOW_WIDTH) / 2
    SCREEN_Y_CENTER = (SCREEN_HEIGHT - WINDOW_HEIGHT) / 2
    root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT,
                  SCREEN_X_CENTER, SCREEN_Y_CENTER))
    root.resizable(False, False)
    PianoTutor(root)
    root.mainloop()


if __name__ == '__main__':
    run()

			
