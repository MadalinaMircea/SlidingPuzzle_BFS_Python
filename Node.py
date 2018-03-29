class Node:
    def __init__(self, data=None, parent=None):
        self.__parent = parent
        self.__data = data
        self.__children = []

    def getData(self):
        return self.__data

    def addChild(self, node):
        self.__children.append(node)

    def getChildren(self):
        return self.__children

    def setData(self, node):
        self.__data = node
