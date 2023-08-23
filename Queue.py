class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        node_new=node(data)
        if self.rear is None:
           self.front=node_new
           self.rear=node_new
        else:
            self.rear.next=node_new
            self.rear=node_new

    def dequeue(self):
        if self.front is None:
            return None
        dequeued_data =self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear is None
            return dequeued_data

    def peek(self):
        if self.front is None:
            return None
        return self.front is None

    def print_queue(self):
        current = self.front
        while current:
            print(current.data)
            current=current.next
        print("None")


queue=Queue()
queue.enqueue(101)
queue.enqueue(102)
queue.enqueue(103)
queue.print_queue()
