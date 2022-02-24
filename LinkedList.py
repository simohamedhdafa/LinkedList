from Node import *

class LinkedList:
    def __init__(self, r=None):
        # 2022/02/24 changement de representation liste vide !
        # entraine modification non encore effectuées!
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
        if self.__root == None : return '-|.'
        p = self.__root
        s = ""
        while p.getNextNode() != None:
            s += str(p)
            p = p.getNextNode()
        s += str(p)
        return s

    def add_after(self, prevNode, d):
        nouveau = Node(d, prevNode.getNextNode() if isinstance(prevNode, Node) else prevNode.__root.getNextNode())
        prevNode.setNextNode(nouveau) if isinstance(prevNode, Node) else prevNode.__root.setNextNode(nouveau)
        # au cas où OBJ = obj.add_after(...)
        return self

    def isEmpty(self):
        return not isinstance(self.__root, Node)

    def Moyenne(self):
        if self.isEmpty(): return 0
        compt = 0
        somme = 0.
        p = self.__root
        while p!=None:
            if isinstance(p.getData(), (int,float,complex)):
                somme += p.getData()
                compt += 1
            p = p.getNextNode()
        return somme/compt if compt!=0 else 0
    
    def add_all(self, nodes):
        # s'assurer que nodes n'est vide
        debut = 1 if self.isEmpty() else 0
        if self.isEmpty():
            self.__root = nodes[0]
        
        p=self.__root
        while p.getNextNode() != None:
            p = p.getNextNode()
        for nd in nodes[debut:]:
            nd.setNextNode(None)
            p.setNextNode(nd)
            p=p.getNextNode()
        return self

    def add_all_v2(self, nodes):    
        # s'assurer que nodes n'est vide
        debut = 1 if self.isEmpty() else 0
        if self.isEmpty():
            self.__root = nodes[0]
        for nd in nodes[debut:]:
            self.add_last(nd)

    def remove(self, node):
        self.getPrev(node).setNextNode(node.getNextNode())

    def getPrev(self, node):
        # si vide ... ?
        p = self.__root
        while p.getNextNode() != node:
            p = p.getNextNode()
        return p
    
