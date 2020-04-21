from Node import *

class Deque(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.counter =0

    def IBF(self,data): #INSERT BEFORE FRONT
        newNode = node(data)
        if self.front==None:
            self.front=newNode
            self.rear=newNode
        else:
            newNode.next=self.front
            self.front=newNode
        self.counter += 1

    def IAR(self,data): #INSERT AT REAR
        newNode = node(data)
        if self.rear==None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
        self.counter+=1

    def DFF(self):  #DELETE FROM FRONT
        if self.counter==0:
            print("The Queue is Empty")
        elif self.counter==1:
            self.front=None
            self.rear=None
        else:
            self.front= self.front.next
        self.counter-=1

    def DFR(self):  #DELETE FROM REAR
        temp = self.front
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            while temp.next.next != None:
                temp=temp.next
            temp.next=None
            self.rear=temp
        self.counter-=1

    def count(self):
        print("The Number of elements in the Queue:",self.counter)

    def display(self):
        temp = self.front
        while temp:
            print("|%d|-->"%temp.data,end="")
            temp=temp.next
        if self.counter == 0:
            print("The Queue is empty")
        else:
            print("X")
