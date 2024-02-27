import asyncio
from asyncio import AbstractEventLoop
import socket
import logging
import signal
from typing import List
import xml.etree.ElementTree as ET
from util.delay_functions import *
from IPC_HERMES_9852.Messages import ServiceDescriptionMessage
from IPC_HERMES_9852.Models import ServiceDescription


# Define constants
HOST: str = '127.0.0.1'
PORT: int = 50100
ADDR: tuple = (HOST, PORT)
BUFFER_SIZE: int = 1024
ENCODING: str = 'utf-8'
XML_HEADER: str = '<?xml version="1.0" encoding="UTF-8"?>'
DISCONNECT_MESSAGE: str = '!DISCONNECT'


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.setblocking(False)


async def check_alive_ping(conn: socket, addr) -> None:
    bytes_sent = conn.sendall(("<Hermes><CheckAlive>Ping</CheckAlive></Hermes>").encode(ENCODING))
    logging.debug(f'[INFO] sent this many bytes to addr {bytes_sent}')
                                                                                                               

async def check_alive(conn: socket, addr):
    check_alive_task = asyncio.create_task(delay(1))
    try:
        result = await asyncio.wait_for(check_alive_task, timeout=3)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('failed to print')


def handle_client(conn, addr):
    logging.info(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(BUFFER_SIZE).decode(ENCODING)  # blocking, #bytes
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(ENCODING) # blocking, msg
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECTED] fom host: {addr}")
                return
            
            if msg == "":
                pass
                
            
        print(f"[{addr}] {msg}")
        # conn.send("Msg recieved".encode(FORMAT))

    conn.close()


class GracefulExit(SystemExit):
    logging.critical("Request to exit interpreter, closing program.")
    pass

def shutdown():
    raise GracefulExit()


async def main():
    print(f"[LISTENING] Server is listening on {HOST}")
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()  # blocking
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIOINS] {threading.active_count() - 1}")


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete()
finally:
    loop.close()