# Create a list 4 ways.


def test1():
    ''' Concatenation '''
    l = []
    for i in range(1000):
        l = l + [i]  # O(k): k = list length

    return l


def test2():
    ''' Append '''
    l = []
    for i in range(1000):
        l.append(i)  # O(1): same regardless of list length

    return l


def test3():
    ''' List comprehension '''
    l = [i for i in range(1000)]

    return l


def test4():
    ''' Range + list constructor '''
    l = list(range(1000))

    return l


'''
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

concat  6.54352807999 milliseconds
append  0.306292057037 milliseconds
comprehension  0.147661924362 milliseconds
list range  0.0655000209808 milliseconds
'''