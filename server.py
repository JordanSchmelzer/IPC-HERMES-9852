import asyncio
from asyncio import AbstractEventLoop
import socket
from typing import List
from state_machines import hermes_states

HOST: str = '127.0.0.1'
PORT: int = 50100
ADDR: tuple = (HOST, PORT)
BUFFER_SIZE: int = 1024
ENCODING: str = 'utf-8'
XML_HEADER: str = '<?xml version="1.0" encoding="UTF-8"?>'
DISCONNECT_MESSAGE: str = '!DISCONNECT'


async def connection_handler(conn: socket, addr: tuple):
    print(f"[INFO]: Handling message from {addr}")
    
    connected = True
    while connected:
        try:
            data_len = await loop.sock_recv(conn, BUFFER_SIZE)
            data_len = int(data_len)
            message = await loop.sock_recv(conn,data_len)
            message = message.decode(ENCODING)
            
            if message == DISCONNECT_MESSAGE:
                connected = False
                print(f"[INFO]: Client disconnected: {addr}")
                conn.close()
                
            if message != DISCONNECT_MESSAGE:
                await this_machine.state.handle(message, conn)
        except Exception as e:
            print(f"[ERROR]: {e}")
    

async def connection_listener(server_socket, loop):
    while True:
        conn, addr = await loop.sock_accept(server_socket)
        conn.setblocking(False)
        print(f"[INFO]: Got a connection from {addr}")
        message_task = asyncio.create_task(connection_handler(conn, addr))
        tasks.add(message_task)


class GracefulExit(SystemExit):
    pass


def shutdown():
    print("[TRACE]: Shutting down with GracefulExit")
    raise GracefulExit()


async def close_tasks(tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task,2) for task in tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            print("[ERROR]: A task timed out")
            pass


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.setblocking(False)
    server_socket.bind(ADDR)
    print(f"[LISTENING]: Server listening on HOST {HOST} PORT {PORT}")
    server_socket.listen()
    
    await connection_listener(server_socket, loop)


if __name__ == "__main__":
    downstream_machines = []
    upstream_machines = []
    tasks = set()
    
    loop = asyncio.new_event_loop()
    this_machine = hermes_states.Machine()
    
    try:
        print(f"[STARTUP]: Starting Server")
        loop.run_until_complete(main())
    except GracefulExit:
        loop.run_until_complete(close_tasks())
    finally:
        print(f"[SHUTDOWN] Shutting down the server")
        loop.close()