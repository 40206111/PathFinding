
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
                # close file
                f.close()
            except:
                # throw exception
                exec("ERROR: cannot open file, " + str(file));
            # Return file name
            return file
        else:
            # Throw exception
            exec("ERROR: invalid file")

    # Method to check for .cav files
    @staticmethod
    def CheckFile(file):
        # If the last 4 characters are .cav
        if (file[-4:]).lower() == '.cav':
            return True
        return False

