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

    # make a button for each file in directory
    for i in range(0, len(files)):
        dirButtons(files[i], i)

    # Create a button to Exit window
    Window.button("Exit", "Exit", Window.main.destroy)


# Method to be called by button to properly go back
def back():
    Window.removeButtons()
    chooseFile()


# Method for button to call to begin pathing
def Pathing(info, stepping):
    # Remove everything currently on window
    Window.removeButtons()
    # create visualisation of caves
    Window.createGrid(info[0], info[1])
    # Add label for path length to go in
    Window.Label("path", "")
    # Create next button if stepping
    if stepping:
        Window.button("Step", "Next", lambda: Window.var.set(1))
    # Create back button
    Window.button("back", "Menu", lambda: back())
    # Call pathfinder on cave system
    PathFinder.FindPath(info[0], info[1], stepping)

# Method to show options
def chooseType(info):
    # clear window
    Window.removeButtons()
    # create buttons
    Window.button("Stepping", "Step Through", lambda: Pathing(info, True))
    Window.button("Fast", "Find Fast", lambda: Pathing(info, False))
    Window.button("Back", "Back", lambda: back())


# Start method
def main():
    Window.main.title("Path Finder")
    # Choose file to read
    chooseFile()

    #window loop
    Window.main.mainloop()

    # Successful exit
    return 0


# Run main on start
if __name__ == "__main__":
    main()
