import tkinter as tk
from tkinter import *

from math import sqrt

__author__ = 'Emma'
__project__ = 'Caves'


class Window(object):
    instance = None
    main = Tk()
    buttons = {}
    labels = {}
    size = 0
    can = None
    points = {}
    arrows = {}
    PPM = 30

    @staticmethod
    def button(name, txt, command):
        b = tk.Button(Window.main, text=txt, width=25, command=command)
        b.pack()
        Window.buttons.update({name: b})

    @staticmethod
    def Label(name, txt):
        L = tk.Label(Window.main, text=txt)
        L.pack()
        Window.labels.update({name: L})

    @staticmethod
    def createGrid(coords, connections):
        Window.can = Canvas(Window.main, width=Window.size[0] * Window.PPM, height=Window.size[1] * Window.PPM)
        oval_r = 10

        for i in range(0, len(connections)):
            for j in range(0, len(connections[i])):
                directionX = coords[i][0] - coords[j][0]
                directionY = coords[i][1] - coords[j][1]
                length = sqrt(directionX * directionX + directionY * directionY)
                if length != 0:
                    norm = tuple(((directionX / length), (directionY / length)))
                else:
                    norm = tuple((0, 0))
                offset = tuple(((oval_r * norm[0]), (oval_r * norm[1])))

                if connections[j][i] == 1:
                    a = Window.can.create_line(coords[j][0] * Window.PPM + offset[0],
                                               (Window.size[1]-1 - coords[j][1]) * Window.PPM - offset[1],
                                               (coords[i][0]) * Window.PPM - offset[0],
                                               (Window.size[1]-1 - coords[i][1]) * Window.PPM + offset[1],
                                               arrow=tk.FIRST)
                    Window.arrows.update({(coords[i], coords[j]): a})

        for i in range(0, len(coords)):
            p = Window.can.create_oval(coords[i][0] * Window.PPM - oval_r, (Window.size[1]-1 - coords[i][1]) * Window.PPM - oval_r,
                                       (coords[i][0] * Window.PPM) + oval_r, ((Window.size[1]-1 - coords[i][1]) * Window.PPM) + oval_r,
                                       fill='red', outline='red')
            Window.can.create_text(coords[i][0] * Window.PPM, (Window.size[1]-1 - coords[i][1]) * Window.PPM,
                                   fill='black', text=i+1, font='bold')
            Window.points.update({coords[i]: p})

        Window.can.pack()


    @staticmethod
    def removeButtons():
        for b in Window.buttons.items():
            b[1].destroy()
        for L in Window.labels.items():
            L[1].destroy()
        if Window.can is not None:
            Window.can.destroy()
        Window.buttons.clear()