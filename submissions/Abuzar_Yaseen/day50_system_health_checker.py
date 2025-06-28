reading = list(map(float,input("Enter system sensor readings: ").split()))

count = len(reading)
total = sum(reading)
mean = total / count

var = 0
for value in reading :
    var += (value -mean) ** 2
    variance = var /count

variance = var /count
std_deviation = variance ** 0.5

print("Average: ",round(mean,2))
print("Variance: ",round(variance,2))
print("Standard Deviation: ",round(std_deviation,2))
