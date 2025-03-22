import threading
import time
from queue import Queue
from src.temperature_sensor import TemperatureSensor

NUM_SENSORS = 5

# Shared resources
temperature_data = [0.0] * NUM_SENSORS
lock = threading.RLock()
condition = threading.Condition(lock)
avg_queue = Queue()

# Start sensor threads
sensors = []
for i in range(NUM_SENSORS):
    sensor = TemperatureSensor(i, temperature_data, lock, condition, avg_queue)
    sensor.start()
    sensors.append(sensor)

# Monitor thread to compute average and display
while True:
    time.sleep(5)
    with lock:
        if not avg_queue.empty():
            temps = list(avg_queue.queue)
            avg_temp = round(sum(temps) / len(temps), 2)
            print("\033c", end="")  # Clear terminal
            print("=== Temperature Sensor Readings ===")
            for i, temp in enumerate(temperature_data):
                print(f"Sensor {i+1}: {temp:.2f} °C")
            print(f"\nAverage Temperature: {avg_temp:.2f} °C\n")
