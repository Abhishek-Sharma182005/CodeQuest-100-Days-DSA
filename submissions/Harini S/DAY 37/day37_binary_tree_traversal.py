class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def binarytree(values):
    if not values:
        return None
    Nodes=[node(val) for val in values]
    root=Nodes[0]
    i=0 #parent index
    j=1 #child index
    while j<len(values):
        if i<len(Nodes):
            if j<len(Nodes):
                Nodes[i].left=Nodes[j]
                j+=1
            if j<len(Nodes):
                Nodes[i].right=Nodes[j]
                j+=1
        i+=1
    return root
def inorder_traversal(Node):
    if Node:       
        inorder_traversal(Node.left)
        print(Node.value,end=" ")     
        inorder_traversal(Node.right)
lis=list(map(int,input("Enter values:").split()))
root=binarytree(lis)
print("Inorder Traversal:")
inorder_traversal(root)

