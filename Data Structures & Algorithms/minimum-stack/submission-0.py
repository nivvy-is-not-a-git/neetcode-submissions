class MinStack:

    def __init__(self):
        self.top_i=-1
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_i+=1

    def pop(self) -> None:
        del self.stack[self.top_i]
        self.top_i-=1

    def top(self) -> int:
        if self.top_i>-1:
            return self.stack[self.top_i]
        else:
            return None

    def getMin(self) -> int:
        self.sorted_stack= self.stack.copy()
        self.sorted_stack.sort()
        if self.top_i>-1:
            return self.sorted_stack[0]
        else:
            return None
        
