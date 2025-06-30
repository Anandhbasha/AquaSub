import socket
from datetime import datetime
from pymongo import MongoClient

# Step 1: MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["pump_factory"]
collection = db["sensor_readings"]

# Step 2: Create UDP server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))

print(" UDP Server Started with MongoDB Integration...")

# UDP max payload size is 65507 bytes (theoretical limit)
# But usually, 512 to 4096 bytes 

while True:
    data, addr = server.recvfrom(1024)
    decoded = data.decode()
    temp, pressure = map(float, decoded.split(","))

    now = datetime.now()
    log = f"[{now}] From {addr} Temp: {temp}°C | Pressure: {pressure} bar"
    print(log)

    # Step 3: Save to MongoDB
    sensor_data = {
        "timestamp": now,
        "ip": addr[0],
        "temp": temp,
        "pressure": pressure
    }
    collection.insert_one(sensor_data)

    # Step 4: Log alerts
    if temp > 55:
        with open("alerts.txt", "a") as f:
            f.write(log + " HIGH TEMP ALERT!\n")
        print("ALERT! High Temperature logged and stored.")