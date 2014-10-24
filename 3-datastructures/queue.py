import random

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)
    print q.items
    print '***'

    while q.size() > 1:
        passes = num
        while passes > 0:
            # Send child at front of queue to rear
            last = q.dequeue()
            q.enqueue(last)
            print q.items

            passes -= 1

        print '---'
        print q.items
        # When all passes are complete, remove front child
        # & repeat
        q.dequeue()

    print q.items
    return q.dequeue()


class Printer():
    def __init__(self):
        self.currentTask = None
        self.busy = False
        # self.busy = self.currentTask is not None


class Task():
    def __init__(self, timestamp, pages):
        self.timestamp = timestamp
        self.pages = pages
        # Printer can print 10 pages per second, draft quality
        # 6 seconds per page
        self.secondsRequired = pages * 6


# class PrintQueue(Queue):
#     def __init__(self):
#         pass


def handlePrint():
    ''' Simulate print tasks over 1 hour '''

    printer = Printer()
    pq = Queue()
    waitTimes = []

    for i in range(3600):  # 60 min * 60 sec
        print '%s ---------------' % i
        currentSecond = i
        taskCreated = random.randint(1, 180) == 180
        print 'taskCreated? %s' % taskCreated
        if taskCreated:
            numPages = random.randint(1, 20)
            print 'Task created with %d pages at second %d' % (
                numPages, currentSecond)
            t = Task(currentSecond, numPages)
            pq.enqueue(t)

        # If the printer is not busy and a job is waiting, start job
        if not printer.busy and not pq.isEmpty():
            nextTask = pq.dequeue()
            waitTime = currentSecond - nextTask.timestamp
            waitTimes.append(waitTime)
            printer.currentTask = nextTask
            printer.busy = True
            print 'added %s second task to printer' % printer.currentTask.secondsRequired
        else:
            if printer.busy:
                print 'printer is busy'
            if pq.isEmpty():
                print 'queue is empty'

        # Perform 1 second of printing
        if printer.busy:
            printer.currentTask.secondsRequired -= 1
            print 'seconds remaining: %d' % printer.currentTask.secondsRequired

            if printer.currentTask.secondsRequired is 0:
                print 'Task completed ==================='
                printer.busy = False
                printer.currentTask = None

    return waitTimes
