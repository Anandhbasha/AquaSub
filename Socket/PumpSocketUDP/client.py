import socket
import random
import time


# network connection create
# This means we're connecting using 'IP addresses' -socket.AF_INET
# socket.SOCK_DGRAM - This means it's a 'UDP' connection. It sends messages but doesn't confirm if they reached the destination. It's faster, but some data might get lost
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Server Address
server_addr = ('localhost', 12345)
# switches = [{},{},{}]
# on=False
# for switch in switches:
#     if on==False:
#         on=True


while True:
    temp = round(random.uniform(40.0, 50.0), 2)
    pressure = round(random.uniform(1.0, 2.5), 2)

    message = f"{temp},{pressure}"
    client.sendto(message.encode(), server_addr) 
    # {}
    print(f"Sent Temp: {temp}°C, Pressure: {pressure} bar")
    time.sleep(2)