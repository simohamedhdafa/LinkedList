from Node import *

class LinkedList:
    def __init__(self, r=None):
        if isinstance(r, LinkedList):
            p = r.__root
            while p!=None:
                self.add_last(Node(p.getData(),None)) 
                # ajouter à la fin de self un noeud qui ressemble au noeud courrant de r
                p = p.getNextNode()
        elif isinstance(r, Node):
            self.__root = Node(r.getData(), None)
        else:
            self.__root = r

    def add_first(self, d):
        n = Node(d, None) if not isinstance(d, Node) else d
        n.setNextNode(self.__root)
        self.__root = n
        return self

    def add_last(self, d):
        if self.isEmpty():
            self.__root = Node(d, None) if not isinstance(d, Node) else d
            return self
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
    
    def __len__(self):
        compt=0
        p=self.__root
        while p!=None:
            compt+=1
            p = p.getNextNode()
        return compt

    def ajouter(self, L):
        if self.isEmpty(): 
            self = L # copie profonde !
            return self 
        elif L.isEmpty(): return self
        p = self.__root
        q = L.__root
        # parcourir la plus courte
        while p!=None and q!=None:
            p.setData(p.getData()+q.getData())
            p = p.getNextNode()
            q = q.getNextNode()
        # si elles ont la même taille
        # ou si self est plus longue
        if q==None or (q==None and p==None):
            return self
        # cas restant est L est plus longue que self
        while q!=None:
            self.add_last(Node(q.getData(), None)) # copie profonde
            q = q.getNextNode()
        return self

    def somme(self, L):
        if self.isEmpty(): 
            #self = L # copie profonde !
            return LinkedList(L) 
        elif L.isEmpty(): return LinkedList(self)
        p = self.__root
        q = L.__root
        som = LinkedList()
        # parcourir la plus courte
        while p!=None and q!=None:
            som.add_last(Node(p.getData()+q.getData(), None))
            p = p.getNextNode()
            q = q.getNextNode()
        p = q if (q!=None and p==None) else p
        while p!=None:
            som.add_last(Node(p.getData(), None))
            p = p.getNextNode()
        return som

    def __add__(self, l):
        return self.somme(l)
    
    def __iter__(self):
        self.current = self.__root
        return self

    def __next__(self):
        x = self.current
        if x!=None:
            self.current = self.current.getNextNode()
            return  x
        else:
            raise StopIteration
