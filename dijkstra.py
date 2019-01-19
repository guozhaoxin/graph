#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/19'
__time__ = '13:05'
__filename__ = 'dijkstra.py'

'''
dijkstra method to find one node to any other node's shortest path and distance in a undirected graph;
image we have a graph:
    matrix = [
        [0,inf,10,inf,30,100],
        [inf,0,5,inf,inf,inf],
        [inf,inf,0,50,inf,inf],
        [inf,inf,inf,0,inf,10],
        [inf,inf,inf,20,0,60],
        [inf,inf,inf,inf,inf,0],
    ]
in this graph,inf means no directed between two nodes.
we assign a variable visited = [0] * len(matrix),this variable store those nodes which have not been
confirmed the path,0 means not confirmed while 1 means confirmed;
we must assign another variable ie distances = [inf] * len(matrix),all eles in this list mean distance corresponding
to the start node and end node.
we keep the third variable ie previous = [-1] * len(matrix) to represent the corresponding node\'s previous node.
we image the first node is 1
in the above graph,the corresponding variables are:
visited = [0,1,0,0,0,0]
distance = [inf,0,5,inf,inf,inf]
previous = [-1,1,,1,-1,-1,-1]
from all nodes,we check the which node has been not confirmed the path and has the shortest path,
if no such path exists,then the scan has finished;
else use the node as a middle node,we check if we can get a shorter path from start node to end node through
the middle node,if so,update the distance and previous nodes,then the node has been confirmed.
cycle the steps until all nodes has been confirmed,and the paths and distances all confirmed. 
'''


class NodeDisSet:
    '''this class is used to store the paths between a given node and all other nodes in a undirected graph'''
    def __init__(self,previous,distance,startnode):
        '''
        there are 3 important attributes,
            1 previArray,list[int],used to store every node's previous node index from start to itself,
                if no such a path,then the value is -1;
            2 distance,[int],used to store start node to corresponding node's distance,
                if no suach a path,then the value is float('inf');
            3 startnode,int,the start node in the class instance,as the class instance only store a given node
                to all other nodes' path information.
        :param previous: [int],seen above;
        :param distance: [int],seen above;
        :param startnode: int,the start node index.
        '''
        self.previArray = previous
        self.distanceArray = distance
        self.startnode = startnode

    def ppath(self,endnode):
        '''
        this method is used to find a path from the class instance's start node to a give node.
        :param endnode: int,the give node as end node we want to get a path.
        :return: [int,[int,]],the first element is the distance between the start and end node,if
                  no such a path exists,then the value is inf,if the 2 nodes are the same node,then
                  the value is 0; the second element is the path list,all the members are all the nodes
                from the start node to the end node(including the start and end node),
                if no such a path exists,the second element is an empty list.
        please if you pass a invalid index then it will throw a ValueError.
        '''
        if endnode < 0 or endnode >= len(self.previArray):
            raise ValueError('end node %s is wrong (%s,%s)' % (endnode, 0, len(self.previArray) - 1))
        res = [0,[]]

        if self.distanceArray[endnode] == float('inf'):
            res[0] = float('inf')
        else:
            res[0] = self.distanceArray[endnode]
            self.__path_dfs(endnode,res)
        res[1] = res[1][::-1] # as the __path_dfs is a recrusion function,so we have to reverse all the nodes.
        return res

    def __path_dfs(self,curnode:int,res):
        '''
        this method is used get the path when start node and end nodes really has such a path.
        :param curnode: int, the current node,as this function is a recrusion method,so we must pass it every time.
        :param res: [int,[int]],the return result ,you can see its information in ppath function.
        :return:
        '''
        if curnode == self.startnode:
            res[1].append(curnode)
            return
        res[1].append(curnode)
        self.__path_dfs(self.previArray[curnode],res)

    def __str__(self):
        return str(self.startnode) + str(self.distanceArray)



def scanf(distanceArray,visitedArray,previous,matrix):
    inf = float('inf')
    while True:
        curnode = -1
        mindistance = inf
        for index in range(len(matrix)):
            if visitedArray[index] == 0 and distanceArray[index] != 0 and distanceArray[index] < mindistance:
                curnode,mindistance = index,distanceArray[index]
        if curnode == -1:
            return
        for index in range(len(matrix)):
            if visitedArray[index] != 0:
                continue
            if distanceArray[index] > matrix[curnode][index] + mindistance:
                previous[index] = curnode
                distanceArray[index] = matrix[curnode][index] + mindistance
        visitedArray[curnode] = 1

def dijkstra(matrxi,startnode:int):
    '''
    this method is dijkstra method,and the API to be used by others.
    you must pass a undirected graph,in the graph,you can set the value between 2 nodes to inf if no directed path
    exists.
    :param matrxi: [[number]]
    :param startnode: int,the start node index
    :return: NodeDisSet instance,please see the class NodeDisSet above.
    please note you must pass a valid index as the start node,else the function will throw a ValueError.
    '''
    if startnode >= len(matrxi) or startnode < 0:
        raise ValueError('the startnode %s not in the nodes\' range (%s,%s)' %(startnode,0,len(startnode) - 1))

    previNodes = [-1] * len(matrxi) # used to store if the node has confirmed the path.
    inf = float('inf')
    distanceArray = [inf] * len(matrxi) # used to store the distance between gieve start and any end node.
    previNodes[startnode] = startnode # the start node use itself as the middle node.
    distanceArray[startnode] = 0 # the start node and itself has a 0 distance
    visitedArray = [0] * len(matrxi) # used to store all the nodes' previous node
    visitedArray[startnode] = 1 # the start node need not check.
    # the below part is used to assign those nodes who have directed link with the given node.
    for index in range(len(matrxi)):
        if index != startnode and matrxi[startnode][index] != 0 and matrxi[startnode][index] != inf:
            previNodes[index] = startnode
            distanceArray[index] = matrxi[startnode][index]

    scanf(distanceArray,visitedArray,previNodes,matrxi)
    res = NodeDisSet(previNodes,distanceArray,startnode)
    return res

def main():
    inf = float('inf')
    matrix = [
        [0,inf,10,inf,30,100],
        [inf,0,5,inf,inf,inf],
        [inf,inf,0,50,inf,inf],
        [inf,inf,inf,0,inf,10],
        [inf,inf,inf,20,0,60],
        [inf,inf,inf,inf,inf,0],
    ]
    res = dijkstra(matrix,1)
    print(res)
    for i in range(len(matrix)):
        path = res.ppath(i)
        print(path[0],path[1])

if __name__ == '__main__':
    main()
