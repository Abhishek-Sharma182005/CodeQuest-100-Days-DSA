scores=list(map(int,input("Enter module scores (space-separated):").split()))
debug=[]
if any(i<50 for i in scores):
    print("Modules to debug:")
    for i in scores:
        if i<50:
            print(i,end=' ')
else: print("All modules are working fine!")
