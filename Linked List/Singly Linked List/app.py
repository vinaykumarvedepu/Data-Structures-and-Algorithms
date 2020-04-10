from LinkedList1 import *

linkedList=LinkedList()
while True:
    print("Single Linked List Menu:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at required position")
    print("4. Display")
    print("5.Delete")
    print("6. Exit")
    print("7.To get the size of the linked list")
    n=int(input("Select any one of the option:"))
    if n==1:
        linkedList.insertStart(int(input("Enter the element you want to insert:")))
    elif n==2:
        linkedList.insertEnd(int(input("Enter the element you want to insert:")))
    elif n==3:
        linkedList.insertAtPosition(int(input("Enter the element you want to insert:")),int(input("Enter the position you want to insert:")))
    elif n==4:
        linkedList.traverseList()
    elif n==5:
        linkedList.remove(int(input("Enter the element you want to delete:")))
    elif n==6:
        break
    elif n==7:
        print("The Size of the linked list is {}".format(linkedList.counter))
