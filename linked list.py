

class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
        self.prev=None

class list:
    def __init__(self) :
        self.head=None
        self.n=0
    def insert_after(self,x,data):
        y=Node(data)
        self.n +=1
        if x.next!=None:
            x.next.prev=y
        y.next=x.next
        y.prev=x
        x.next=y
        return y
    
    def delete(self,x):
        self.n-=1
        x.prev.next=x.next
        x.next.prev=x.prev
        return x




