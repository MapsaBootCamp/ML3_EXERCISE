
class Graph:
    def __init__(self, directed=False) -> None:
        self._adj_mat: Dict[str, List] = {}
        self.directed = directed

    def _add_node(self, node: str) -> None:
        if node not in self._adj_mat:
            self._adj_mat[node] = []

    def add_node(self, nodes: Union[str, int, List]) -> None:
        if isinstance(nodes, str) or isinstance(nodes, int):
            nodes = [nodes]

        for node in nodes:
            self._add_node(node)

    def add_edge(self, node1: str, node2: str) -> None:
        if node1 not in self._adj_mat or node2 not in self._adj_mat:
            raise NameError("yeki az in noda nis to graph")
        self._adj_mat[node1].append(node2)
        if not self.directed:
            self._adj_mat[node2].append(node1)

    def __str__(self):
        result = "Graph \n"
        if len(self._adj_mat) > 0:
            for node in self._adj_mat:
                result += f"{node} ->"
                for item in self._adj_mat[node]:
                    result += f" {item} "
                result += "\n"
        return result

    def find_all_node_can_go(self, node, neighbor_can_go=[]) -> List:
        for neighbor in self._adj_mat[node]:
            if neighbor not in neighbor_can_go:
                print(neighbor_can_go)
                neighbor_can_go.append(neighbor)
                self.find_all_node_can_go(neighbor, neighbor_can_go)
        return neighbor_can_go

    def isconnected(self):
        if (len(list(self._adj_mat.keys())) < 2):
            return True
        result = self.find_all_node_can_go(list(self._adj_mat.keys())[0])
        print(result)
        if len(result) == len(list(self._adj_mat.keys())):
            return True
        else:
            return False

    def find_path(self, node1, node2):
        pass

    def shortest_path(self, node1, node2):
        pass

    def changestatus(self,rst,bst,newmat):
        print('------------------')
        history=''
        for i in range(len(newmat[rst])):
            if i >=0:

                rstnew=newmat[rst][i]
                print('0rstnew',rstnew,'i',i,'rst',rst)
                # print(1, newmat[rstnew])
                # print(2,newmat[rstnew][rst])
                history=history+'r'+str(rst)
                newmat[rst].remove(newmat[rst][i])
                newmat[rstnew].remove(rst)
                rst=rstnew
                print(newmat)
                # return(rst, newmat)
                break
            else:
                return(False)
        for i in range(len(newmat[bst])):
            if i >=0:

                bstnew=newmat[bst][i]
                print('bstnew',bstnew,'i',i)
                history=history+'b'+str(bst)
                newmat[bst].remove(newmat[bst][i])
                newmat[bstnew].remove(bst)
                bst=bstnew
                print(newmat)
                # return(True)
                break
            else:
                return(False)
        if len(newmat[rst]>0
        Graph.changestatus(self,rst,bst,newmat) :
            print('rst,bst,newmat',rst,bst,newmat)
        else: return(False)




g1 = Graph()
g1.add_node(1);g1.add_node([2, 3, 4, 5])
g1.add_edge(1, 2);g1.add_edge(2, 3);g1.add_edge(1, 4);g1.add_edge(4, 3);g1.add_edge(1, 5);g1.add_edge(5, 1)

print(g1._adj_mat)
print(g1)
# print(g1.isconnected())
f=g1.changestatus(1,1,g1._adj_mat)
# print(f)
# g1.find_all_node_can_go(2)
# my_dict = {1: 1}
# print(len(list(my_dict.keys())))