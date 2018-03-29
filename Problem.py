from State import State

class Problem:
    def __init__(self):
        self.__initial = State()
        self.__final = State()
        self.readFromFile()

    def getValues(self):
        return self.__values

    def getInitial(self):
        return self.__initial

    def getFinal(self):
        return self.__final

    def expand(self, state):
        return state.allNextStates()

    def heuristic(self, state1, state2):
        h = 0
        for i in range(state1.getSize()):
            for j in range(state1.getSize()):
                if state1.getValueOnPos(i, j) == state2.getValueOnPos(i, j):
                    h = h + 1
        return h

    def readFromFile(self):
        try:
            file = open('E:\Mada\E\School\MPP\BitBucket\Sliding\input.in', 'r')
            initial = []
            n = file.readline()
            n = int(n)
            for i in range(0, n):
                initial.append([])
                line = file.readline()
                line = line.split(' ')
                initial[-1] = [int(x) for x in line]
            self.__initial.setValues(initial)

            file.readline()

            final = []
            for i in range(0, n):
                final.append([])
                line = file.readline()
                line = line.split(' ')
                final[-1] = [int(x) for x in line]
            self.__final.setValues(final)
        except Exception as e:
            print(str(e))
