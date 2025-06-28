signal_input = input("ENter signal (space-separated): ")
signal = list(map(int,signal_input.strip().split()))
window = int(input("Enter window size(w): "))
smoothed_signal =[]
for i in range(len(signal)-window +1):
    window_signal = signal[i:i+window]
    average = sum(window_signal)
    smoothed_signal.append(average)
print("Smoothed Signal:",''.join(map(str,smoothed_signal)))
