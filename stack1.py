class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
    	return len(self.stack) == 0

    def top(self):
    	if len(self.stack) == 0:
    		print('list tidak ada')
    	else:
    		return self.stack[-1]

    def isi(self):
    	return self.stack

# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

    def isi(self):
    	return self.queue

    def isEmpty(self):
    	return len(self.queue) == 0

    def front(self):
    	if len(self.queue) == 0:
    		print('list tidak ada')
    	else:
    		return self.queue[0]

    def rear(self):
        if len(self.queue) == 0:
            print('list tidak ada')
        else:
            return self.queue[-1]






        