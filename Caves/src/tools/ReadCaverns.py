
__author__ = 'Emma'
__project__ = 'Caves'


class ReadCaverns(object):

    # Method to read from cavern file
    @staticmethod
    def ReadCavern(file):
        # check that it's a .cav file
        if ReadCaverns.CheckFile(file):
            # try to open the file
            try:
                f = open(file, "r")
                return ReadCaverns.GetData(f)
            except:
                # throw exception
                # DEBUG
                print("DEBUG: opening error")
                exec("ERROR: cannot open file, " + str(file));
            # Return file name
            return file
        else:
            # Throw exception
            #DEBUG
            print("DEBUG: Reading Error")
            exec("ERROR: invalid file")

    # Method to check for .cav files
    @staticmethod
    def CheckFile(file):
        # If the last 4 characters are .cav
        if (file[-4:]).lower() == '.cav':
            return True
        return False

    # Method to get data out of file
    @staticmethod
    def GetData(file):
        # Read file and split by commas
        data = file.read().split(',')
        # Set amount to first data in list
        amount = int(data[0].strip())
        # Use this a lot so storing it
        doubleAPlus = amount * 2 + 1
        # Initialise coords and connections
        coords = list()
        connections = []
        # Initialise j
        j = -1

        # Check that there aren't too many caves
        if amount <= 20:
            # Add coordinates to list of tuples
            for i in range(1, doubleAPlus - 1, 2):
                coords.append((int(data[i].strip()),  int(data[i+1].strip())))
            # Add data to "matrix" (list of lists)
            for i in range(doubleAPlus, doubleAPlus + amount * amount):
                # If at the end of matrix row add new list to matrix
                if (i - doubleAPlus) % amount == 0:
                    connections.append([])
                    j += 1
                connections[j].append((int(data[i].strip())))
            # Close file
            file.close()
            # *************DEBUG**************************
            ReadCaverns.PrintCavern(coords, connections)
            # Return data
            return coords, connections
        else:
            # Close file
            file.close()
            exec("ERROR: Too many caves")

    # Method to print cavern connections
    @staticmethod
    def PrintCavern(coords, connections):
        print('\t\t', end='')
        # Print all coords
        for c in coords:
            print(c, end='\t')
        print()
        # Print out connection matrix
        for i in range(0, len(coords)):
            print(coords[i], end='\t\t')
            for j in range(0, len(coords)):
                print(connections[i][j], end='\t\t')
            print("\n\n")
        print()
