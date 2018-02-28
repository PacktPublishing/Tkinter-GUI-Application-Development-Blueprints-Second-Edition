"""
Code illustration: 7.09
    Port Scanner
Tkinter GUI Application Development Blueprints
"""
import socket
from tkinter import Tk, Label, Entry, Button, Frame, Scrollbar, W, EW, E, Text, \
    DISABLED, Y, BOTH, NORMAL, END
from threading import Thread


class PortScanner():

    stop = False
    url = "google.com"
    start_port = 70
    end_port = 85

    def __init__(self, root):
        self.root = root
        self.create_gui()

    def on_scan_button_clicked(self):
        self.empty_console()
        self.scan_in_a_new_thread()

    def empty_console(self):
        self.console_text.config(state=NORMAL)
        self.console_text.delete("1.0", END)
        self.console_text.config(state=DISABLED)

    def scan_in_a_new_thread(self):
        url = self.host_entry.get()
        start_port = int(self.start_port_entry.get())
        end_port = int(self.end_port_entry.get())
        thread = Thread(target=self.start_scan,
                        args=(url, start_port, end_port))
        thread.start()

    def start_scan(self, url, start_port, end_port):
        for port in range(start_port, end_port + 1):
            if not self.stop:
                self.output_to_console("Scanning port {}".format(port))
                if self.is_port_open(url, port):
                    self.output_to_console(" -- Port {} open \n".format(port))
                else:
                    self.output_to_console("-- Port {} closed \n".format(port))

    def is_port_open(self, url, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((socket.gethostbyname(url), port))
            s.close()
            return True
        except:
            return False

    def on_stop_button_clicked(self):
        self.stop = True

    def output_to_console(self, new_text):
        self.console_text.config(state=NORMAL)
        self.console_text.insert(END, new_text)
        self.console_text.see(END)
        self.console_text.config(state=DISABLED)

    def create_gui(self):
        Label(self.root, text='Host :').grid(row="1", column="1", sticky=W)
        self.host_entry = Entry(self.root)
        self.host_entry.insert(0, self.url)
        self.host_entry.grid(row="1", column="2", sticky=EW)
        Label(self.root, text='Start Port :').grid(
            row="2", column="1", sticky=W)
        self.start_port_entry = Entry(self.root)
        self.start_port_entry.insert(0, self.start_port)
        self.start_port_entry.grid(row="2", column="2", sticky=EW)
        Label(self.root, text='End Port :').grid(row="3", column="1", sticky=W)
        self.end_port_entry = Entry(self.root)
        self.end_port_entry.insert(0, self.end_port)
        self.end_port_entry.grid(row="3", column="2", sticky=EW)
        Button(self.root, text='Scan', command=self.on_scan_button_clicked).grid(
            row="4", column="2", sticky=E)
        Button(self.root, text='Stop', command=self.on_stop_button_clicked).grid(
            row="4", column="2", sticky=W)
        Label(self.root, text='Scan Result :').grid(
            row="5", column="1", sticky=W)
        console_frame = Frame(self.root)
        console_frame.grid(row="6", column="1", columnspan="2")
        self.console_text = Text(
            console_frame, fg="green", bg="black", state=DISABLED)
        scrollbar = Scrollbar(console_frame, command=self.console_text.yview)
        scrollbar.pack(side="right", fill=Y)
        self.console_text.pack(expand=1, fill=BOTH)
        self.console_text['yscrollcommand'] = scrollbar.set

if __name__ == '__main__':
    root = Tk()
    PortScanner(root)
    root.mainloop()
