binary_input = input("Enter binary number: ")
try:
    decimal_output = int(binary_input,2)
    print("Decimal:",decimal_output)
except ValueError:
    print("Invalid binary number! please enter only 0s and 1s.")    