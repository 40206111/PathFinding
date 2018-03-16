import tkinter as tk
from tkinter import *

__author__ = 'Emma'
__project__ = 'Caves'


class Window(object):
    instance = None
    main = None
    buttons = {}
    size = 0
    can = None
    points = {}
    arrows = {}
    PPM = 30

    def __init__(self):
        if Window.instance is None:
            self.create()
        return Window.instance

    def create(self):
        Window.main = Tk()
        Window.main.title("Path Finding")

    def button(self, name, txt, command):
        b = tk.Button(self.main, text=txt, width=25, command=command)
        b.pack()
        self.buttons.update({name: b})

    def gridHelp(self, pic):
        tk.Label(self.main, image=pic).pack()

    def createGrid(self, coords, connections):
        print(Window.size)
        Window.can = Canvas(Window.main, width=Window.size[0] * Window.PPM, height=Window.size[1] * Window.PPM)

        for i in range(0, len(connections)):
            for j in range(0, len(connections[i])):
                if connections[j][i] == 1:
                    a = Window.can.create_line(coords[j][0] * Window.PPM, (Window.size[1]-1 - coords[j][1]) * Window.PPM,
                                               coords[i][0] * Window.PPM, (Window.size[1]-1 - coords[i][1]) * Window.PPM, arrow=tk.FIRST)
                    Window.arrows.update({(coords[i], coords[j]): a})
        for c in coords:
            p = Window.can.create_oval(c[0] * Window.PPM - 5, (Window.size[1]-1 - c[1]) * Window.PPM - 5,
                                       (c[0] * Window.PPM) + 5, ((Window.size[1]-1 - c[1]) * Window.PPM) + 5,
                                       fill='red')
            Window.points.update({c: p})

        Window.can.pack()


    @staticmethod
    def removeButtons():
        for b in Window.buttons.items():
            b[1].destroy()
        if Window.can is not None:
            Window.can.destroy()
        Window.buttons.clear()