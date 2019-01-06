#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/6'
__time__ = '16:53'
__filename__ = 'bfs.py'

from common import checkSymmetricMatrix
from common import Queue

def findNextAdjNode(matrix,start,end = 0):
    '''
    in a given matrix,find the given start node's next adj node which has a index not less
    than end
    this function is a iterator in fact
    :param matrix: [[]]
    :param start: int,the node's index which is the start node to get the index
    :param end: int,next node index
    :return: int,-1 representing the node has no adjacent node
                  other index means the node's valid next adjacent node
    '''

    for index in range(end,len(matrix)):
        if matrix[start][index] != 0:
            yield index

    yield -1

def noDirecBFS(graphMatrix,startNode = 0):
    '''
    this function is used to traversal the undirected graph
    :param graphMatrix:[[]],the graph's adjacent graph
    :return:[], containing the values of the nodes in the graph after traversalling
    '''

    if not checkSymmetricMatrix(graphMatrix):
        raise ValueError('the matrix is not symmetric,please pass a symmetric matrix.')
    if startNode >= len(graphMatrix):
        raise ValueError('the start node is not in the graph,please check.')

    visited = [0] * len(graphMatrix)
    queue = Queue()
    res = [startNode]
    queue.push(startNode)
    visited[startNode] = 1

    while not queue.isEmpty():
        header = queue.pull()
        for index in findNextAdjNode(graphMatrix,header):
            if index == -1:
                break
            if visited[index] == 0:
                visited[index] = 1
                res.append(index)
                queue.push(index)

    return res

if __name__ == '__main__':
    from common import noDirecGraphMatrix
    print(noDirecBFS(noDirecGraphMatrix))
    print(noDirecBFS(noDirecGraphMatrix,100))