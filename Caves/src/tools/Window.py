import tkinter as tk

__author__ = 'Emma'
__project__ = 'Caves'


class Window(object):
    instance = None
    main = None
    buttons = {}

    def __init__(self):
        if self.instance is None:
            self.create()
        return self.instance

    def create(self):
        self.main = tk.Tk()
        self.main.title("Path Finding")

    def button(self, name, file, command):
        b = tk.Button(self.main, text=file, width=25, command=command)
        b.pack()
        self.buttons.update({name: b})
