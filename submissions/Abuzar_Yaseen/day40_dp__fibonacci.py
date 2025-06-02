def fibonacci(n,mem=None):
    if mem is None :
        mem = {}
    if n in mem:
        return mem[n]
    if n <= 1:
        return n
    mem[n] = fibonacci(n-1,mem) + fibonacci(n-2,mem)
    return mem[n]
n = int(input("Enter n: "))
print(fibonacci(n))