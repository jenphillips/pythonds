class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if item == current.getData():
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        # Assume the item will be found
        while current is not None and not found:
            if item == current.getData():
                # Found item to remove
                found = True
            else:
                previous = current
                current = current.getNext()

        if current is None:
            return 'Not found'

        if previous is None:
            # Item was the first item in the list
            self.head = current.getNext()
        else:
            # Remove by setting previous node to point at next node
            previous.setNext(current.getNext())

    def append(self, item):
        # Append item to end of list
        current = self.head
        nodeToAppend = Node(item)

        if current is None:
            self.head = nodeToAppend
        else:
            while current is not None:
                if current.getNext() is None:
                    # Found end of list; append
                    current.setNext(nodeToAppend)
                    return
                current = current.getNext()

    def index(self, item):
        # Return index of given item
        current = self.head
        i = 0

        while current is not None:
            print current.getData()
            if item == current.getData():
                return i

            i += 1
            current = current.getNext()

        return 'Item not found'

    # def pop(self):
    #     '''
    #     Remove & return last item in list
    #     - Traverse the list to its end
    #     - Set the previous node's 'next' value to None
    #     - Return the current node
    #     '''
    #     current = self.head
    #     previous = None

    #     while current.getNext() is not None:
    #         previous = current
    #         current = current.getNext()

    #     # current is now the last node in the list
    #     if current is self.head:
    #         # list only contained one item
    #         self.head = None
    #     else:
    #         previous.setNext(None)

    #     return current

    def pop(self, index='last'):
        '''
        If index is provided, remove & return item at index
        Otherwise, remove & return last item in list
        - If an index is passed in, traverse the list to the index
        - Otherwise, traverse the list to its end
        - Set the previous node's 'next' value to None
        - Return the current node
        '''
        current = self.head
        previous = None
        counter = 0
        found = False

        while current.getNext() is not None and not found:
            if index != 'last':
                if index == counter:
                    found = True
                else:
                    counter += 1
            if not found:
                previous = current
                current = current.getNext()

        # current is now the last node in the list
        if current is self.head:
            if index is 0 and self.size() > 1:
                # first item was popped
                self.head = current.getNext()
            else:
                # list only contained one item
                self.head = None
        else:
            previous.setNext(None)

        return current
