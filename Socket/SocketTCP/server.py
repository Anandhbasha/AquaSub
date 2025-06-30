import socket
import ast
from db import get_collection

collection = get_collection()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(1)

print("TCP Server Ready  Awaiting Alert Messages...")

while True:
    conn, addr = server.accept()
    print("Connected from:", addr)

    data = conn.recv(1024).decode()

    try:
        # Convert string to dictionary
        alert = ast.literal_eval(data)

        # Insert into MongoDB
        collection.insert_one(alert)
        print("Alert saved to DB:", alert)

        conn.send(b"Alert received and saved.")
    except Exception as e:
        print("Error:", e)
        conn.send(b"Invalid alert format")

    conn.close()