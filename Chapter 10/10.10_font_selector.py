"""
Code illustration: 10.10
Font Selector
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, StringVar, Label, Entry, Text, BooleanVar, Checkbutton, \
        INSERT, DISABLED, ttk, font


class FontSelectorDemo():

    def __init__(self):
        self.current_font = font.Font(font=('Times New Roman', 12))
        self.family = StringVar(value='Times New Roman')
        self.size = StringVar(value='12')
        self.weight = StringVar(value=font.NORMAL)
        self.slant = StringVar(value=font.ROMAN)
        self.underline = BooleanVar(value=False)
        self.overstrike = BooleanVar(value=False)
        self.sample_text = 'The quick brown fox jumps over the lazy dog'
        self.gui_creator()

    def gui_creator(self):
        # font family selector combobox
        Label(text='Font Family').grid(row=0, column=0)
        font_list = ttk.Combobox(textvariable=self.family)
        font_list.grid(
            row=1, column=0, columnspan=2, sticky='nsew', padx=10)
        font_list.bind('<<ComboboxSelected>>', self.on_value_change)
        all_fonts = list(font.families())
        all_fonts.sort()
        font_list['values'] = all_fonts
        # Font Sizes
        Label(text='Font Size').grid(row=0, column=2)
        sizeList = ttk.Combobox(textvariable=self.size)
        sizeList.bind('<<ComboboxSelected>>', self.on_value_change)
        sizeList.grid(
            row=1, column=2, columnspan=2, sticky='nsew', padx=10)
        all_sizes = list(range(6, 70))
        sizeList['values'] = all_sizes
        # Font Styles
        Checkbutton(text='bold',  variable=self.weight, command=self.on_value_change,
                    onvalue='bold', offvalue='normal').grid(row=2, column=0)
        Checkbutton(text='italic', variable=self.slant, command=self.on_value_change,
                    onvalue='italic', offvalue='roman').grid(row=2, column=1)
        Checkbutton(text='underline', variable=self.underline,
                    command=self.on_value_change, onvalue=True, offvalue=False).grid(row=2, column=2)
        Checkbutton(text='overstrike', variable=self.overstrike,
                    command=self.on_value_change,  onvalue=True, offvalue=False).grid(row=2, column=3)
        self.text = Text()
        self.text.columnconfigure(1, weight=1)
        self.text.grid(
            row=3, column=0, columnspan=10, padx=10, pady=10, sticky='ew')
        self.text.insert(INSERT, '{}\n{}'.format(
            self.sample_text, self.sample_text.upper()), 'fontspecs')
        self.text.config(state=DISABLED)

    def on_value_change(self, event=None):
        self.current_font.config(family=self.family.get(),
                                 size=self.size.get(), weight=self.weight.get(),
                                 slant=self.slant.get(), underline=self.underline.get(),
                                 overstrike=self.overstrike.get())
        self.text.tag_config('fontspecs', font=self.current_font)


if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    font = FontSelectorDemo()
    root.mainloop()
