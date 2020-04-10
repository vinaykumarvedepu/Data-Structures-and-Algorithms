from Node import *
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter =0

    def insertStart(self,data):
        self.counter+=1
        newNode = Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def insertEnd(self,data):
        if self.head is None:
            self.insertStart(data)
            return
        self.counter+=1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def remove(self,data):
        self.counter-=1
        if data == self.head.data:
            self.head = self.head.nextNode
        else:
            self.head.remove(data , self.head)

    def traverseList(self):
        temp = self.head
        while temp is not None:
            print("%d"%temp.data,end = " ")
            temp=temp.nextNode
        print()

    def insertAtPosition(self,data,pos):
        newNode = Node(data)
        h = self.head
        if pos ==1:
            self.insertStart(data)
            return
        if pos == self.counter:
            self.insertEnd(data)
            return
        for i in range(1,pos):
            prev = h
            h= h.nextNode
            if h is None:
                print("There is no such location:")
                return
        prev.nextNode = newNode
        newNode.nextNode=h
        self.counter += 1

