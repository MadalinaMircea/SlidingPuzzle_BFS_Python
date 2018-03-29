from Path import Path
from copy import deepcopy
from State import State

class Controller:
    def __init__(self, problem):
        self.__problem = problem

    def getProblem(self):
        return self.__problem

    def orderStates(self, stateList):
        for i in range(len(stateList) - 1):
            for j in range(i + 1, len(stateList)):
                if self.__problem.heuristic(stateList[i], self.__problem.getFinal()) < self.__problem.heuristic(stateList[j], self.__problem.getFinal()):
                    aux = stateList[i]
                    stateList[i] = stateList[j]
                    stateList[j] = aux

        return stateList

    def bfs(self, problem):
        q = [Path([problem.getInitial()])]
        visited = []
        i = 0
        while q:
            i = i + 1
            currentPath = q.pop(0)
            currentState = currentPath.getLast()

            if currentState == problem.getFinal():
                return currentPath, i

            visited.append(currentState)

            for child in currentState.allNextStates():
                if child not in visited:
                    p = Path(deepcopy(currentPath.getValues()))
                    p.add(State(deepcopy(child.getValues())))
                    q.append(p)
        return None, i

    def gbfs(self, problem):
        q = [Path([problem.getInitial()])]
        visited = []
        i = 0
        while q:
            i = i + 1
            currentPath = q.pop(0)
            currentState = currentPath.getLast()

            if currentState == problem.getFinal():
                return currentPath, i

            visited.append(currentState)

            aux = []

            for child in currentState.allNextStates():
                if child not in visited:
                    aux.append(child)

            aux = self.orderStates(aux)

            for state in aux:
                p = Path(deepcopy(currentPath.getValues()))
                p.add(State(deepcopy(state.getValues())))
                q.append(p)

        return None, i
