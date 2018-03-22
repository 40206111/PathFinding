from tools.ReadCaverns import ReadCaverns
from tools.PathFinder import PathFinder
from tools.Window import Window
from os import listdir

__author__ = 'Emma'
__project__ = 'Caves'


# Create Directory buttons, doesn't work properly in single loop for some reason
def dirButtons(file, i):
    Window.button("Button" + str(i), file, lambda: chooseType(ReadCaverns.ReadCavern("../caves/" + file, "button" + str(i))))


# Menu method to choose cave file
def chooseFile():
    # Get files in correct directory
    files = listdir("../caves")

    for i in range(0, len(files)):
        dirButtons(files[i], i)

    Window.button("Exit", "Exit", Window.main.destroy)


def back():
    for b in Window.buttons.items():
        b[1].destroy()
    chooseFile()


def Pathing(info, stepping):
    Window.removeButtons()
    Window.createGrid(info[0], info[1])
    Window.button("back", "Menu", lambda: toMenu())
    PathFinder.FindPath(info[0], info[1])

def toMenu():
    Window.removeButtons()
    chooseFile()


def chooseType(info):
    Window.removeButtons()

    Window.button("Stepping", "Step Through", lambda: Pathing(info, True))
    Window.button("Fast", "Find Fast", lambda: Pathing(info, False))
    Window.button("Back", "Back", lambda: back())


def main():
    Window.main.title("Path Finder")
    # Choose file to read
    chooseFile();
    Window.main.mainloop()

    # Successful exit
    return 0


# Run main on start
if __name__ == "__main__":
    main()
