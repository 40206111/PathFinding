
__author__ = 'Emma'
__project__ = 'Caves'


class PathFinder(object):

    # Method to do the search
    @staticmethod
    def FindPath(coords, connections, stepping):
        print("Calculating...")
        path = {}
        # Set start and end coordinates
        start = coords[0]
        end = coords[len(coords) - 1]
        # Initialise sets
        closedSet = set()
        openSet = {start}
        gScoreMap = {start: 0}
        fScoreMap = {start: PathFinder.SquaredDist(start, end)}

        # While openset isn't empty
        while openSet != {}:
            # set current to min score currently in the open set
            current = PathFinder.FindMin(openSet, fScoreMap, stepping)
            if stepping:
                input("current: " + str(current))
            # if goal reached
            if current == end:
                if stepping:
                    input("GOAL REACHED")
                else:
                    print("GOAL REACHED")
                # return path
                return PathFinder.GetPath(path, end)

            # Find the caves this node is connected too
            neighbours = PathFinder.FindNeighbours(current, coords, connections)
            # remove current from open set
            openSet.remove(current)
            # add current path to closed set
            closedSet.update([current])

            # loop through neighbours
            for n in neighbours:
                # ignore if neighbour is closed
                if n in closedSet:
                    continue
                # add to open set
                if n not in openSet:
                    openSet.update([n])
                if stepping:
                    print("Checking neighbour: " + str(n))
                # work out g score
                tempGScore = gScoreMap[current] + PathFinder.SquaredDist(current, n)

                # check if this is a better path than has already been worked out
                if n in gScoreMap and tempGScore >= gScoreMap[n]:
                    continue
                # update g score map
                gScoreMap.update({n: tempGScore})
                # update path
                path.update({n: current})
                # update f score
                fScoreMap.update({n: gScoreMap[n] + PathFinder.SquaredDist(n, end)})
        # Inform user no route was found
        print("NO ROUTE")
        return 1

    # Finding the minimum
    @staticmethod
    def FindMin(theSet, m, stepping):
        # Initialise min int and current min
        theMin = None
        currentMin = None

        # Loop through set
        for s in theSet:
            if stepping:
                print(str(s) + ": " + str(m[s]))
            # if Min hasn't been set yet
            if theMin is None:
                theMin = m[s]
                currentMin = s
            # if score in map is less than current min
            elif m[s] < m[currentMin]:
                # update mins
                theMin = m[s]
                currentMin = s
        # return current min
        return currentMin

    # Method to Find the neighbours of a coordinate
    @staticmethod
    def FindNeighbours(a, coords, connections):
        # initialise neighbors set
        neighbours = set()
        # set j to be index of coordinate
        j = coords.index(a)

        # loop through connections
        for i in range(0, len(connections[j])):
            # if there is a connection add coord to neighbours
            if connections[i][j] == 1:
                neighbours.add(coords[i])
        return neighbours

    # Method to find the squared euclidean distance as square rooting is slow
    @staticmethod
    def SquaredDist(a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

    # Method to return the path as list
    @staticmethod
    def GetPath(camefrom, current):
        # set path to a list containing current
        path = [current]

        while current in camefrom:
            # update current
            current = camefrom[current]
            path.append(current)
        # Return path reversed
        return path[::-1]


