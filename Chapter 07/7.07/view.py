'''
7.07

    Implementing the Score Maker

new imports here:
    from score_maker import ScoreMaker
    
   
methods modified here
    build_score_sheet_frame  # instantiated ScoreMaker
    on_progression_button_clicked
    find_chord
    find_scale

    
'''
from tkinter import Tk, Frame, Button, BOTH, Label, PhotoImage, \
    StringVar, OptionMenu, ttk, font
from functools import partial
import json
from collections import OrderedDict
from audio import play_note, play_scale_in_new_thread, \
    play_chord_in_new_thread
from constants import *
from score_maker import ScoreMaker

class PianoTutor:

    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title('Piano Tutor')
        self.keys = []
        self.progression_buttons = []
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
        with open(CHORDS_JSON_FILE, 'r') as f:
            self.chords = json.load(f, object_pairs_hook=OrderedDict)
        with open(PROGRESSIONS_JSON_FILE, 'r') as f:
            self.progressions = json.load(f,
                    object_pairs_hook=OrderedDict)

    def on_progression_scale_changed(self, event):
        selected_progression_scale = \
            self.progression_scale_selector.get()
        progressions = [k for k in
                        self.progressions[selected_progression_scale].keys()]
        self.progression_selector['values'] = progressions
        self.progression_selector.current(0)
        self.show_progression_buttons()

    def on_progression_key_changed(self, event):
        self.show_progression_buttons()

    def on_progression_changed(self, event):
        self.show_progression_buttons()

    def destroy_current_progression_buttons(self):
        for buttons in self.progression_buttons:
            buttons.destroy()

    def show_progression_buttons(self):
        self.destroy_current_progression_buttons()
        selected_progression_scale = \
            self.progression_scale_selector.get()
        selected_progression = self.progression_selector.get().split('-'
                )
        self.progression_buttons = []
        for i in range(len(selected_progression)):
            self.progression_buttons.append(Button(self.progressions_frame,
                    text=selected_progression[i],
                    command=partial(self.on_progression_button_clicked,
                    i)))
            sticky = ('W' if i == 0 else 'E')
            col = (i if i > 1 else 1)
            self.progression_buttons[i].grid(column=col, row=2,
                    sticky=sticky, padx=10)

    def on_progression_button_clicked(self, i):
        self.remove_all_key_highlights()
        selected_progression = self.progression_selector.get().split('-'
                )[i]
        if any(x.isupper() for x in selected_progression):
            selected_chord = 'Major'
        else:
            selected_chord = 'Minor'
        key_offset = ROMAN_TO_NUMBER[selected_progression]
        selected_key = self.progression_key_selector.get()
        index_of_selected_key = (KEYS.index(selected_key) + key_offset) \
            % 12
        self.keys_to_highlight = [ALL_KEYS[j + index_of_selected_key]
                                  for j in self.chords[selected_chord]]
        self.score_maker.draw_chord(self.keys_to_highlight)                                  
        self.highlight_list_of_keys(self.keys_to_highlight)
        play_chord_in_new_thread(self.keys_to_highlight)

    def on_chord_changed(self, event):
        self.remove_all_key_highlights()
        self.find_chord(event)

    def on_chords_key_changed(self, event):
        self.remove_all_key_highlights()
        self.find_chord(event)

    def find_chord(self, event=None):
        self.selected_chord = self.chords_selector.get()
        self.chords_selected_key = self.chords_key_selector.get()
        index_of_selected_key = KEYS.index(self.chords_selected_key)
        self.keys_to_highlight = [ALL_KEYS[i + index_of_selected_key]
                                  for i in
                                  self.chords[self.selected_chord]]
        self.score_maker.draw_chord(self.keys_to_highlight)                                  
        self.highlight_list_of_keys(self.keys_to_highlight)
        play_chord_in_new_thread(self.keys_to_highlight)

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
        self.keys_to_highlight = [ALL_KEYS[i + index_of_selected_key]
                                  for i in
                                  self.scales[self.selected_scale]]
        self.score_maker.draw_notes(self.keys_to_highlight)                                  
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
        self.mode_selector.grid(row=0, column=1, columnspan=3,
            padx=10, pady=10, sticky='nsew')
        self.mode_selector_frame.grid(row=0, column=0)

    def build_score_sheet_frame(self):
        self.score_sheet_frame = Frame(self.root, width=WINDOW_WIDTH,
                height=SCORE_DISPLAY_HEIGHT)
        self.score_sheet_frame.grid_propagate(False)
        self.score_sheet_frame.grid(row=1, column=0)
        self.score_maker = ScoreMaker(self.score_sheet_frame) 



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
                                  height=CONTROLS_FRAME_HEIGHT)
        self.scales_frame.grid(row=1, column=0, sticky='nsew')
        Label(self.scales_frame, text='Select scale').grid(row=0,
                column=1, sticky='w', padx=10, pady=1)
        self.scale_selector = ttk.Combobox(self.scales_frame, values=[k
                for k in self.scales.keys()])
        self.scale_selector.current(0)
        self.scale_selector.bind('<<ComboboxSelected>>',
                                 self.on_scale_changed)
        self.scale_selector.grid(row=1, column=1, sticky='e', padx=10,
                                 pady=10)
        Label(self.scales_frame, text='in the key of').grid(row=0,
                column=2, sticky='w', padx=10, pady=1)
        self.scale_key_selector = ttk.Combobox(self.scales_frame,
                values=[k for k in KEYS])
        self.scale_key_selector.current(0)
        self.scale_key_selector.bind('<<ComboboxSelected>>',
                self.on_scale_key_changed)
        self.scale_key_selector.grid(row=1, column=2, sticky='e',
                padx=10, pady=10)

    def build_chords_frame(self):
        self.chords_frame = Frame(self.controls_frame,
                                  width=WINDOW_WIDTH,
                                  height=CONTROLS_FRAME_HEIGHT)
        self.chords_frame.grid_propagate(False)
        self.chords_frame.grid(row=1, column=0, sticky='nsew')
        Label(self.chords_frame, text='Select Chord').grid(row=0,
                column=1, sticky='w', padx=10, pady=1)
        self.chords_selector = ttk.Combobox(self.chords_frame,
                values=[k for k in self.chords.keys()])
        self.chords_selector.current(0)
        self.chords_selector.bind('<<ComboboxSelected>>',
                                  self.on_chord_changed)
        self.chords_selector.grid(row=1, column=1, sticky='e', padx=10,
                                  pady=10)
        Label(self.chords_frame, text='in the key of').grid(row=0,
                column=2, sticky='w', padx=10, pady=1)
        self.chords_key_selector = ttk.Combobox(self.chords_frame,
                values=[k for k in KEYS])
        self.chords_key_selector.current(0)
        self.chords_key_selector.bind('<<ComboboxSelected>>',
                self.on_chords_key_changed)
        self.chords_key_selector.grid(row=1, column=2, sticky='e',
                padx=10, pady=10)

    def build_progressions_frame(self):
        self.progressions_frame = Frame(self.controls_frame,
                width=WINDOW_WIDTH, height=CONTROLS_FRAME_HEIGHT)
        self.progressions_frame.grid_propagate(False)
        self.progressions_frame.grid(row=1, column=0, sticky='nsew')
        Label(self.progressions_frame, text='Select Scale').grid(row=0,
                column=1, sticky='w', padx=10, pady=1)
        Label(self.progressions_frame, text='Select Progression'
              ).grid(row=0, column=2, sticky='w', padx=10, pady=1)
        Label(self.progressions_frame, text='in the Key of'
              ).grid(row=0, column=3, sticky='w', padx=10, pady=1)

        self.progression_scale_selector = \
            ttk.Combobox(self.progressions_frame, values=[k for k in
                         self.progressions.keys()], width=18)
        self.progression_scale_selector.bind('<<ComboboxSelected>>',
                self.on_progression_scale_changed)
        self.progression_scale_selector.current(0)
        self.progression_scale_selector.grid(row=1, column=1, sticky='w'
                , padx=10, pady=10)

        self.progression_selector = \
            ttk.Combobox(self.progressions_frame, values=[k for k in
                         self.progressions['Major'].keys()], width=18)
        self.progression_selector.bind('<<ComboboxSelected>>',
                self.on_progression_changed)
        self.progression_selector.current(0)
        self.progression_selector.grid(row=1, column=2, sticky='w',
                padx=10, pady=10)

        self.progression_key_selector = \
            ttk.Combobox(self.progressions_frame, values=KEYS, width=18)
        self.progression_key_selector.current(0)
        self.progression_key_selector.bind('<<ComboboxSelected>>',
                self.on_progression_key_changed)
        self.progression_key_selector.grid(row=1, column=3, sticky='w',
                padx=10, pady=10)

    def on_mode_changed(self, event):
        self.remove_all_key_highlights()
        selected_mode = self.mode_selector.get()
        if selected_mode == 'Scales':
            self.show_scales_frame()
            self.find_scale()
        elif selected_mode == 'Chords':
            self.show_chords_frame()
            self.find_chord()
        elif selected_mode == 'Chord Progressions':
            self.show_progressions_frame()
            self.show_progression_buttons()

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


			
