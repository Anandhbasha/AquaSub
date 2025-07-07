import serial
import time
import os

# Step 1: Machine port list
machine_ports = {
    "Pump1": "COM3",
    "Pump2": "COM4",
    "Pump3": "COM5"
}

# Step 2: Create folder to store logs
log_dir = "machine_logs"
os.makedirs(log_dir, exist_ok=True)

# Step 3: Connect to all machines
machines = {}
for name, port in machine_ports.items():
    try:
        ser = serial.Serial(port=port, baudrate=9600, timeout=1)
        machines[name] = ser
        print(f" Connected to {name} on {port}")
    except Exception as e:
        print(f" Failed to connect {name} on {port} - {e}")

# Step 4: Read & store every 2 minutes
try:
    while True:
        for name, ser in machines.items():
            if ser.in_waiting > 0:
                data = ser.readline().decode().strip()
                
                # Create filename based on machine
                file_path = os.path.join(log_dir, f"{name}.txt")
                
                # Append data with timestamp
                with open(file_path, "a") as f:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{timestamp}] {data}\n")
                
                print(f" {name}: {data}")
        
        print(" Waiting 2 minutes...\n")
        time.sleep(120)  # 2 minutes

except KeyboardInterrupt:
    print("Stopped manually.")
finally:
    for ser in machines.values():
        ser.close()