alerts = []
print("Alert list: ")

while True: 
    line = input()
    if not line :
        break
    if "with priority" in line:
        parts = line.split("with priority")
        desc = parts[0].split(".",1) [-1].strip().strip('"')
        priority = int(parts[1].strip()) 
        alerts.append((priority,desc))

sorted_alerts = []
for alert in alerts:
    i = 0
    while i < len(sorted_alerts) and alert[0] >= sorted_alerts[i][0]:
        i += 1
    sorted_alerts.insert(i,alert)

print("\n Processing Alerts: ")
i = 1
for aler in sorted_alerts:
    p,d = aler
    print(f"{i}. {d} (Priority:{p})")
    i +=1 
    

