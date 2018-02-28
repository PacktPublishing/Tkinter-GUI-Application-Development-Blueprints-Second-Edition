'''
Code illustration: 9.10
    Chat Client

    *** NOTE  Run atleast 2 instances of this program to see chat in action***

Tkinter GUI Application Development Blueprints
'''

from tkinter import Tk, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL
import socket
import threading
from tkinter import messagebox


class ChatClient:

    client_socket = None
    last_received_message = None

    def __init__(self, root):
        self.root = root
        self.initialize_socket()
        self.initialize_gui()
        self.listen_for_incoming_messages_in_a_thread()

    def initialize_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_ip = '127.0.0.1'
        remote_port = 10319
        self.client_socket.connect((remote_ip, remote_port))

    def initialize_gui(self):
        self.display_name_section()
        self.display_chat_transcript()
        self.display_chat_entrybox()

    def listen_for_incoming_messages_in_a_thread(self):
        t = threading.Thread(
            target=self.recieve_message_from_server, args=(self.client_socket,))
        t.start()

    def recieve_message_from_server(self, so):
        while True:
            buf = so.recv(256)
            if not buf:
                break
            self.chat_transcript_area.insert('end', buf.decode('utf-8') + '\n')
            self.chat_transcript_area.yview(END)
        so.close()

    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Enter your name:').pack(side='left')
        self.name_widget = Entry(frame, width=20)
        self.name_widget.pack(side='left', anchor='e')
        frame.pack(side='top', anchor='w')

    def display_chat_transcript(self):
        frame = Frame()
        Label(frame, text='Chat Transcript:').pack(side='top', anchor='w')
        self.chat_transcript_area = Text(frame, width=60, height=20)
        scrollbar = Scrollbar(
            frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.pack(side='left')
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

    def display_chat_entrybox(self):
        frame = Frame()
        Label(frame, text='Enter chat messages:').pack(side='top', anchor='w')
        self.enter_text_widget = Text(frame, width=60, height=8)
        scrollbar = Scrollbar(
            self.root, command=self.enter_text_widget.yview, orient=VERTICAL)
        self.enter_text_widget.config(yscrollcommand=scrollbar.set)
        self.enter_text_widget.pack(side='left')
        scrollbar.pack(side='right', fill='y')
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top')

    def on_enter_key_pressed(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror(
                "Enter your name", "Enter your name to send a message")
            return
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.name_widget.get().strip() + ":"
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

if __name__ == '__main__':
    root = Tk()
    ChatClient(root)
    root.mainloop()
