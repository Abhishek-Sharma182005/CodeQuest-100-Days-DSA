class fenwickTree:
    def __init__(self,size):
        self.tree = [0] * (size + 1)

    def update(self,i,value):
        i += 1
        while i < len(self.tree):
            self.tree[i] += value
            i += i & -i
    def query(self, i):
        i += 1
        total = 0
        while i >0:
            total  += self.tree[i]
            i -= i & -i
        return total 
arr = list(map(int,input("Initial Traffic Data: ").split()))
n = len(arr)
bit = fenwickTree(n)

for i in range(n):
    bit.update(i,arr[i])

q = int(input("Number of queries: "))
for _ in range(1,q + 1):
    query = input("Enter query: ").lower().split()

    if query[0] == "query":
        index = int(query[-1])
        values = arr[:index + 1]
        total = bit.query(index)
        print(f"Prefix sum (index{index}):{' + '.join(map(str,values))} = {total}")
    elif query[0] == "update":
        index = int(query[2])
        add_value = int(query[-1])
        arr[index] += add_value
        bit.update(index,add_value)
