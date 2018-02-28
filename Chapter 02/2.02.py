"""
Code illustration: 2.02
Text Editor Code
Step 3: Adding  Menu items to each menu
Step 4: Adding labels to hold shortcut toolbar and line number

@Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar


PROGRAM_NAME = "Footprint Editor"

root = Tk()
root.geometry('350x350')
root.title(PROGRAM_NAME)

# getting icons ready for compound menu
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')

menu_bar = Menu(root)  # menu begins

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


view_menu = Menu(menu_bar, tearoff=0)
# View menu-items displays some variations
# so we tackle view menu code to be entered here in a later section
menu_bar.add_cascade(label='View', menu=view_menu)


about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About')
about_menu.add_command(label='Help')
menu_bar.add_cascade(label='About',  menu=about_menu)

root.config(menu=menu_bar)  # menu ends

# add top shortcut bar & left line number bar
shortcut_bar = Frame(root,  height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill='x')

line_number_bar = Text(root, width=4, padx=3, takefocus=0,  border=0,
                       background='khaki', state='disabled',  wrap='none')
line_number_bar.pack(side='left',  fill='y')


# add the main content Text widget and Scrollbar widget
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

root.mainloop()
