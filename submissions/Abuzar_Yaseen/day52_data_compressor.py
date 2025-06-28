data_packet = input("Enter data packet: ")
if  not data_packet:
    print("Compressed Data: ")
else:
    compressed = " "
    count = 1
    for i in range(1,len(data_packet)):
        if(data_packet[i] == data_packet[i-1]):
            count += 1
        else:
            compressed += str(count) + data_packet[i-1]
            count = 1
    compressed += str(count) + data_packet[-1]
    print("Compressed Data: ",compressed)
