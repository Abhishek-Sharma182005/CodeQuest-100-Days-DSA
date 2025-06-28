def find_max_signal(signal):
    max_sum = curr_sum = signal[0]
    startt = end = temp_start = 0
    for i in range(1,len(signal)):
        if signal[i] > curr_sum + signal[i]:
            curr_sum = signal[i]
            temp_start = i
        else:
            curr_sum += signal[i]
        if curr_sum > max_sum:
            max_sum = curr_sum 
            start = temp_start
            end = i
    print("Maximum signal Strength:",max_sum)
    print("Strongest Segment:",*signal[start:end+1])

signal = list(map(int,input("Enter signal sttrengths (space-separated):").split()))
find_max_signal(signal)