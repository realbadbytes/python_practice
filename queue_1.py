class Queue:
    def __init__(self):
            self.queue = list()

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ('[-] queue is empty')

    def size(self):
        return len(self.queue)

    def print_queue(self):
        return self.queue

# declare and initialize
my_queue = Queue()
print 'my_queue size {}'.format(my_queue.size())
print 'enqueue 5'
my_queue.enqueue(5)
print 'enqueue 6'
my_queue.enqueue(6)
print 'enqueue 7'
my_queue.enqueue(7)

# dequeue
print 'my_queue size {}'.format(my_queue.size())
print 'dequeue {}'.format(my_queue.dequeue())
print 'dequeue {}'.format(my_queue.dequeue())
print 'dequeue {}'.format(my_queue.dequeue())
print 'my_queue size {}'.format(my_queue.size())
