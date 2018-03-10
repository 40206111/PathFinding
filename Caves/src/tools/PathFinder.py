
__author__ = 'Emma'
__project__ = 'Caves'

class PathFinder(object):

    #Method to step through the search
    @staticmethod
    def StepThrough(coords, connections):
        # Set start and end coordinates
        start = coords[0]
        end = coords[len(coords) - 1]

        # Initialise sets
        closedSet = {}
        openSet = {start}

        # While openset isn't empty
        while openSet != {}:
            openSet.clear()

        return 0

    # Method to do the search
    @staticmethod
    def FindFast(coords, connections):
        return 0

    #Method to find the squared distance as square rooting is slow
    @staticmethod
    def SquaredDist(a, b):
        return (b[0] - a[0])**2 + (b[1] - a[1])**2