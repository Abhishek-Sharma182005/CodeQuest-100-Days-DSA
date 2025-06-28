import threading
import time
import random

def temperature_sensor():
    for _ in range(10):
        temp = random.randint(20,30)
        print(f"[Temperature Sensor] Temperature: {temp} C")
        time.sleep(1)

def humidity_sensor():
    for _ in range(10):
        humid = random.randint(40,60)
        print(f"[Humidity Sensor] Humidity: {humid}%")
        time.sleep(1)

temp_thread = threading.Thread(target=temperature_sensor)
humid_thread = threading.Thread(target=humidity_sensor)

temp_thread.start()
humid_thread.start()

temp_thread.join()
humid_thread.join()

print("Sensor simulation complete.")