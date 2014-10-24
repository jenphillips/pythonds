def findMin1(myList):
    ''' Find the minimum number in a list, a silly way.  O(n2) + n
    '''
    for i in myList:
        lessThanAll = []
        for j in range(0, len(myList)):
            lessThanAll.append(i < myList[j])

            print 'i=%d, j=%d' % (i, myList[j])
            print '---'

        print lessThanAll

        if lessThanAll.count(False) is 1:
            minNum = i
        print '---------------'

    return minNum


def findMin2(myList):
    ''' Find the minimum number in a list, a (slightly) less silly way.  O(n2)
    '''
    theMin = None
    for index1, x in enumerate(myList):
        isMin = True  # Assume it's the min!  Crazy?
        # Compare to every other number in the list
        for index2, y in enumerate(myList):
            if index1 != index2:  # Skip comparing to itself
                # See if i is greater than j; if so, it's not the min
                if x > y:
                    isMin = False
        if isMin:
            theMin = x

    return theMin


def findMin3(myList):
    ''' Refactoring findMin2.  O(n2)
    '''
    theMin = None
    for x in myList:
        isMin = True
        # Compare to every other number in the list
        for y in myList:
            if x > y:
                isMin = False
        if isMin:
            theMin = x

    return theMin


def findMinLinear(myList):
    ''' Find the minimum number in a list.  O(n)
    '''
    minNum = myList[0]  # Seed with an arbitrary value from the list

    for i in myList:
        if i < minNum:
            minNum = i

    return minNum
