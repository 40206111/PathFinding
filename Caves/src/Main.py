from tools.ReadCaverns import ReadCaverns
from tools.PathFinder import PathFinder
from tools.Window import Window
from os import listdir

__author__ = 'Emma'
__project__ = 'Caves'


# Create Directory buttons, doesn't work properly in single loop for some reason
def dirButtons(win, file, i):
    win.button(win, "button" + str(i), file, lambda: chooseType(ReadCaverns.ReadCavern("../caves/" + file, "button" + str(i))))

# Menu method to choose cave file
def chooseFile():
    # Get files in correct directory
    files = listdir("../caves")

    for i in range(0, len(files)):
        dirButtons(Window, files[i], i)

    Window.button(Window, "Exit", "Exit", Window.main.destroy)


def back():
    for b in Window.buttons.items():
        b[1].destroy()
    chooseFile()

def Pathing(info, stepping):
    for b in Window.buttons.items():
        b[1].destroy()
    #Window.main.geometry(str(Window.size[0] * 10) + 'x' + str(Window.size[1] * 10))
    Window.createGrid(Window, info[0])
    PathFinder.FindPath(info[0], info[1], stepping)

def chooseType(info):
    for b in Window.buttons.items():
        b[1].destroy()
    Window.buttons.clear()

    Window.button(Window, "Stepping", "Step Through", lambda: Pathing(info, True))
    Window.button(Window, "Fast", "Find Fast", lambda: Pathing(info, False))
    Window.button(Window, "Back", "Back", lambda: back())


def main():
    Window()
    # Choose file to read
    chooseFile();
    Window.main.mainloop()

    # Successful exit
    return 0


# Run main on start
if __name__ == "__main__":
    main()
