# Memoization dictionary
memo = {}

# Recursive Fibonacci function with memoization
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Take input
n = int(input("Enter n: "))

# Output the result
print("Fibonacci number:", fibonacci(n))