import tkinter as tk

__author__ = 'Emma'
__project__ = 'Caves'


class Window(object):
    instance = None
    main = None
    buttons = {}

    def __init__(self):
        if Window.instance is None:
            self.create()
        return Window.instance

    def create(self):
        Window.main = tk.Tk()
        Window.main.title("Path Finding")

    def button(self, name, txt, command):
        b = tk.Button(self.main, text=txt, width=25, command=command)
        b.pack()
        self.buttons.update({name: b})
