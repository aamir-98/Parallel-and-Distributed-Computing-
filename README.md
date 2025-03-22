# DSAI 3202 - Lab 4 (Part 1): Temperature Monitoring System Using Threads

## Overview
This lab simulates a **temperature monitoring system** using **Python threads**, where multiple sensors (threads) generate and update temperature readings at regular intervals. The program uses synchronization techniques like `Lock` and `Condition` to safely update and access shared data. Every 5 seconds, the program displays:
- All current sensor readings
- The average temperature of all sensors

---

## Objectives
- Understand and implement **multithreading** in Python
- Use `threading.Thread`, `Lock`, and `Condition` for thread management
- Share data safely among threads using synchronization mechanisms

---

## Program Structure

```
DSAI3202_Lab4/
├── src/
│   ├── __init__.py
│   └── temperature_sensor.py      # Contains the TemperatureSensor class
└── main.py                        # Entry point that starts sensor threads and monitoring
```

---

## Explanation of Components

### `temperature_sensor.py`
Defines the `TemperatureSensor` class:
- Each sensor is a thread
- Simulates a new temperature (10-40°C) every 1-2 seconds
- Uses locks to safely update shared dictionary `sensor_data`

### `main.py`
- Creates and starts multiple sensor threads
- Every 5 seconds:
  - Acquires lock
  - Displays all sensor readings
  - Computes and prints average temperature

---

## Sample Output
```
=== Temperature Sensor Readings ===
Sensor 1: 18.23 °C
Sensor 2: 19.87 °C
Sensor 3: 26.45 °C
Sensor 4: 20.02 °C
Sensor 5: 22.31 °C

Average Temperature: 21.78 °C
```

---

## Synchronization Techniques Used
- `RLock`: Allows safe simultaneous access to shared resources
- `Condition`: Can be used for notification (not required here but optionally included)
- `Queue`: Alternative structure used for storing sensor values (optional)

---

## Requirements
Use the following dependencies listed in `requirements.txt`:
```
threading
random
time
```
---

## Key Learnings
- Built a concurrent sensor system with threads
- Practiced shared data management and synchronization
- Gained practical experience simulating real-time systems using Python concurrency tools

---

## Author
- **Aamir Ahmed**  
Course: **DSAI 3202 - Parallel and Distributed Computing**
Lab 4 - Part 1

