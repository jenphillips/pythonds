class BinaryTree():
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def __repr__(self):
        return '[ %s , [ %s ], [ %s ] ]' % (
            self.key, self.leftChild, self.rightChild)

    def insertLeft(self, newNode):
        newTree = BinaryTree(newNode)
        if self.leftChild:
            oldLeft = self.leftChild
            newTree.leftChild = oldLeft
        self.leftChild = newTree

    def insertRight(self, newNode):
        newTree = BinaryTree(newNode)
        if self.rightChild:
            oldRight = self.rightChild
            newTree.rightChild = oldRight
        self.rightChild = newTree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def testTree():
    r = BinaryTree('a')
    # print(r.getRootVal())
    # print(r.getLeftChild())
    r.insertLeft('b')
    # print(r.getLeftChild())
    # print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    # print(r.getRightChild())
    # print(r.getRightChild().getRootVal())
    # r.getRightChild().setRootVal('hello')
    # print(r.getRightChild().getRootVal())
    print r


def selfCheck():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getLeftChild().insertRight('d')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    print r
