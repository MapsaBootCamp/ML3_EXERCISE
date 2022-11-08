class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.next_node = None


class LinkedList:
    
    def __init__(self) -> None:
        self.root = None
        self.lst=[]

    def add_begin(self, node):
        if len(self.lst) == 0:
            self.lst.append(node)
        else:
            node.next_node=self.lst[0]
            a=[]
            for i in self.lst[0:]:
                a.append(i)
            self.lst.clear()
            self.lst.append(node)
            for i in a:
                self.lst.append(i)

    def appendl(self, node):
        if len(self.lst)>0:
            self.lst[-1].next_node = node
            self.lst.append(node)
        else:
            self.lst.append(node)

    def popl(self):
        return self.lst[-1]

    def remove(self, index):
        if index==0:
            a=[]
            for i in self.lst[1:]:
                a.append(i)
            self.lst.clear()
            for i in a:
                self.lst.append(i)
        elif index != len(self.lst):
            a=[]
            for i in range(index):
                a.append(self.lst[i])
            for i in self.lst[index+1:]:
                a.append(i)

            self.lst.clear()
            for i in a:
                self.lst.append(i)
        else:
            self.lst.pop()
            
            
            

    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        return self.lst

    def __next__(self):
        pass