class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def mainMenu(self):
        x = input('1 - BFS\n2 - GBFS\nGive input: ')
        if x == '1':
            result, i = self.__ctrl.bfs(self.__ctrl.getProblem())

            if result == None:
                print("No solution")
            else:
                print("BFS: " + str(i))
                for state in result.getValues():
                    print(state)
        else:
            result, i = self.__ctrl.gbfs(self.__ctrl.getProblem())

            if result == None:
                print("No solution")
            else:
                print("GBFS: " + str(i))
                for state in result.getValues():
                    print(state)