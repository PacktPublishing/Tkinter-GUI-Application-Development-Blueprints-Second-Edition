"""
Code illustration: 2.03

Adding View Menu Items to demonstrate
other Types of Menu Items
    1. Checkbutton menu-item
    2. Radiobutton menu-item
    3. Cascade menu-item

@Tkinter GUI Application Development Blueprints
"""

from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, IntVar, \
    StringVar


PROGRAM_NAME = "Footprint Editor"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

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
file_menu.add_command(label='New', accelerator='Ctrl+N',
                      compound='left', image=new_file_icon, underline=0)
file_menu.add_command(label='Open', accelerator='Ctrl+O',
                      compound='left', image=open_file_icon, underline=0)
file_menu.add_command(label='Save', accelerator='Ctrl+S',
                      compound='left', image=save_file_icon, underline=0)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S')
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4')
menu_bar.add_cascade(label='File', menu=file_menu)
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z',
                      compound='left', image=undo_icon)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y',
                      compound='left', image=redo_icon)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X',
                      compound='left', image=cut_icon)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C',
                      compound='left', image=copy_icon)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V',
                      compound='left', image=paste_icon)
edit_menu.add_separator()
edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F')
edit_menu.add_separator()
edit_menu.add_command(label='Select All', underline=7, accelerator='Ctrl+A')
menu_bar.add_cascade(label='Edit', menu=edit_menu)

##
# Implementing Checkbutton, Radiobutton and Cascade menu-items under View Menu in this iteration
##
view_menu = Menu(menu_bar, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(
    label='Show Cursor Location at Bottom', variable=show_cursor_info)
highlight_line = IntVar()
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1,
                          offvalue=0, variable=highlight_line)
themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

"""
color scheme is defined with dictionary elements like -
        theme_name : foreground_color.background_color
"""
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
    themes_menu.add_radiobutton(label=k, variable=theme_choice)
menu_bar.add_cascade(label='View', menu=view_menu)


#
# End of View menu implementation in this iteration
#

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About')
about_menu.add_command(label='Help')
menu_bar.add_cascade(label='About',  menu=about_menu)
root.config(menu=menu_bar)

shortcut_bar = Frame(root,  height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill='x')
line_number_bar = Text(root, width=4, padx=3, takefocus=0,  border=0,
                       background='khaki', state='disabled',  wrap='none')
line_number_bar.pack(side='left',  fill='y')

content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

root.mainloop()
