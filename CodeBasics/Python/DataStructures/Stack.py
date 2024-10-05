from collections import deque


#Instead of list , we are using deque because list uses dynamic array while deque uses doubly linked list 
#hence we avoid dynamic memory allocation problem because in case memory exceeded dynamic memory allocation will lead 
#to lots of memory re allocation
class Stack:

    def __init__(self):
        self.container=deque()
    
    def push(self,data):
        self.container.append(data)
        print(self.container)
    
    def pop(self):
        self.container.pop()
        print(self.container)
    
    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container)==0
    
    def sizeOfStack(self):
        return len(self.container)




ob=Stack()

print("pushing 45,46 and 47")
ob.push(45)
ob.push(46)
ob.push(47)

print("2 peek operations")
print(ob.peek())
print(ob.peek())

print("2 pop operations")
ob.pop()
ob.pop()

print("IsEmpty ")
print(ob.isEmpty())

print("Pop Operation ")
ob.pop()

print("IsEmpty ")
print(ob.isEmpty())

print("size")
print(ob.sizeOfStack())

print("push Operation")
ob.push(48)

print("size")
print(ob.sizeOfStack())
