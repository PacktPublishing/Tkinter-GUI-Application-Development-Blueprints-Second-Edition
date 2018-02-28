"""
Code illustration: 5.03
    
    New imports here:
        import os
    
    Methods modified here:
        on_add_file_button_clicked()
        on_remove_selected_button_clicked()
        on_add_directory_button_clicked()
        on_clear_play_list_button_clicked()
        
    New methods added here:
        add_audio_file()
        remove_selected_files()
        add_all_audio_files_from_directory() 
        get_all_audio_file_from_directory(directory_path)
        clear_play_list()
        

@Tkinter GUI Application Development Blueprints
"""
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import os
import model
import player

AUDIO_PLAYER_NAME = "Achtung Baby"


class View:

    loop_choices = [("No Loop", 1), ("Loop Current", 2), ("Loop All", 3)]

    def __init__(self, root, model, player):
        self.root = root
        self.model = model
        self.player = player
        self.create_gui()

    def create_gui(self):
        self.root.title(AUDIO_PLAYER_NAME)
        self.create_top_display()
        self.create_button_frame()
        self.create_list_box()
        self.create_bottom_frame()
        self.create_context_menu()

    def create_top_display(self):
        frame = tk.Frame(self.root)
        glass_frame_image = tk.PhotoImage(file='../icons/glass_frame.gif')
        self.canvas = tk.Canvas(frame, width=370, height=90)
        self.canvas.image = glass_frame_image
        self.canvas.grid(row=1)
        self.console = self.canvas.create_image(
            0, 10, anchor=tk.NW, image=glass_frame_image)
        self.clock = self.canvas.create_text(125, 68, anchor=tk.W, fill='#CBE4F6',
                                             text="00:00")
        self.track_length_text = self.canvas.create_text(167, 68, anchor=tk.W, fill='#CBE4F6',
                                                         text="of 00:00")
        self.track_name = self.canvas.create_text(50, 35, anchor=tk.W, fill='#9CEDAC',
                                                  text='\"Currently playing: none \"')
        frame.grid(row=1, pady=1, padx=0)

    def create_button_frame(self):
        frame = tk.Frame(self.root)
        previous_track_icon = tk.PhotoImage(file='../icons/previous_track.gif')
        previous_track_button = tk.Button(
            frame, image=previous_track_icon, borderwidth=0, padx=0, command=self.on_previous_track_button_clicked)
        previous_track_button.image = previous_track_icon
        previous_track_button.grid(row=3, column=1, sticky='w')

        rewind_icon = tk.PhotoImage(file='../icons/rewind.gif')
        rewind_button = tk.Button(
            frame, image=rewind_icon, borderwidth=0, padx=0, command=self.on_rewind_button_clicked)
        rewind_button.image = rewind_icon
        rewind_button.grid(row=3, column=2, sticky='w')

        self.play_icon = tk.PhotoImage(file='../icons/play.gif')
        self.stop_icon = tk.PhotoImage(file='../icons/stop.gif')
        self.play_stop_button = tk.Button(
            frame, image=self.play_icon, borderwidth=0, padx=0, command=self.on_play_stop_button_clicked)
        self.play_stop_button.image = self.play_icon
        self.play_stop_button.grid(row=3, column=3)

        pause_icon = tk.PhotoImage(file='../icons/pause.gif')
        pause_unpause_button = tk.Button(
            frame, image=pause_icon, borderwidth=0, padx=0, command=self.on_pause_unpause_button_clicked)
        pause_unpause_button.image = pause_icon
        pause_unpause_button.grid(row=3, column=4)

        fast_forward_icon = tk.PhotoImage(file='../icons/fast_forward.gif')
        fast_forward_button = tk.Button(
            frame, image=fast_forward_icon, borderwidth=0, padx=0, command=self.on_fast_forward_button_clicked)
        fast_forward_button.image = fast_forward_icon
        fast_forward_button.grid(row=3, column=5)

        next_track_icon = tk.PhotoImage(file='../icons/next_track.gif')
        next_track_button = tk.Button(
            frame, image=next_track_icon, borderwidth=0, padx=0, command=self.on_next_track_button_clicked)
        next_track_button.image = next_track_icon
        next_track_button.grid(row=3, column=6)

        self.mute_icon = tk.PhotoImage(file='../icons/mute.gif')
        self.unmute_icon = tk.PhotoImage(file='../icons/unmute.gif')
        self.mute_unmute_button = tk.Button(
            frame, image=self.unmute_icon, text='unmute', borderwidth=0, padx=0, command=self.on_mute_unmute_button_clicked)
        self.mute_unmute_button.image = self.unmute_icon
        self.mute_unmute_button.grid(row=3, column=7)

        self.volume_scale = tkinter.ttk.Scale(
            frame, from_=0.0, to=1.0, command=self.on_volume_scale_changed)
        self.volume_scale.set(0.6)
        self.volume_scale.grid(row=3, column=8, padx=5)

        frame.grid(row=3, columnspan=5, sticky='w', pady=4, padx=5)

    def create_list_box(self):
        frame = tk.Frame(self.root)
        self.list_box = tk.Listbox(frame, activestyle='none', cursor='hand2',
                                   bg='#1C3D7D', fg='#A0B9E9', selectmode=tk.EXTENDED, height=10)
        self.list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.list_box.bind(
            "<Double-Button-1>", self.on_play_list_double_clicked)
        self.list_box.bind("<Button-3>", self.show_context_menu)
        scroll_bar = tk.Scrollbar(frame)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.list_box.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.list_box.yview)
        frame.grid(row=4, padx=5, columnspan=10, sticky='ew')

    def create_bottom_frame(self):
        frame = tk.Frame(self.root)

        add_file_icon = tk.PhotoImage(file='../icons/add_file.gif')
        add_file_button = tk.Button(frame, image=add_file_icon, borderwidth=0,
                                    padx=0, text='Add File', command=self.on_add_file_button_clicked)
        add_file_button.image = add_file_icon
        add_file_button.grid(row=5, column=1)

        remove_selected_icon = tk.PhotoImage(
            file='../icons/delete_selected.gif')
        remove_selected_button = tk.Button(
            frame, image=remove_selected_icon, borderwidth=0, padx=0, text='Delete', command=self.on_remove_selected_button_clicked)
        remove_selected_button.image = remove_selected_icon
        remove_selected_button.grid(row=5, column=2)

        add_directory_icon = tk.PhotoImage(file='../icons/add_directory.gif')
        add_directory_button = tk.Button(frame, image=add_directory_icon, borderwidth=0,
                                         padx=0, text='Add Dir', command=self.on_add_directory_button_clicked)
        add_directory_button.image = add_directory_icon
        add_directory_button.grid(row=5, column=3)

        empty_play_list_icon = tk.PhotoImage(
            file='../icons/clear_play_list.gif')
        empty_play_list_button = tk.Button(frame, image=empty_play_list_icon, borderwidth=0,
                                           padx=0, text='Clear All', command=self.on_clear_play_list_button_clicked)
        empty_play_list_button.image = empty_play_list_icon
        empty_play_list_button.grid(row=5, column=4)

        self.loop_value = tk.IntVar()
        self.loop_value.set(3)
        for txt, val in self.loop_choices:
            tk.Radiobutton(frame, text=txt, variable=self.loop_value, value=val).grid(
                row=5, column=4 + val, pady=3)

        frame.grid(row=5, sticky='w', padx=5)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self.list_box, tearoff=0)
        self.context_menu.add_command(
            label="Delete", command=self.on_remove_selected_context_menu_clicked)

    def show_context_menu(self, event):
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def on_add_file_button_clicked(self):
        self.add_audio_file()

    def on_remove_selected_button_clicked(self):
        self.remove_selected_files()

    def on_add_directory_button_clicked(self):
        self.add_all_audio_files_from_directory()

    def on_clear_play_list_button_clicked(self):
        self.clear_play_list()

    def on_remove_selected_context_menu_clicked(self):
        self.remove_selected_files()

    def on_previous_track_button_clicked(self):
        pass

    def on_rewind_button_clicked(self):
        pass

    def on_play_stop_button_clicked(self):
        pass

    def on_pause_unpause_button_clicked(self):
        pass

    def on_mute_unmute_button_clicked(self):
        pass

    def on_fast_forward_button_clicked(self):
        pass

    def on_next_track_button_clicked(self):
        pass

    def on_volume_scale_changed(self, value):
        pass

    def on_play_list_double_clicked(self, event=None):
        pass

    def add_audio_file(self):
        audio_file = tkinter.filedialog.askopenfilename(filetypes=[(
            'All supported', '.mp3 .wav'), ('.mp3 files', '.mp3'), ('.wav files', '.wav')])
        if audio_file:
            self.model.add_to_play_list(audio_file)
            file_path, file_name = os.path.split(audio_file)
            self.list_box.insert(tk.END, file_name)

    def remove_selected_files(self):
        try:
            selected_indexes = self.list_box.curselection()
            for index in reversed(selected_indexes):
                self.list_box.delete(index)
                self.model.remove_item_from_play_list_at_index(index)
        except IndexError:
            pass

    def add_all_audio_files_from_directory(self):
        directory_path = tkinter.filedialog.askdirectory()
        if not directory_path:
            return
        audio_files_in_directory = self.get_all_audio_file_from_directory(
            directory_path)
        for audio_file in audio_files_in_directory:
            self.model.add_to_play_list(audio_file)
            file_path, file_name = os.path.split(audio_file)
            self.list_box.insert(tk.END, file_name)

    def get_all_audio_file_from_directory(self, directory_path):
        audio_files_in_directory = []
        for (dirpath, dirnames, filenames) in os.walk(directory_path):
            for audio_file in filenames:
                if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
                    audio_files_in_directory.append(dirpath + "/" + audio_file)
        return audio_files_in_directory

    def clear_play_list(self):
        self.model.clear_play_list()
        self.list_box.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(width=False, height=False)
    model = model.Model()
    player = player.Player()
    app = View(root, model, player)
    root.mainloop()
