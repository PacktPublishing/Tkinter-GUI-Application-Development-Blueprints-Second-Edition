"""
Code illustration: 3.02
    - Defining & Initializing the Data Structure

Chapter 3 : Programmable Drum Machine
Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk

PROGRAM_NAME = ' Explosion Drum Machine '
MAX_NUMBER_OF_PATTERNS = 10
MAX_NUMBER_OF_DRUM_SAMPLES = 5
INITIAL_NUMBER_OF_UNITS = 4
INITIAL_BPU = 4
INITIAL_BEATS_PER_MINUTE = 240


class DrumMachine:

    def __init__(self, root):
        self.root = root
        self.root.title(PROGRAM_NAME)
        self.beats_per_minute = INITIAL_BEATS_PER_MINUTE
        self.all_patterns = [None] * MAX_NUMBER_OF_PATTERNS
        self.init_all_patterns()

    def init_all_patterns(self):
        self.all_patterns = [
            {
                'list_of_drum_files': [None] * MAX_NUMBER_OF_DRUM_SAMPLES,
                'number_of_units': INITIAL_NUMBER_OF_UNITS,
                'bpu': INITIAL_BPU,
                'is_button_clicked_list':
                self.init_is_button_clicked_list(
                    MAX_NUMBER_OF_DRUM_SAMPLES,
                    INITIAL_NUMBER_OF_UNITS * INITIAL_BPU
                )
            }
            for k in range(MAX_NUMBER_OF_PATTERNS)]

    def init_is_button_clicked_list(self, num_of_rows, num_of_columns):
        return [[False] * num_of_columns for x in range(num_of_rows)]


if __name__ == '__main__':
    root = Tk()
    DrumMachine(root)
    root.mainloop()
