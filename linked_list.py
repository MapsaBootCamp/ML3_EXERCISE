class Node:
    def __init__(self, name=None,next_node=None) -> None:
        self.name = name
        self.next_node = next_node

class LinkedList:
    def __init__(self,root=None) -> None:
        self.root = root

    def add_begin(self, node):
        nodee=Node(node)
        self.root=nodee

    def append(self, node):
        new_list=Node(node)
        cur_node=self.root
        if self.root is None:
            self.root=new_list
            return
        while True:
            if cur_node.next_node is None:
                cur_node.next_node=new_list
                break
            cur_node=cur_node.next_node

        while cur_node is not None:
            print(cur_node.name,'-->',end=' ')
            cur_node=cur_node.next_node

    def pop(self):
        link_list=self.__iter__()
        link=link_list[:-1]
        print()
        print('pop:')
        for i in link:
            print(i,end=' ')

    def remove(self, index):
        link_list=self.__iter__()
        link_list=link_list[:index]+link_list[index+1:]
        print()
        print('remove:')
        for i in link_list:
            print(i, end=' ')

    def __len__(self)->int:
        return len(self.__iter__())

    def __iter__(self)->list:
        itr=self.root
        strr=''
        while itr:
            strr+=str(itr.name)
            itr=itr.next_node
        return list(strr)

    def __next__(self):
        pass
l=LinkedList()
l.add_begin('1')
l.append('2')
l.append('3')
l.append('7')
for i in l.__iter__():
    print(i,end=' ')
l.pop()
l.remove(2)


