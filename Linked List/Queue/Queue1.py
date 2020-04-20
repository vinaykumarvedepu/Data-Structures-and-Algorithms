from node import *
class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.counter = 0

    def insert(self,data):
        actualNode =Node(data)
        if self.front == None:
            self.front=actualNode
            self.rear=actualNode
        else:
            self.rear.next =actualNode
            self.rear=actualNode
        self.counter+=1

    def delete_f(self):
        if self.front==None:
            print("The Queue is empty")
        elif self.front.next == None:
            self.front=None
            self.rear=None
        else:
            delNode = self.front
            self.front=delNode.next
            del(delNode)
        self.counter-=1

    def display(self):
        temp = self.front
        while temp:
            print("|%d|-->"%temp.data,end="")
            temp = temp.next
        if self.counter != 0:
            print('X')
        else:
            print("The Queue is empty")

    def count(self):
        print("The Number of elements in the Queue:",self.counter)


