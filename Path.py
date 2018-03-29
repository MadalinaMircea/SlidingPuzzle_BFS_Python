class Path:
    def __init__(self, values):
        self.__values = values

    def getValues(self):
        return self.__values

    def setValues(self, path):
        self.__values = path

    def getLast(self):
        return self.__values[-1]

    def add(self, state):
        self.__values.append(state)

    def __str__(self):
        result = 'Path\n'
        for puzzle in self.__values:
            result = result + str(puzzle) + '\n'
        return result