__author__ = 'Emma'
__project__ = 'Caves'


class PathFinder(object):
    # Method to step through the search
    @staticmethod
    def StepThrough(coords, connections):

        return 0

    # Method to do the search
    @staticmethod
    def FindFast(coords, connections):
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
            current = PathFinder.FindMin(openSet, fScoreMap)
            neighbours = PathFinder.FindNeighbours(current, coords, connections)
            openSet.remove(current)
            closedSet.update(current)

            if current == end:
                print("GOAL REACHED")
                return PathFinder.GetPath(path, end)

            for n in neighbours:
                if n in closedSet:
                    continue
                if n not in openSet:
                    openSet.update([n])

                tempGScore = gScoreMap[current] + PathFinder.SquaredDist(n, end)
                try:
                    if tempGScore >= gScoreMap[n]:
                        continue
                    gScoreMap[n] = tempGScore
                except:
                    gScoreMap.update({n: tempGScore})
                path.update({n: current})
                fScoreMap.update({n: gScoreMap[n] + PathFinder.SquaredDist(n, end)})
        print("NO ROUTE")
        return 1

    @staticmethod
    def FindMin(theSet, m):
        theMin = None
        minS = None
        for s in theSet:
            if theMin is None:
                theMin = m[s]
                minS = s
                continue
            if m[s] < m[minS]:
                theMin = m[s]
                minS = s

        return minS

    @staticmethod
    def FindNeighbours(a, coords, connections):
        neighbours = set()
        j = coords.index(a)
        for i in range(0, len(connections[j])):
            if connections[j][i] == 1:
                neighbours.add(coords[i])
        return neighbours

    # Method to find the squared distance as square rooting is slow
    @staticmethod
    def SquaredDist(a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

    @staticmethod
    def GetPath(camefrom, current):
        path = [current]
        while current in camefrom:
            current = camefrom[current]
            path.append(current)
        return path[::-1]


