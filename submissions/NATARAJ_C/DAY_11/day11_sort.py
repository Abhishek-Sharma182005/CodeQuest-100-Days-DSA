list=[]
print("Enter numbers: ")
n=0
while (n>=0):
    n=int(input())
    if(n>=0):
        list.append(n)
print("Sorted List: "," ".join(map(str,sorted(list))))  #map function used to every item in an iterable and retruns new iterable

#moreover, using map function, we can print the list without square brackets'[]'