import asyncio
from asyncio import AbstractEventLoop
import socket
from typing import List


HOST: str = '127.0.0.1'
PORT: int = 50100
ADDR: tuple = (HOST, PORT)
BUFFER_SIZE: int = 1024
ENCODING: str = 'utf-8'
XML_HEADER: str = '<?xml version="1.0" encoding="UTF-8"?>'
DISCONNECT_MESSAGE: str = '!DISCONNECT'

downstream_machines = []
upstream_machines = []
tasks = set()

async def add_machine(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        pass
    except Exception as e:
        pass
    finally:
        pass


async def message_handler(conn):
    pass


async def connection_listener(server_socket, loop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        message_task = asyncio.ceate_task(message_handler(connection, loop))
        tasks.add(message_task)

class GracefulExit(SystemExit):
    pass

def shutdown():
    print("Shutting down with GracefulExit")
    raise GracefulExit()

async def close_tasks(tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task,2) for task in tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            print("A task timed out")
            pass

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.setblocking(False)
    server_socket.bind(ADDR)
    print(f"Bound server socket to HOST {HOST} on PORT {PORT}")
    server_socket.listen()
    
    await connection_listener(server_socket, loop)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_tasks())
finally:
    print(f"[SHUTDOWN] Shutting down the server")
    loop.close()