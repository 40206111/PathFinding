from tools.ReadCaverns import ReadCaverns
from os import listdir

__author__ = 'Emma'
__project__ = 'Caves'


# Menu method to choose cave file
def chooseFile():
    # Get files in correct directory
    files = listdir("../caves")

    # Loop for valid input
    while True:
        # print out files in directory
        for i in range(0, len(files)):
            print(str(i + 1) + ": " + files[i])
        # Print exit option
        print(str(len(files) + 1) + ": Exit")

        # Try to parse input
        try:
            # Set theIn to int
            theIn = int(input("Please choose cave file: "))
            # Check if input corresponds to file
            if 0 < theIn <= len(files):
                # Try to read from given file
                try:
                    # Print output from reading the caverns
                    chooseType(ReadCaverns.ReadCavern("../caves/" + files[theIn - 1]))
                    # Return true
                    return True
                except:
                    # Tell user what the problem is
                    print("ERROR: Invalid file, please choose a valid file")
            #  Exit if the user chooses to exit
            elif theIn == len(files) + 1:
                return False
            else:
                # Inform user of problem
                print("ERROR: value out of range")
        except:
            # Inform user of problem
            print("ERROR: Please enter a valid number")


def chooseType(coords, connections):
    print("1: Step Through")
    print("2: Find Fast")
    print("3: Back")

    while True:
        try:
            theIn = int(input("Please choose a search type: "))

            if theIn == 1:
                # Call step through
                return 0
            elif theIn == 2:
                # Call find fast
                return 0
            elif theIn == 3:
                return 1
        except:
            print("ERROR: Please enter a valid number")



def main():
    # Choose file to read
    if chooseFile():
        # For when running outside of pycharm to make sure it doesn't close immediately
        input("press enter to end")

    # Successful exit
    return 0


# Run main on start
if __name__ == "__main__":
    main()
