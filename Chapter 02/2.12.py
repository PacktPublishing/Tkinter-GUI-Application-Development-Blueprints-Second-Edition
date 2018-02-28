"""
Code illustration: 2.12.py
Features Added:
    Add context/ Pop-up Menu
    Set focus on launch

@Tkinter GUI Application Development Blueprints
"""

import os
from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, IntVar, \
    StringVar, BooleanVar, Button, END, Label, INSERT
import tkinter.filedialog
import tkinter.messagebox

PROGRAM_NAME = "Footprint Editor"
file_name = None

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

# show pop-up menu


def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


def show_cursor_info_bar():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor_info_bar(event=None):
    row, col = content_text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(
        background=background_color, fg=foreground_color)


def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')


def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add(
        "active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()


def on_content_changed(event=None):
    update_line_numbers()
    update_cursor_info_bar()


def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output


def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo(
        "About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI Application\n Development Blueprints"))


def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo(
        "Help", "Help Book: \nTkinter GUI Application\n Development Blueprints",
        icon='question')


def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
        root.destroy()


def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)
    on_content_changed()


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())
        on_content_changed()


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        tkinter.messagebox.showwarning("Save", "Could not save the file.")


def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return "break"


def find_text(event=None):
    search_toplevel = Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)

    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')

    search_entry_widget = Entry(
        search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(
        row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0,
           command=lambda: search_output(
               search_entry_widget.get(), ignore_case_value.get(),
               content_text, search_toplevel, search_entry_widget)
           ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(needle, if_ignore_case, content_text,
                  search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
                                            nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return "break"


def copy():
    content_text.event_generate("<<Copy>>")
    return "break"


def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return "break"


def undo():
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return "break"


def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return 'break'

new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left',
                      image=new_file_icon, underline=0, command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left',
                      image=open_file_icon, underline=0, command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S',
                      compound='left', image=save_file_icon, underline=0, command=save)
file_menu.add_command(
    label='Save as', accelerator='Shift+Ctrl+S', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z',
                      compound='left', image=undo_icon, command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y',
                      compound='left', image=redo_icon, command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X',
                      compound='left', image=cut_icon, command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C',
                      compound='left', image=copy_icon, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V',
                      compound='left', image=paste_icon, command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find', underline=0,
                      accelerator='Ctrl+F', command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', underline=7,
                      accelerator='Ctrl+A', command=select_all)
menu_bar.add_cascade(label='Edit', menu=edit_menu)


view_menu = Menu(menu_bar, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number,
                          command=update_line_numbers)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(
    label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor_info_bar)
to_highlight_line = BooleanVar()
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1,
                          offvalue=0, variable=to_highlight_line, command=toggle_highlight)
themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}

theme_choice = StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(
        label=k, variable=theme_choice, command=change_theme)
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', command=display_about_messagebox)
about_menu.add_command(label='Help', command=display_help_messagebox)
menu_bar.add_cascade(label='About',  menu=about_menu)
root.config(menu=menu_bar)

shortcut_bar = Frame(root,  height=25)
shortcut_bar.pack(expand='no', fill='x')

icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste',
         'undo', 'redo', 'find_text')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon))
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')

line_number_bar = Text(root, width=4, padx=3, takefocus=0,  border=0,
                       background='khaki', state='disabled',  wrap='none')
line_number_bar.pack(side='left',  fill='y')

content_text = Text(root, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


content_text.bind('<KeyPress-F1>', display_help_messagebox)
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='ivory2')

# set up the pop-up menu
popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=select_all)
content_text.bind('<Button-3>', show_popup_menu)


# bind right mouse click to show pop up and set focus to text widget on launch
content_text.bind('<Button-3>', show_popup_menu)
content_text.focus_set()

root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()
