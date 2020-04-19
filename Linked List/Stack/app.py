from Stack1 import *

Stack_ele = Stack()

while True:
    print("STACK MENU")
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    print("4.COUNT")
    print("5.TOP")
    print("EXIT")
    n = int(input("ENTER ANY OPTION FROM THE ABOVE MENU:"))
    if n == 1:
        Stack_ele.push(int(input("Enter the element you want to push:")))
    elif n==2:
        Stack_ele.pop()
    elif n==3:
        Stack_ele.display()
    elif n==4:
        Stack_ele.count()
    elif n==5:
        Stack_ele.top()
    elif n==6:
        break

