def sequentialSearch(listToSearch, item):
    found = False
    # for i in listToSearch:
    #     if i == item:
    #         found = True

    pos = 0

    while pos < len(listToSearch) and not found:
        if listToSearch[pos] == item:
            found = True
        else:
            pos += 1

    return found


def orderedSequentialSearch(listToSearch, item):
    # Sequential sort on a sorted list
    found = False
    pos = 0
    stop = False

    while pos < len(listToSearch) and not found and not stop:
        if listToSearch[pos] == item:
            found = True
        else:
            if listToSearch[pos] > item:
                # Item will not be found
                stop = True
            else:
                pos += 1

    return found


def binarySearchRec(listToSearch, item):
    # XXX NOT WORKING if value not in list
    found = False
    middle = len(listToSearch) // 2
    print 'middle: %s' % middle

    while not found and len(listToSearch) > 0:
        if listToSearch[middle] == item:
            print '%s = listToSearch[%s] %s' % (
                item, middle, listToSearch[middle])
            found = True
        elif listToSearch[middle] > item:
            # Item is in first half if present
            print '%s is < %s; must be in first half.  middle: %s' % (
                item, listToSearch[middle], middle)
            found = binarySearchRec(listToSearch[:middle], item)
        else:
            # Item is in second half if present
            print '%s is > %s; must be in second half.  middle: %s' % (
                item, listToSearch[middle], middle)
            found = binarySearchRec(listToSearch[(middle + 1):], item)

    return found


def binarySearchRec2(listToSearch, item):
    # Modified my first solution based on book example.
    # (I was close!)
    if len(listToSearch) == 0:
        return False
    else:
        middle = len(listToSearch) // 2

        if listToSearch[middle] == item:
            print '%s = listToSearch[%s] %s' % (
                item, middle, listToSearch[middle])
            return True
        else:
            if item < listToSearch[middle]:
                # Item is in first half if present
                print '%s is < %s; must be in first half.  middle: %s' % (
                    item, listToSearch[middle], middle)
                return binarySearchRec2(listToSearch[:middle], item)
            else:
                # Item is in second half if present
                print '%s is > %s; must be in second half.  middle: %s' % (
                    item, listToSearch[middle], middle)
                return binarySearchRec2(listToSearch[middle + 1:], item)


def binarySearchRec3(alist, item):
    # Straight from the book
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)


def binarySearch(listToSearch, item):
    first = 0
    last = len(listToSearch) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if listToSearch[midpoint] == item:
            found = True
        else:
            if item < listToSearch[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found
