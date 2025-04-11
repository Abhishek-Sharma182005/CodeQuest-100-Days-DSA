elements = list(map(int, input("Enter numbers: ").split())) # get the input from the user and map it with integer
# it takes each value separated with space
print("Sorted List: ", *sorted(elements)) # * is used to print the elements in the list without specifies the list
