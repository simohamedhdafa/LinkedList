from Node import *

class LinkedList:
    def __init__(self, r=Node()):
        self.__root = r

    def add_first(self, d):
        n = Node(d, None) if not isinstance(d, Node) else d
        n.setNextNode(self.__root)
        self.__root = n
        return self

    def add_last(self, d):
        p = self.__root
        while isinstance(p.getNextNode(), Node):
            p = p.getNextNode()
        p.setNextNode(Node(d, None) if not isinstance(d, Node) else d)
        return self

    def __str__(self):
        p = self.__root
        s = ""
        while p.getNextNode() != None:
            s += str(p)
            p = p.getNextNode()
        s += str(p)
        return s

    def add_after(self, prevNode, d):
        #nouveau = Node(d, prevNode.getNextNode())
        nouveau = Node(d, prevNode.__root.getNextNode())
        #prevNode.setNextNode(nouveau)
        prevNode.__root.setNextNode(nouveau)
        return self
    