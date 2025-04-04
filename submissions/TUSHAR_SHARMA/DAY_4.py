def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number  % 10
        number //= 10
    return total
        
num =int(input("enter any number: "))
result = sum_of_digits(abs(num))
print(f"sum of the digit : {result}")
