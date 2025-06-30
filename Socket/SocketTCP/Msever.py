import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"From {address}: {data.decode()}")
        except:
            break
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(53)  # accept 53 client connections

print("TCP Server running...")

while True:
    client_socket, addr = server.accept()
    print(f"Connected: {addr}")
    threading.Thread(target=handle_client, args=(client_socket, addr)).start()