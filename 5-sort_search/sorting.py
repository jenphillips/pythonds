def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                # Swap
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def shortBubbleSort(alist):
    # Stop early if we detect that the list is sorted
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                # Swap
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                exchanges = True
        passnum -= 1


def selectionSort(alist):
    # [5, 7, 3, 2, 1]
    for endslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        # for i in alist[:endslot]:
            # if i > biggest:
            #     biggest = i
        # ^^ My solution; less good, need to keep track of index
        for location in range(1, endslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[endslot]  # Save current end value
        alist[endslot] = alist[positionOfMax]  # Put biggest value at end
        alist[positionOfMax] = temp  # Put end value where biggest was


def insertionSort(alist):
    for index in range(1, len(alist)):
        # Go through each number in the list (n-1)
        print 'index: %s' % index

        currentValue = alist[index]
        pos = index

        print 'currentValue: %s' % currentValue

        # Look at all number sorted so far; if they are
        # greater than current value, shift to the right
        while pos > 0 and alist[pos - 1] > currentValue:
            print '---'
            print alist
            alist[pos] = alist[pos - 1]
            pos = pos - 1
            print 'switched'
            print alist
            print '---'

        # Insert number in correct place in sorted list
        alist[pos] = currentValue

        print 'final alist: %s' % alist
        print '==='


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue


''' Shell sort with a gap of 3 after 3 passes

5, 16, 20, 12, 3, 8, 9, 17, 19, 7

5 12 9 7

5, 16, 20, 7, 3, 8, 9, 17, 19, 12

16 3 17

5, 3, 20, 7, 16, 8, 9, 17, 19, 12

20 8 19

5, 3, 8, 7, 16, 19, 9, 17, 20, 12
'''


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first > last:  # Will be false if list is 1 item long
        splitpoint = partition(alist, first, last)

        # Sort first half of list
        quickSortHelper(alist, first, splitpoint - 1)
        # Sort second half of list
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivot = alist[first]    # Not actually the first value in alist; the first
                            # value in the sublist we're currently sorting
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and \
                alist[leftmark] <= pivot:
            leftmark += 1

        while rightmark >= leftmark and \
                alist[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
            # Marks have crossed; rightmark is at position
            # where pivot value belongs (split point)
            done = True
        else:
            # Split point not yet reached; swap values
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    # Once done, swap pivot value and value at split point
    temp = alist[first]  # <-- pivot
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    # Return splitpoint to use to divide sublists
    return rightmark


''' Quick sort after second partitioning

14, 17, 13, 15, 19, 10, 3, 16, 9, 12

pivot: 14
leftmark: 17 > 14; Stop
rightmark: 12 < 14: Stop

14, 12, 13, 15, 19, 10, 3, 16, 9, 17

leftmark: 13 < 14; continue
leftmark: 15 > 14; Stop
rightmark: 9 < 14; Stop

14, 12, 13, 9, 19, 10, 3, 16, 15, 17

'''

14, 12, 13, 9, 3, 10, 19, 16, 15, 17

10, 12, 13, 9, 3, 14, 19, 16, 15, 17 # one complete partition

10, 12, 13, 9, 3,   14,   19, 16, 15, 17

10, 3, 13, 9, 12

10, 3, 9, 13, 12

9, 3, 10, 13, 12



