
from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque() #Deque initialisation
    def push(self,val):
        self.container.append(val) #Append value
    def pop(self):
        return self.container.pop() #Remove and retuen top element
    def peek(self):
        return self.container[-1] #Return top element
    def is_empty(self):
        return len(self.container)==0  #Checking stack is empty
    def size(self):
        return len(self.container)  #Return stack size
    

#stack instance
s=Stack()

#Push elements into stack    
s.push('book')
s.push('look')
s.push('shook')
s.push('took')

#Display
print("Top element:",s.peek()) 
print("Popped element:", s.pop()) 
print("Stack after pop:", list(s.container))