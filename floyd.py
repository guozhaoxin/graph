#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/19'
__time__ = '16:30'
__filename__ = 'floyd.py'

'''
the floyd method
this method is used to find all nodes pair shortest path,even if the edge weight may be negative.
the basic thought is that every time we get a middle node,we check every pair if the path can be shorter 
through the node,if so update the result.
'''

class Floyd:
    @classmethod
    def floydcheck(cls,distanceArray:list,pathArray:list):
        '''
        used to update the result every time use a node as n middle node.
        :param distanceArray: [[]],the distance table
        :param pathArray: [[]],the middle node table
        :param nodescount: the
        :return: None,as all the update work is don in distanceArray and pathArray.
        '''
        nodescount = len(distanceArray)
        for middle in range(nodescount):
            for start in range(nodescount):
                for end in range(nodescount):
                    if distanceArray[start][end] > distanceArray[start][middle] + distanceArray[middle][end]:
                        distanceArray[start][end] = distanceArray[start][middle] + distanceArray[middle][end]
                        pathArray[start][end] = middle
    @classmethod
    def floyd(cls,matrix):
        '''
        the only api can be used by others.
        :param matrix: []
        :return: dict,the key is (start,end),while the value is a list,[distance,[path]],
                        distance is the distance between the 2 nodes,while path is the the whole path.
        '''
        distaceArray = [] # used to store every node pair distance
        pathArray = [] # used to store all the middle node,if no such a node a middle node,the value is -1.
        for i in range(len(matrix)):
            curPath = []
            curDis = []
            for j in range(len(matrix)):
                curPath.append(-1)
                curDis.append(matrix[i][j])
            pathArray.append(curPath)
            distaceArray.append(curDis)
        cls.floydcheck(distaceArray,pathArray)
        res = cls.findpath(pathArray,distaceArray)
        return res

    @classmethod
    def findpath(cls,patharray,distacearray):
        '''
        used to find a path between any nodes pair.
        :param patharray: [],the final path table.
        :param distacearray: [],the final distance table.
        :return: dict,the key is (start,end),while the value is a list,[distance,[path]],
                        distance is the distance between the 2 nodes,while path is the the whole path.
        '''
        inf = float('inf')
        res = dict()
        nodescount = len(patharray)
        for i in range(nodescount):
            for j in range(nodescount):
                if i == j:
                    continue
                path_I_J = [distacearray[i][j]] # used to store the distance and path
                if distacearray[i][j] != inf:
                    path = cls.__helper(i,j,patharray)
                    path.append(j)
                    path_I_J.append(path)
                res[(i,j)] = path_I_J
        return res

    @classmethod
    def __helper(cls,i,j,paths):
        '''
        a recursion method
        :param i: int,currently start node
        :param j: int,currently end node
        :param paths: the complete path table.
        :return: [],the path between start and node,but not include the end node itself.
        '''
        if paths[i][j] == -1:
            return [i]
        left = cls.__helper(i,paths[i][j],paths)
        right = cls.__helper(paths[i][j],j,paths)
        return left + right

if __name__ == '__main__':
    inf = float('inf')
    graph = [
        [0,1,inf,4],
        [inf,0,9,2],
        [3,5,0,8],
        [inf,inf,6,0],
    ]
    res = Floyd.floyd(graph)
    for key in res.keys():
        print(key,res[key][0],res[key][1])