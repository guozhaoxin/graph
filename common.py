#coding: utf-8
__author__ = 'gold'
__date__ = '2019/1/6'
__time__ = '16:36'
__filename__ = 'common.py'

noDirecGraphMatrix = [
    [0,1,0,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,1,1],
    [0,0,0,0,0,1,1,0,0],
    [0,0,0,0,1,0,0,0,1],
    [0,1,0,1,0,1,1,0,1],
    [0,1,1,0,1,0,1,0,0],
    [0,0,1,0,1,1,0,0,0],
    [0,1,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0],
]


def checkSymmetricMatrix(matrix):
    '''
    this function is used to check if the matrix is symmetric
    :param matrix: [[]],the graph's adjacent matrix
    :return: bool,True if the matrix is symmetric ;
                  False if the matrix is not symmetric.
    '''

    # firstly check if the matrix is empty
    if not matrix:
        return False

    # then check if the matrix is square
    rowCount = len(matrix)
    for row in matrix:
        if len(row) != rowCount:
            return False

    # lastly check if the matrix is symmetric
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != matrix[col][row]:
                return False

    return True

class QueueNode:
    '''
    this is node class;
    it has two attributes:1 value,the node's value
                          2 next,which is its next Node position
    '''
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Queue:
    '''
    this queue class
    it has 2 attributes:
        1 the header pointing to the header node of the queue;
        2 the tail pointing to the tail of the queue;
    this class has a push function to append a node at the tail
    this chass has a pull function to make the header node leave the queue
    '''

    def __init__(self):
        self.header = self.tail = None

    def push(self,node):
        '''
        this function is used to append a node to the queue
        :param node: value,representing any kind of object
        :return: None
        '''
        if node is None:
            return
        if not self.header:
            self.header = self.tail = QueueNode(node)
        else:
            temp = QueueNode(node)
            self.tail.next = temp
            self.tail = temp

    def pull(self):
        '''
        this function is used to get the queue's header node
        :return: the value of the the header node
        '''

        if not self.header:
            return None

        temp = self.header
        if self.header == self.tail:
            self.header = self.tail = None
        else:
            self.header = self.header.next

        return temp.value

    def isEmpty(self):
        '''
        judge if the queue is empty
        :return: bool,True if the queue is empty
                      False if the queue is not empty
        '''
        if not self.header:
            return True
        return False
