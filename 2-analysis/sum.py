import time


def sumOfN(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()

    return theSum, end-start


def sumOfN3(n):
    start = time.time()

    theSum = (n*(n+1))/2

    end = time.time()

    return theSum, end-start
