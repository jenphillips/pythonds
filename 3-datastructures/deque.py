class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def checkPalindrome(str_to_check):
    d = Deque()
    for c in str_to_check:
        d.addRear(c)

    # My solution
    # reversed_str = ''
    # for i in range(d.size()):
    #     reversed_str += d.removeRear()

    # print 'Input: %s' % str_to_check
    # print 'Reversed: %s' % reversed_str
    # if reversed_str == str_to_check:
    #     return True

    # return False

    # His solution
    while d.size() > 1:
        rearChar = d.removeRear()
        frontChar = d.removeFront()

        if rearChar != frontChar:
            # Not a palindrome; return.
            return False

    return True
