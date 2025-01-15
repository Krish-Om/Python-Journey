class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__stklist = []

    def put(self, elem):
        self.__stklist.insert(0, elem)

    def get(self):
        if not (len(self.__stklist) < 0):
            val = self.__stklist[-1]
            del self.__stklist[-1]
            return val
        else:
            raise QueueError

    def showAll(self):
        print("Elements in the queue: ")
        print("[", end="")
        for e in self.__stklist:
            print(e, end=",")
        print("]")


queue = Queue()
queue.get()
queue.put(12)
queue.put(34)
queue.put(45)


queue.showAll()

print(queue.get())
queue.showAll()
