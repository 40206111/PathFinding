from tools.Window import Window
import tkinter as tk

__author__ = 'Emma'
__project__ = 'Caves'


class PathFinder(object):

    # Method to do the search
    @staticmethod
    def FindPath(coords, connections, step):

        print("Calculating...")
        path = {}
        # Set start and end coordinates
        start = coords[0]
        end = coords[len(coords) - 1]
        if step:
            Window.buttons["Step"].wait_variable(Window.var)
            Window.var.set(0)
        Window.can.itemconfig(Window.points[start], fill='#FFC0CB', outline='#FFC0CB')
        Window.can.itemconfig(Window.points[end], fill='#FFFFF1', outline='#FFFFF1')

        # Initialise sets
        closedSet = set()
        openSet = {start}
        gScoreMap = {start: 0}
        fScoreMap = {start: PathFinder.SquaredDist(start, end)}

        if step:
            Window.buttons["Step"].wait_variable(Window.var)
            Window.var.set(0)

        # While openset isn't empty
        while len(openSet) != 0:
            # set current to min score currently in the open set
            current = PathFinder.FindMin(openSet, fScoreMap)
            if current != start and current != end:
                Window.can.itemconfig(Window.points[current], fill='blue', outline='blue')

            # if goal reached
            if current == end:
                print("GOAL REACHED")
                # return path
                path = PathFinder.GetPath(path, end)
                Window.labels["path"].config(text="Path Length: " + str(len(path)))
                for p in path:
                    if p != start and p != end:
                        if step:
                            Window.buttons["Step"].wait_variable(Window.var)
                            Window.var.set(0)
                        Window.can.itemconfig(Window.points[p], fill='green', outline='green')
                    elif p == end:
                        if step:
                            Window.buttons["Step"].wait_variable(Window.var)
                            Window.var.set(0)
                        Window.can.itemconfig(Window.points[p], fill='#32D732', outline='#32D732')
                if step:
                    Window.buttons["Step"].destroy()
                return 0

            # Find the caves this node is connected too
            neighbours = PathFinder.FindNeighbours(current, coords, connections)
            # remove current from open set
            openSet.remove(current)

            # loop through neighbours
            for n in neighbours:
                if n != start and n != end and n not in openSet and n not in closedSet:
                    Window.can.itemconfig(Window.points[n], fill='#FFA500', outline='#FFA500')
                # ignore if neighbour is closed
                if n in closedSet:
                    continue
                # add to open set
                if n not in openSet:
                    openSet.update([n])
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

            # add current path to closed set
            closedSet.update([current])
            if step and current != start:
                Window.buttons["Step"].wait_variable(Window.var)
                Window.var.set(0)
                Window.can.itemconfig(Window.points[current], fill='#b1e3e7', outline='#b1e3e7')
        # Inform user no route was found
        print("NO ROUTE")
        return 1

    # Finding the minimum
    @staticmethod
    def FindMin(theSet, m):
        # Initialise min int and current min
        theMin = None
        currentMin = None

        # Loop through set
        for s in theSet:
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


