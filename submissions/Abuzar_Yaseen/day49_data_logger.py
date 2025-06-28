readings = input("Enter sensor readings: ").split()
readings = [float(x) for x in readings]

avg = sum(readings) / len(readings)
min_val = min(readings)
max_val = max(readings)

print("Average: ",avg)
print("Minimum: ",min_val)
print("Maximum: ",max_val)