packet_data=input("Enter packet data:")
sum=0
for i in packet_data:
    sum+=ord(i)

print("Checksum:",sum%256)

