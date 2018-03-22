import tkinter as tk
from tkinter import *
from math import sqrt

__author__ = 'Emma'
__project__ = 'Caves'


# "Static" Class to create and manage window
class Window(object):
##### static Variables #####
    main = Tk()
    size = 0
    # Variable to Scale canvas up
    PPM = 40
    # Variable to set for button waiting
    var = tk.IntVar()
    # Items drawn on window
    can = None
    buttons = {}
    labels = {}
    points = {}
    arrows = {}

    # Method to create button on window
    @staticmethod
    def button(name, txt, command):
        b = tk.Button(Window.main, text=txt, width=25, command=command)
        b.pack()
        # Add button to set of buttons
        Window.buttons.update({name: b})

    # Method to add Label to Window
    @staticmethod
    def Label(name, txt):
        l = tk.Label(Window.main, text=txt)
        l.pack()
        # Add label to labels
        Window.labels.update({name: l})

    # Method to create cave system on canvas
    @staticmethod
    def createGrid(coords, connections):
        # Create canvas to size
        Window.can = Canvas(Window.main, width=Window.size[0] * Window.PPM, height=Window.size[1] * Window.PPM)
        # Set oval radius
        oval_r = 10

        # Loop through connections
        for i in range(0, len(connections)):
            for j in range(0, len(connections[i])):
                # If there is a connection
                if connections[j][i] == 1:
                    # Calculate offset
                    directionX = coords[i][0] - coords[j][0]
                    directionY = coords[i][1] - coords[j][1]
                    length = sqrt(directionX * directionX + directionY * directionY)
                    if length != 0:
                        norm = tuple(((directionX / length), (directionY / length)))
                    else:
                        norm = tuple((0, 0))
                    offset = tuple(((oval_r * norm[0]), (oval_r * norm[1])))

                    # create arrow
                    a = Window.can.create_line(coords[j][0] * Window.PPM + offset[0],
                                               (Window.size[1]-1 - coords[j][1]) * Window.PPM - offset[1],
                                               (coords[i][0]) * Window.PPM - offset[0],
                                               (Window.size[1]-1 - coords[i][1]) * Window.PPM + offset[1],
                                               arrow=tk.FIRST)
                    # Add arrow to list
                    Window.arrows.update({(coords[i], coords[j]): a})

        # Loop through coords
        for i in range(0, len(coords)):
            # Create oval at coord
            p = Window.can.create_oval(coords[i][0] * Window.PPM - oval_r, (Window.size[1]-1 - coords[i][1]) * Window.PPM - oval_r,
                                       (coords[i][0] * Window.PPM) + oval_r, ((Window.size[1]-1 - coords[i][1]) * Window.PPM) + oval_r,
                                       fill='red', outline='red')
            # Create Number in oval
            Window.can.create_text(coords[i][0] * Window.PPM, (Window.size[1]-1 - coords[i][1]) * Window.PPM,
                                   fill='black', text=i+1, font='bold')
            # Update points
            Window.points.update({coords[i]: p})

        # Pack canvas
        Window.can.pack()


    # Method to clear canvas
    @staticmethod
    def removeButtons():
        # Destroy all buttons
        for b in Window.buttons.items():
            b[1].destroy()
        # Destroy all labels
        for L in Window.labels.items():
            L[1].destroy()
        # Destroy canvas
        if Window.can is not None:
            Window.can.destroy()
        # clear sets
        Window.buttons.clear()
        Window.labels.clear()
        Window.arrows.clear()