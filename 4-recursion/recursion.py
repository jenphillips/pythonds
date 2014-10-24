def fact(n):
    # Return n * n-1 * n-2 ...
    if n <= 1:
        return 1

    return n * fact(n-1)


def fact2(n):
    # Non-factorial version, just for kicks.
    factorial = n
    while n > 1:
        n -= 1
        print n
        factorial = factorial * n
        print factorial
        print '---'

    return factorial


def toStr(n, base):
    # Convert an integer to a string in any base
    convString = '0123456789ABCDEF'
    if n < base:
        return convString[n]
    else:
        return toStr(n//base, base) + convString[n % base]


def revString(string):
    toConvert = list(string)
    if len(toConvert) == 1:
        return str(toConvert[0])
    else:
        # Return last character & decrease size of toConvert
        return ''.join(toConvert.pop() + str(revString(toConvert)))


def detectPalindrome(string):
    reverse = revString(string)
    if reverse == string:
        return True
    return False


import random
import turtle


def tree(branchLen, t):
    if branchLen > 5:
        t.pensize(branchLen/15)
        right_turn = random.randint(15, 45)
        left_turn = random.randint(15, 45)

        t.forward(branchLen)
        # t.right(20)
        t.right(right_turn)
        tree(branchLen-15, t)
        # t.left(40)
        t.left(right_turn + left_turn)
        tree(branchLen-15, t)
        # t.right(20)
        t.right(left_turn)
        t.backward(branchLen)


def drawTree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()


def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    #  Check for base cases:
    #  1. We have run into an obstacle, return false
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED:
        return False
    # 3. Success, an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found
