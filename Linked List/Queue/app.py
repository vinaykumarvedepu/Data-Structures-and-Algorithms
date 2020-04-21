from Queue1 import *
queue = Queue()

while True:
    print("QUEUE MENU")
    print("1.INSERT")
    print("2.DELETE")
    print("3.DISPLAY")
    print("4.COUNT")
    print("5.EXIT")
    n = int(input("ENTER ANY OPTION FROM THE ABOVE MENU:"))
    if n == 1:
        queue.insert(int(input("Enter the element you want to Insert:")))
    elif n==2:
        queue.delete_f()
    elif n==3:
        queue.display()
    elif n==4:
        queue.count()
    elif n==5:
        break
