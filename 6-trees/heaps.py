class BinaryHeap():

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, item):
        self.heapList.append(item)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        # Takes index of item (i)
        # Swap item with parent until it is smaller than
        # its children and larger than its parent
        while i // 2 > 0:
            child = self.heapList[i]
            parent = self.heapList[i // 2]
            if child < parent:
                tmp = parent
                self.heapList[i // 2] = child
                self.heapList[i] = tmp
        i = i // 2

    def findMin(self):
        return self.items[0]

    def minChild(self, i):
        # Return index of smaller child of root at given index
        if i * 2 + 1 > self.currentSize:
            return i * 2
            # ^^ This seems to assume there is a left child (i * 2);
            # what if there isn't?
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        # Takes index of item (i)
        # Swap item with child until it is smaller than
        # its children and larger than its parent
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
        i = mc

    def delMin(self):
        minval = self.heapList[1]  # Return minimum value
        # Move last value in list to first/top
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()  # Delete last value (it's been moved)
        self.percDown(1)
        return minval

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def buildHeap(self, list):
        pass
