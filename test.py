from LinkedList import *

if __name__ == '__main__':
    """
    a = Node(d=2)
    b = Node(d=0)
    c = Node(d=6)
    x = Node(d=2)
    l = LinkedList(a)
    print(l)
    l = l.add_first(b)
    print(l)
    l = l.add_last(c)
    print(l)
    l = l.add_after(a, 5)
    print(l)
    l = l.add_after(x, 2022)
    print(l)
    """
    L = LinkedList() 
    print(L)
    n1 = L.add_first(2) 
    print(L)
    L.add_first(1) 
    print(L)
    L.add_last(4) 
    print(L)
    L.add_last(5) 
    print('L', L)
    print('n1', n1)
    L.add_after(n1, 3) 
    print(L)
    