from node import *
class Stack(object):
    def __init__(self):
        self.head =None
        self.counter = 0

    def push(self,data):
        newNode = Node(data)
        self.counter += 1
        if not self.head:
            self.head=newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            print("There are no elements in the stack")
        else:
            if self.head.next is None:
                self.head = None
                self.counter-=1
                print("Element popped and the stack is empty")
            else:
                self.head = self.head.next
                self.counter-=1
                print("Element popped ")

    def count(self):
        print("Number of elements in Stack:",self.counter)

    def top(self):
        topNode = self.head
        print("Top element in stack:",topNode.data)

    def display(self):
        actualNode = self.head
        while actualNode is not None:
            print("|%d|"%actualNode.data)
            print("___")
            actualNode=actualNode.next
        else:
            print("Empty Stack")





