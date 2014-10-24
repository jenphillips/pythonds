class Stack():
    ''' Stack data structure implementation
    Push, pop, peek, isEmpty, size
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return(len(self.items) == 0)
        # return self.items == []  # His solution

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
        # return self.items[len(self.items) - 1]  # His solution

    def size(self):
        return len(self.items)


def revstring(mystr):
    ''' Use a stack to reverse a string. '''
    s = Stack()
    for c in mystr:
        s.push(c)

    reversed_str = ''

    while s.isEmpty() is False:
        reversed_str += s.pop()

    return reversed_str


def parenChecker(parenStr):
    ''' Check whether a string of parentheses is balanced. '''
    s = Stack()

    for p in parenStr:
        if p == '(':
            # Push to stack to wait for a closing symbol
            s.push(p)
        elif p == ')':
            # Remove most recent open paren from stack
            try:
                s.pop()
            except:
                # May throw error if more close than open parens
                return 'Not balanced!  Too many close parens.'

    if s.isEmpty():
        return 'Parentheses are balanced'
    else:
        return 'Not balanced!  Too many open parens.'


def symbolChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    print 'open: %s, close: %s' % (open, close)
    openers = "([{"
    closers = ")]}"

    return openers.index(open) == closers.index(close)


def divideBy2(decNumber):
    ''' Convert a positive base 10 integer to a binary number using
        divide by 2 algorithm. '''

    remainderStack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remainderStack.push(rem)
        decNumber = decNumber // 2

    binaryStr = ''
    while not remainderStack.isEmpty():
        binaryStr += remainderStack.pop()

    return binaryStr


def baseConverter(decNumber, base):
    ''' Convert a positive base 10 integer to a binary number using
        divide by 2 algorithm. '''

    digits = "0123456789ABCDEF"

    remainderStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remainderStack.push(rem)
        decNumber = decNumber // base

    newStr = ''
    while not remainderStack.isEmpty():
        binaryStr += digits[remainderStack.pop()]

    return binaryStr


def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

# print(infixToPostfix("5 * 3 ^ (4 - 2)"))
