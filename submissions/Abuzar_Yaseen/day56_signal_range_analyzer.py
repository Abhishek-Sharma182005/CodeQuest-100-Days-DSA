def build(arr):
    n= len(arr)
    tree = [0] * (2 * n)

    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n -1,0,-1):
        tree[i] = tree[2 * i] + tree[2 * i +1]
        return tree

def range_sum(tree,arr,n,l,r):
    l0,r0 = l,r
    l += n
    r += n
    total = 0
    while l <= r:
        if l % 2 == 1:
            total += tree[l]
            l +=1 
        if r % 2 == 0:
            total += tree[r]
            r -= 1
        l //= 2
        r //= 2
    segment = "+".join(str(x) for x in arr[l0:r0 + 1])
    print(f"Sum for range [{l0},{r0}]: {segment} = {total}")

arr = list(map(int,input("Enter signal strength (space-separated):").split()))
n = len(arr)
tree = build(arr)
q = int(input("Enter number of queries: "))
for i in range(q):
    l,r = map(int,input(f"Query {i+1} - Enter range(start end):").split())
    range_sum(tree,arr,n,l,r)