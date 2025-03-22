import threading
import random
import time
from queue import Queue

class TemperatureSensor(threading.Thread):
    def __init__(self, sensor_id, temperature_data, lock, condition, avg_queue):
        super().__init__()
        self.sensor_id = sensor_id
        self.temperature_data = temperature_data
        self.lock = lock
        self.condition = condition
        self.avg_queue = avg_queue

    def run(self):
        while True:
            new_temp = round(random.uniform(15.0, 30.0), 2)
            with self.lock:
                self.temperature_data[self.sensor_id] = new_temp
                self.avg_queue.put(new_temp)
                self.condition.notify_all()
            time.sleep(random.uniform(1, 2))