class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
         
        return self.stack2[-1]
        
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
        
    def push(self, value):
        self.stack1.append(value)

queue = MyQueue()
t = int(input("Enter number of operations: "))
for line in range(t):
    values = map(int, input("Use '1' to push, '2' to pop, and '3' to peek:").split())
    values = list(values)
    if values[0] == 1:
        queue.push(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())