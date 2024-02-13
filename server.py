import socket
import xml.etree.ElementTree as ET
import threading
import time
from IPC_HERMES_9852.Messages import ServiceDescriptionMessage
from IPC_HERMES_9852.Models import ServiceDescription

# Define constants
HOST = '127.0.0.1'
PORT = '50100'
BUFFER_SIZE = 1024
ENCODING = 'utf-8'
XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>'
DISCONNECT_MESSAGE = '!DISCONNECT'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    service_description_downstream = conn.recv().decode(ENCODING)
    if service_description_downstream:
        msg_length = int(service_description_downstream)
        service_description_downstream = conn.recv(msg_length).decode(ENCODING)
    
    # Answer with own ServiceDescription and establish check alive loop
    service_description_server = ServiceDescription()
    service_description_server = ServiceDescriptionMessage.ServiceDescriptionMessage()
    conn.send(service_description_server).encode(ENCODING)
    connected = True
    
    while connected:
        # global time since last check alive
        
        # listen for the check alive message
        # if a message isnt recieved in 3 seconds, send disconnect to client, kill conn
        
        # respond to downstream machine with check alive 
        pass


def start():
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = server_socket.accept()  # blocking
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIOINS] {threading.active_count() - 1}")

print(f"[STARTING] host: {HOST}, port: {PORT}")
start()