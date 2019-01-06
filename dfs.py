#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/6'
__time__ = '18:41'
__filename__ = 'dfs.py'

'''this file is used to traversal the graph by dfs'''

from common import checkSymmetricMatrix,Stack

def findNextStartNode(visited):
    '''
    this function is used to get the smallest node index which has not been visited
    :param visited: [],in this list,0 means not visited while 1 means has been visited
    :return: int,index,when all the nodes have all been visited,return -1.
    '''
    for i in range(len(visited)):
        if visited[i] == 0:
            return i
    return -1

def unDirecDFS(graphMatrix):
    if not checkSymmetricMatrix(graphMatrix):
        raise ValueError('the matrix is not symmetric,please pass a symmetric matrix.')

    visited = [0] * len(graphMatrix)
    res = []

    while len(res) < len(graphMatrix):
        index = findNextStartNode(visited)
        visited[index] = 1
        res.append(index)
        stack = Stack()
        stack.push(index)
        while not stack.isEmpty():
            value = stack.getTop()
            newNode = -1
            for i in range(len(graphMatrix)):
                if graphMatrix[value][i] != 0 and visited[i] == 0:
                    newNode = i
                    break
            if newNode == -1:
                stack.pop()
            else:
                stack.push(newNode)
                visited[newNode] = 1
                res.append(newNode)

    return res

if __name__ == '__main__':
    from common import noDirecGraphMatrix
    print(unDirecDFS(noDirecGraphMatrix))
    haha = [
    [0,1,0,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,0,1],
    [0,0,0,0,0,1,1,0,0],
    [0,0,0,0,1,0,0,0,1],
    [0,1,0,1,0,1,1,0,1],
    [0,1,1,0,1,0,1,0,0],
    [0,0,1,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0],
]
    print(unDirecDFS(haha))