import threading
import time
import random

# Global variable
sensor_data = {'temperature': 0, 'pressure': 0}
lock = threading.Lock()

# 1. Sensor Reading Thread
def read_sensors():
    while True:
        temp = random.randint(70, 120)      # Dummy temperature
        pressure = random.randint(30, 90)   # Dummy pressure
        with lock:
            sensor_data['temperature'] = temp
            sensor_data['pressure'] = pressure
        print(f"[SENSOR] Temp: {temp}°C, Pressure: {pressure} PSI")
        time.sleep(2)

# 2. Logging Thread
def log_data():
    while True:
        with lock:
            temp = sensor_data['temperature']
            pressure = sensor_data['pressure']
        with open("pump_log.txt", "a") as f:
            log_line = f"Temp: {temp}°C, Pressure: {pressure} PSI\n"
            f.write(log_line)
        print("[LOG] Data logged.")
        time.sleep(5)

# 3. Alert Thread
def check_alerts():
    while True:
        with lock:
            temp = sensor_data['temperature']
            pressure = sensor_data['pressure']
        if temp > 100:
            print(" [ALERT] High Temperature Detected!")
        if pressure > 80:
            print(" [ALERT] Pressure Too High!")
        time.sleep(3)

# Thread creation
t1 = threading.Thread(target=read_sensors)
t2 = threading.Thread(target=log_data)
t3 = threading.Thread(target=check_alerts)

# Start threads
t1.start()
t2.start()
t3.start()