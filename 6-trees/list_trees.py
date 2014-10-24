# class Node():
#     def __init__(self):
#         self.key = None


# class BinaryTree():
#     def __init__(self):
#         self.nodes = []
#         self.currentNode = None

#     def getLeftChild(self, node):
#         pass

#     def getRightChild(self, node):
#         pass

#     def setRootVal(self, val):
#         pass

#     def getRootVal(self):
#         return self.currentNode.val

#     def insertLeft(self, val):
#         pass

#     def insertRight(self, val):
#         pass


# List of lists
def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    print 'root: %s' % root
    existingLeft = root[1]
    print 'existingLeft: %s' % existingLeft
    root[1] = newBranch
    if len(existingLeft) > 0:
        print len(existingLeft)
        print root[1]
        # Push existing branch down the tree as left child of 
        # new branch
        root[1][1] = existingLeft

    return root


def insertRight(root, newBranch):
    print 'root: %s' % root
    existingLeft = root[2]
    print 'existingLeft: %s' % existingLeft
    root[2] = newBranch
    if len(existingLeft) > 0:
        print len(existingLeft)
        print root[2]
        # Push existing branch down the tree as left child of 
        # new branch
        root[2][2] = existingLeft

    return root


def testInsertLeft():
    t1 = [ 1, ['a'], ['b']]
    newRoot = insertLeft(t1, ['c', [], []])

    # [ 1, 
    #     ['c', 
    #         ['a']
    #     ]
    #     ['b']
    # ]
    print newRoot


def testInsertRight():
    t1 = [ 1, ['a'], ['b']]
    newRoot = insertRight(t1, ['c', [], []])

    # [ 1, 
    #     ['c'],
    #     ['b', 
    #         ['a']
    #   ]
    # ]
    print newRoot


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]
