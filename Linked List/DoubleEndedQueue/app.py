from Deque1 import *
deque = Deque()

while True:
    print("QUEUE MENU")
    print("1.INSERT AT FRONT")
    print("2.INSERT AT REAR")
    print("3.DELETE FROM FRONT")
    print("4.DELETE FROM REAR")
    print("5.COUNT")
    print("6.DISPLAY")
    print("7.EXIT")

    n = int(input("ENTER ANY OPTION FROM THE ABOVE MENU:"))
    if n == 1:
        deque.IBF(int(input("Enter the element you want to insert before front:")))
    elif n==2:
        deque.IAR(int(input("Enter the element you want to insert after rear:")))
    elif n==3:
        deque.DFF()
    elif n==4:
        deque.DFR()
    elif n==5:
        deque.count()
    elif n==6:
        deque.display()
    elif n==7:
        break

