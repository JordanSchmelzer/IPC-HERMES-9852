import socket
import logging
import time
import os
import xml


FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
DEFAULT_PORT = 8081
HOST = "10.0.0.124"
ADDR = (HOST,DEFAULT_PORT)
HEADER = 64
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# protocol goes here
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
send("Hello World!")
send("Send can be called more than once")
send(DISCONNECT_MESSAGE)     