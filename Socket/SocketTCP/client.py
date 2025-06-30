import socket
from datetime import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

# Simulated alert message
alert = {
    "machine_id": "Pump_Unit_07",
    "type": "Overheat",
    "value": 72.5,
    "timestamp": datetime.now().isoformat()
}

client.send(str(alert).encode())  # Send as string

# Server response
response = client.recv(1024)
print("Server Response:", response.decode())

client.close()