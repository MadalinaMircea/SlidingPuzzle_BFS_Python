from copy import deepcopy

class State:
    def __init__(self, values=[]):
        self.__values = values
        self.__size = len(values)

    def getValues(self):
        return self.__values

    def getSize(self):
        return self.__size

    def setValues(self, values):
        self.__values = values
        self.__size = len(values)

    def getValueOnPos(self, i, j):
        return self.__values[i][j]

    def setValueOnPos(self, i, j, value):
        self.__values[i][j] = value

    def getEmptyPos(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if self.__values[i][j] == 0:
                    return i, j
        return -1, -1

    def moveNeighbour(self, oldi, oldj, newi, newj):
        child = State(deepcopy(self.__values))
        child.setValueOnPos(oldi, oldj, self.__values[newi][newj])
        child.setValueOnPos(newi, newj, 0)
        return child

    def allNextStates(self):
        result = []
        i, j = self.getEmptyPos()

        if i == 0:
            if j == 0:
                # empty in top right corner
                # move right neighbour
                result.append(self.moveNeighbour(i, j, i, j+1))
                # move bottom neighbour
                result.append(self.moveNeighbour(i, j, i+1, j))

            elif j == self.__size - 1:
                # empty in top right corner
                # move left neighbour
                result.append(self.moveNeighbour(i, j, i, j-1))
                # move bottom neighbour
                result.append(self.moveNeighbour(i, j, i+1, j))
            else:
                # empty on first line, not in corner
                # move left neighbour
                result.append(self.moveNeighbour(i, j, i, j-1))
                # move right neighbour
                result.append(self.moveNeighbour(i, j, i, j+1))
                # move bottom neighbour
                result.append(self.moveNeighbour(i, j, i+1, j))
        elif i == self.__size - 1:
            if j == 0:
                # empty in bottom left corner
                # move right neighbour
                result.append(self.moveNeighbour(i, j, i, j+1))
                # move top neighbour
                result.append(self.moveNeighbour(i, j, i-1, j))
            elif j == self.__size - 1:
                # empty in bottom right corner
                # move left neighbour
                result.append(self.moveNeighbour(i, j, i, j-1))
                # move top neighbour
                result.append(self.moveNeighbour(i, j, i-1, j))
            else:
                # empty on last line, not in corners
                # move left neighbour
                result.append(self.moveNeighbour(i, j, i, j-1))
                # move right neighbour
                result.append(self.moveNeighbour(i, j, i, j+1))
                # move top neighbour
                result.append(self.moveNeighbour(i, j, i-1, j))
        else:
            if j == 0:
                # empty on first column, not in corners
                # move right neighbour
                result.append(self.moveNeighbour(i, j, i, j+1))
                # move top neighbour
                result.append(self.moveNeighbour(i, j, i-1, j))
                # move bottom neighbour
                result.append(self.moveNeighbour(i, j, i+1, j))
            elif j == self.__size - 1:
                # empty on last column, not in corners
                # move left neighbour
                result.append(self.moveNeighbour(i, j, i, j-1))
                # move top neighbour
                result.append(self.moveNeighbour(i, j, i-1, j))
                # move bottom neighbour
                result.append(self.moveNeighbour(i, j, i+1, j))
            else:
                # empty not on edge
                result.append(self.moveNeighbour(i, j, i, j-1))
                result.append(self.moveNeighbour(i, j, i, j+1))
                result.append(self.moveNeighbour(i, j, i-1, j))
                result.append(self.moveNeighbour(i, j, i+1, j))

        return result

    def __eq__(self, state):
        if not isinstance(state, State):
            return False

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if self.__values[i][j] != state.getValueOnPos(i, j):
                    return False

        return True

    def __len__(self):
        return self.__size

    def __str__(self):
        result = ''
        for line in self.__values:
            for value in line:
                result = result + ' ' + str(value)
            result = result + '\n'
        return result
