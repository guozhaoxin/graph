#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/12'
__time__ = '12:32'
__filename__ = 'prim.py'

'''
this file is used to show how prim alg works.
the basic solution is :
    1 we choose a random node as the first node;
    2 we build a kind of structure which contains the edge between the root node and all other node in this graph (not
        include the root node); in this structure,we must store the start node(initially is the root node we chose in 
        step 1),the end node,and the lengthen of the edge between the 2 nodes(if no such a edge,then the distance is 
        infinite,in C we can set it to 65535,in python we can set it to float('inf')),the status of this this path,choosen
        well or not;
        below is such a structure:
        struct EdgeSet{
            int startindex; // it can also be char *
            int endindex; // it can also be char *
            int distance;
            int status; // you can use bool or other valid type,only if it can represent yes or no.
        }
        after the structure is designed,we store corresponding info in an array,while the lengthen of the array
        is equal to the nodes' count - 1,we name the array to edgeArray.
    3 firstly we scan the edgeArray,to find a edge that has not chosen(the status is false) and the lengthen is the shortest,
        1) if no such a edge,then the graph has no MST,we can end terminate the function;
        2) we find such a edge,assume the start node is A,while end node is B,then we update the edgeSet's status to true,
            and add the path to res,then we scan the edgeArray,to find those edges not chosen,we assume one edge uses K as 
            its start node and L as its end node,then we compare the edge's lengthen and the lengthen of pair (B,L),
            if pair(B,L) is shorter,then we update the edgeSet to use B as its root node and the distance to the value 
            of pair(B,L);
    4 execute step 2 -3 by nodes' count - 1 and return the res.

to use the method,like this:
    res = prim(matrix)
the matrix is the graph's adj matrix,you must ensure the matrix only contains int or float ele and never < 0.
'''
class EdgeSet:
    '''
    this class is used to represent the edge information in a given map
    it has some attr:
        start:str or num,the start node of a give edge,even the undirected graph has no start node;
        end:str or num,the end node of a given edge,even the undirected graph has no end node;
        edgeValue:num,the lengthen of the edge between start and end,if no edge between 2 nodes,its value is float('inf');
        status:0 or 1,representing if the edge has been decided well or not.
    '''
    def __init__(self,start,end,edgevalue):
        self.start = start
        self.end = end
        self.edgeValue = edgevalue
        self.status = 0

    def __str__(self):
        return ','.join([str(self.start),str(self.end),str(self.edgeValue)])

def modify(edgeMatrix,edgeArray):
    '''
    this function is used to get the MST of a given graph,in fact this function is real prim function.
    :param edgeMatrix:[[]],the adj matrix of a given graph,and ele in this function is num,
                        such as int or float,and never less than 0.
    :param edgeArray:[EdgeSet,],a list containing N EdgeSet objects and N is equal to the count
                    of the nodes in a given graph.
    :return:{},the prim result is stored in this dict,and this dict uses (start,end) of node as key,while the
            lengthen of the directed conected edge between two nodes.
            but we must know that the graph may have no MST,in this case,we will return an empty dict.
    '''
    res = {} # the var will contain the MST result
    for i in range(1,len(edgeMatrix)): # as N nodes,we only need to find N - 1 edges.
        k = -1 # k will keep the new shortest edge's index in the edgeArray
        min = float('inf') # the shortest distance this step finds.
        for j,edgeSet in enumerate(edgeArray):
            if edgeSet.status == 0 and edgeSet.edgeValue < min: # find a new path that has not chosen
                k = j
                min = edgeSet.edgeValue
        if min == float('inf'): # in this time,we never find a valid path ,and this means that the graph has no MST.
            return {}
        start = edgeArray[k].start
        res[(start,edgeArray[k].end)] = edgeArray[k].edgeValue # add the path to the result
        edgeArray[k].status = 1 #update edgeSet as the path has been chosen
        start = edgeArray[k].end # we will only detect those paths that starts with start node and not chosen.

        for edgeSet in edgeArray:
            # this part is used to update the edgeArray
            if edgeSet.status == 0 and edgeMatrix[start][edgeSet.end] != 0 and edgeMatrix[start][edgeSet.end] < edgeSet.edgeValue:
                edgeSet.start = start
                edgeSet.edgeValue = edgeMatrix[start][edgeSet.end]
    return res


def prim(edgeMatrix):
    '''
    this function is prim function and is mainly used to generate a edge array whose elements all EdgeSet object
    in this function,you must pass the graph's adj matrix,and this matrix has no ele that is less than 0.
    :param edgeMatrix:[],the graph's adj matrix,and no num is less than 0.
    :return:dict,please read modify function above,the method may raise AssertionError.
    '''
    assert edgeMatrix # ensure this graph is not an empty graph
    assert len(edgeMatrix) == len(edgeMatrix[0]) # ensure the adj matrix is a square matrix.
    edgeArray = [] # used to contain those EdgeSet objects.
    start = 0 # to a graph,if it has a MST,then the start node doesn't matter,so we use the first node as root node,and you can modify
              # this value to any num you want,but it must be an integer between 0 and the counts of the graph's nodes.
    for i in range(len(edgeMatrix)):
        if i == start:
            continue
        edgeArray.append(EdgeSet(start,i,edgeMatrix[start][i] if edgeMatrix[start][i] else float('inf')))
    return modify(edgeMatrix,edgeArray)

if __name__ == '__main__':
    inf = float('inf')
    inf = 0
    edgeMatrix = [
        [inf,6,1,5,inf,inf],
        [6,inf,5,inf,3,inf],
        [1,5,inf,5,6,4],
        [5,inf,5,inf,inf,2],
        [inf,3,6,inf,inf,6],
        [inf,inf,4,2,6,inf]
    ]
    inde2name = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
    res = prim(edgeMatrix)
    for key in res:
        print(inde2name[key[0]],',',inde2name[key[1]],',',res[key])