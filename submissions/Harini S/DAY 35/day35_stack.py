class Stack:
    def __init__(self,size):
        self.size=size
        self.stack=[None]*size
        self.tos=-1
    def push(self,value):
        if self.tos>=self.size-1: print("Stack overflow")
        else:
            self.tos+=1
            self.stack[self.tos]=value
    def pop(self):
        if self.tos==-1: print("Stack underflow")
        else:
            self.stack[self.tos]=None
            self.tos-=1
    def display(self):
        if self.tos==-1: print("stack underflow")
        else:
            print("Current Stack:",end=" ")
            for i in self.stack[:self.tos+1]: print(i,end=" ")
lis=list(map(int,input("Input: ").split()))
pop_value=int(input("Enter pop value:"))
s=Stack(len(lis))
for i in lis: s.push(i)
for i in range(pop_value): s.pop()
s.display()