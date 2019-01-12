#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/12'
__time__ = '17:10'
__filename__ = 'kruskal.py'

'''
this file is used to show how kruskal works.
the basic thought is:
1 firstly we sort all the edges in the graph ascending,to complete this step,we can make
   a new structure:
   struct EdgeSet{
    int start; // the start node's index ,we can also use the node's name
    int end; // the end node's index, we can also use the node's name
    int weight; // the distance between the 2 nodes, in kruskal,the weight value cannot be 0 or infinite
   }
  we then make a array containing all EdgeSet type var and sort by ascending.
2 we scan the EdgeSet array from small to large,every we add a path(or EdgeSet element) to the result,
    we check if the result will have a ring after adding such a path,if so,we discard such a path and 
    continue to check next path.
    then how to judge if the res has ring?
    we can give every node a root, in such case, those nodes using the same node as root node will in a same tree,
    assume now we get the path pair(i,j),if j and j have the same root,then we can know adding the path will
    result in a ring appearing in the result,discard it.
    to record the root node,we can design a new array whose lengthen equal to the count of the nodes whille
    only int eles appear in the array,initially all the elements are -1, meaning all nodes use itself as root
    node,assume we have 5 nodes,then the array is:
        array = [-1,-1,-1,-1,-1]
    from the first edgeSet to last,we check if the start and end nodes are in the same tree,if so ,skip;
    if not,we must find the 2 nodes' root node,assuming A,B ,then we check who has more children,if A has more,
    join the two trees in A, we can set array[A] += array[B],while set array[B] = A
3 lastly,we must know if res's lengthen < nodecount - 1,then the graph has no MST,we must return empty result.

to use the method,such as :
    res = kruskal(matrix)
the matrix is the graph's adj matrix, you must ensure all elements are int or float and never < 0.
'''

INFINITE = float('inf') # infinite distance

class EdgeSet:
    '''
    the edge edge class,its attr is below:
    1 start,int or str,the start node's name or index;
    2 end,int or str,the end node's name or index;
    3 weight,int,the distance between start and end node;
    '''
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return ','.join([str(self.start),str(self.end),str(self.weight)])

def modify(edgeArray,nodescount):
    '''
    the core of kruskal thought,the method may raise AssertionError
    :param edgeArray: [EdgeSet,],all the edges pair,
    :param nodescount: the count of all the nodes
    :return: dict，the result,
            key:(start,end),every edge's start and end node;
            value:int, the distance between 2 nodes.
            if the graph has no MST,return empty dict.
            besides,the method may raise AssertionError.
    '''
    res = {}

    #if the count of the paths are less than nodes' count ,then the graph never has a MST.
    if len(edgeArray) < nodescount:
        return res

    roots = [-1] * nodescount # store all nodes' root node index
    for k in range(len(edgeArray)):
        start = edgeArray[k].start
        end = edgeArray[k].end

        starroot = start
        while roots[starroot] > -1:
            starroot = roots[starroot] # to find the start node's root node
        endroot = end
        while roots[endroot] > -1:
            endroot = roots[endroot] # to find the end node's root node
        if starroot == endroot: # if start and end nodes has the same root node,the path can not be added in the res
            continue

        # merge the two trees in a same tree
        if roots[starroot] < roots[endroot]:
            least = endroot
            most = starroot
        else:
            least = starroot
            most = endroot
        roots[most] += roots[least]
        roots[least] = most

        res[(start,end)] = edgeArray[k].weight

    if len(res) != nodescount - 1: # the paths count are less than needed,no MST.
        return {}

    return res

def kruskal(matrix):
    '''
    the kruskal method, this is its real API,
    :param matrix: [],the graph's adj matrix
    :return: dict,please read modify method.
    '''

    # check if the matrix is vaild
    assert matrix
    assert len(matrix) == len(matrix[0])

    edgeArray = [] # we need not store all the paths,as the matrix is symmetric
    for i in range(len(matrix)):
        for j in range(i,len(matrix[i])):
            if matrix[i][j] != 0 and matrix[i][j] != INFINITE:
                edgeArray.append(EdgeSet(i,j,matrix[i][j]))
    edgeArray.sort(key = lambda x:x.weight) # sort the edge array according to the distance
    return modify(edgeArray,len(matrix))

if __name__ == '__main__':
    inf = float('inf')
    inf = 0
    edgeMatrix = [
        [inf,0,0,0,inf,inf],
        [0,inf,5,inf,3,inf],
        [0,5,inf,5,6,4],
        [0,inf,5,inf,inf,2],
        [inf,3,6,inf,inf,6],
        [inf,inf,4,2,6,inf]
    ]
    inde2name = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
    res = kruskal(edgeMatrix)
    print(res)
    for key in res.keys():
        print(inde2name[key[0]],',',inde2name[key[1]],',',res[key])