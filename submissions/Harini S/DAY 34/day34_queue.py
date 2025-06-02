class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,value):
        if self.rear<self.size-1:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue[self.rear]=value
        else:
            print("Queue overflow")
    
    def dequeue(self):
        if self.front==-1 or self.front>self.rear:
            print("Queue underflow")
        else:
            self.queue[self.front]=None
            self.front+=1
    
    def display(self):
        if self.front==-1 or self.front>self.rear: print("Queue underflow")
        else:
            for i in self.queue[self.front:self.rear+1]: print(i,end=" ")
lis=list(map(int,input("Input: ").split()))
deq=int(input("Dequeue: "))
q=Queue(len(lis))
for i in lis: q.enqueue(i)
for i in range(deq): q.dequeue()
print("Remaining queue:",end=" ")
q.display()