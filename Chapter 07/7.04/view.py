'''
7.04

    Implementing the Scales Tutor

new imports here:
 import json
 from collections import OrderedDict
 from audio import play_scale_in_new_thread
method modified here
    __init___  - added call to self.load_json_files()
    build_scales_frame - added two combobox

methods defined here:
    on_scale_changed
    on_scale_key_changed
    find_scale
    highlight_list_of_keys
    
'''
from tkinter import Tk, Frame, Button, BOTH, Label, PhotoImage, \
    StringVar, OptionMenu, ttk
import json    
from collections import OrderedDict
from audio import play_note, play_scale_in_new_thread    
from constants import *


class PianoTutor:

    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title('Piano Tutor')
        self.keys = []
        self.load_json_files()
        self.keys_to_highlight = []
        self.build_mode_selector_frame()
        self.build_score_sheet_frame()
        self.build_controls_frame()
        self.build_keyboard_frame()
        self.build_chords_frame()
        self.build_progressions_frame()
        self.build_scales_frame()
        self.find_scale()

    def load_json_files(self):
      with open(SCALES_JSON_FILE, 'r') as f:
        self.scales = json.load(f, object_pairs_hook=OrderedDict)


    def on_scale_changed(self, event):
      self.remove_all_key_highlights()
      self.find_scale(event)
      
    def on_scale_key_changed(self, event):
      self.remove_all_key_highlights()
      self.find_scale(event)

    def find_scale(self, event=None):
      self.selected_scale = self.scale_selector.get()
      self.scale_selected_key = self.scale_key_selector.get()
      index_of_selected_key = KEYS.index(self.scale_selected_key)
      self.keys_to_highlight = [ ALL_KEYS[i+index_of_selected_key] \
                            for i in self.scales[self.selected_scale]]
      self.highlight_list_of_keys(self.keys_to_highlight)
      play_scale_in_new_thread(self.keys_to_highlight)

    def highlight_list_of_keys(self, key_names):
      for key in key_names:
        self.highlight_key(key)
	
    def highlight_key(self, key_name):
        if len(key_name) == 2:
            img = WHITE_KEY_PRESSED_IMAGE
        elif len(key_name) == 3:
            img = BLACK_KEY_PRESSED_IMAGE
        key_img = PhotoImage(file=img)
        for widget in self.keys:
          if widget.name == key_name:
            widget.configure(image=key_img)
            widget.image = key_img
      
    def remove_key_highlight(self, key_name):
        if len(key_name) == 2:
            img = WHITE_KEY_IMAGE
        elif len(key_name) == 3:
            img = BLACK_KEY_IMAGE
        key_img = PhotoImage(file=img)
        for widget in self.keys:
          if widget.name == key_name:
            widget.configure(image=key_img)
            widget.image = key_img
      
    def remove_all_key_highlights(self):
      for key in self.keys_to_highlight:
        self.remove_key_highlight(key)
      self.keys_to_highlight = [] 




    def build_mode_selector_frame(self):
        self.mode_selector_frame = Frame(self.root, width=WINDOW_WIDTH,
                height=MODE_SELECTOR_HEIGHT)
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
                                    height=CONTROLS_FRAME_HEIGHT)
        self.controls_frame.grid_propagate(False)
        self.controls_frame.grid(row=2, column=0)

    def build_keyboard_frame(self):
        self.keyboard_frame = Frame(self.root, width=WINDOW_WIDTH,
                                    height=KEYBOARD_HEIGHT,
                                    background='LavenderBlush2')
        self.keyboard_frame.grid_propagate(False)
        self.keyboard_frame.grid(row=4, column=0, sticky='nsew')
        for (index, key) in enumerate(WHITE_KEY_NAMES):
            x = WHITE_KEY_X_COORDINATES[index]
            self.create_key(WHITE_KEY_IMAGE, key, x)
        for (index, key) in enumerate(BLACK_KEY_NAMES):
            x = BLACK_KEY_X_COORDINATES[index]
            self.create_key(BLACK_KEY_IMAGE, key, x)

    def build_scales_frame(self):
        self.scales_frame = Frame(self.controls_frame,
                                  width=WINDOW_WIDTH,
                                  height=CONTROLS_FRAME_HEIGHT
                                  )
        self.scales_frame.grid(row=1, column=0, sticky='nsew')
        Label(self.scales_frame, text='Select scale').grid(row=0, \
                                column=1, sticky='w', padx=10,pady=1)
        self.scale_selector = ttk.Combobox(self.scales_frame, \
                                values=[k for k in self.scales.keys()])
        self.scale_selector.current(0)
        self.scale_selector.bind("<<ComboboxSelected>>", \
                                            self.on_scale_changed)
        self.scale_selector.grid(row=1, column=1, sticky='e', padx=10,\
                                                                pady=10)
        Label(self.scales_frame, text='in the key of').grid(row=0, \
                                column=2, sticky='w', padx=10,pady=1)
        self.scale_key_selector = ttk.Combobox(self.scales_frame, \
                                    values=[k for k in KEYS])
        self.scale_key_selector.current(0)
        self.scale_key_selector.bind("<<ComboboxSelected>>", \
                                    self.on_scale_key_changed)
        self.scale_key_selector.grid(row=1, column=2, sticky='e', \
                                    padx=10, pady=10)




    def build_chords_frame(self):
        self.chords_frame = Frame(self.controls_frame,
                                  width=WINDOW_WIDTH,
                                  height=CONTROLS_FRAME_HEIGHT
                                  )
        self.chords_frame.grid_propagate(False)
        Label(self.chords_frame, text='placeholder for chords frame'
              ).grid(row=1, column=1)
        self.chords_frame.grid(row=1, column=0, sticky='nsew')

    def build_progressions_frame(self):
        self.progressions_frame = Frame(self.controls_frame,
                width=WINDOW_WIDTH, height=CONTROLS_FRAME_HEIGHT)
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

    def create_key(self, img, key_name, x_coordinate):
        key_image = PhotoImage(file=img)
        label = Label(self.keyboard_frame, image=key_image, border=0)
        label.image = key_image
        label.place(x=x_coordinate, y=0)
        label.name = key_name
        label.bind('<Button-1>', self.on_key_pressed)
        label.bind('<ButtonRelease-1>', self.on_key_released)
        self.keys.append(label)
        return label

    def change_image_to_pressed(self, event):
        if len(event.widget.name) == 2:
            img = WHITE_KEY_PRESSED_IMAGE
        elif len(event.widget.name) == 3:
            img = BLACK_KEY_PRESSED_IMAGE
        key_img = PhotoImage(file=img)
        event.widget.configure(image=key_img)
        event.widget.image = key_img

    def change_image_to_unpressed(self, event):
        if len(event.widget.name) == 2:
            img = WHITE_KEY_IMAGE
        elif len(event.widget.name) == 3:
            img = BLACK_KEY_IMAGE
        key_img = PhotoImage(file=img)
        event.widget.configure(image=key_img)
        event.widget.image = key_img

    def on_key_pressed(self, event):
        play_note(event.widget.name)
        self.change_image_to_pressed(event)

    def on_key_released(self, event):
        print (event.widget.name + ' released')
        self.change_image_to_unpressed(event)


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

			
