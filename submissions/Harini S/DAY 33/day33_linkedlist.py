class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.start=None
    def insert_at_end(self,value):
        newnode=Node(value)
        if self.start is None:
            self.start=newnode
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
    def display(self):
        temp=self.start
        while temp is not None:
            print(f"{temp.data} ->",end=" ")
            temp=temp.next
        print("NULL")

s=sll()
lis=list(map(int,input("Enter list:").split()))
for i in lis: s.insert_at_end(i)
s.display()