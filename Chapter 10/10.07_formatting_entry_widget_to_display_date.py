"""
Code illustration: 10.07
Formatting Entry Widget
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, Entry, Label, StringVar, INSERT


class FormatEntryWidgetDemo:

    def __init__(self, root):
        Label(root, text='Date(MM/DD/YYYY)').pack()
        self.entered_date = StringVar()
        self.date_entry = Entry(textvariable=self.entered_date)
        self.date_entry.pack(padx=5, pady=5)
        self.date_entry.focus_set()
        self.slash_positions = [2, 5]
        root.bind('<Key>', self.format_date_entry_widget)

    def format_date_entry_widget(self, event):
        entry_list = [c for c in self.entered_date.get() if c != '/']
        for pos in self.slash_positions:
            if len(entry_list) > pos:
                entry_list.insert(pos, '/')
        self.entered_date.set(''.join(entry_list))
        # Controlling cursor
        cursor_position = self.date_entry.index(
            INSERT)  # current cursor position
        for pos in self.slash_positions:
            if cursor_position == (pos + 1):  # if cursor position is on slash
                cursor_position += 1
        if event.keysym not in ['BackSpace', 'Right', 'Left', 'Up', 'Down']:
            self.date_entry.icursor(cursor_position)

root = Tk()
FormatEntryWidgetDemo(root)
root.mainloop()
