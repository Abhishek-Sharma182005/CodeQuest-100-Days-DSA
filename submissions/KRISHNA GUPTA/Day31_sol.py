numbers=list(map(int, input("Enter numbers: ").split()))
K=int(input("Enter rotation value (K): "))

K= K % len(numbers)
rotated = numbers[-K:] + numbers[:-K]  
print("Rotated Array: ", *rotated)