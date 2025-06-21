binary_signal=list(map(int, input("Enter binary signal:").split()))
count=0
for parity in binary_signal:
    if parity==1:
        count+=1
    
if count %2==0:
    print("Even parity")
else:
    print("Odd Parity – Error Detected!")
