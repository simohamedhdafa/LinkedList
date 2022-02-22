class Node:
    def __init__(self, d=None, node=None):
        self.__data = d
        self.__nextNode = node

    def getData(self):
        return self.__data

    def getNextNode(self):
        return self.__nextNode

    def setData(self, d):
        self.__data = d

    def setNextNode(self, node):
        self.__nextNode = node

    def hasNext(self):
        return self.__nextNode != None

    def __str__(self):
        return "["+str(self.__data)+"]->" if self.hasNext() else "["+str(self.__data)+"]."