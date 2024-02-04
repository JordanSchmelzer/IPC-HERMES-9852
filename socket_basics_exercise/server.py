import socket
import threading
import xml


HOST = socket.gethostbyname(socket.gethostname())
PORT = 8081
ADDR = (HOST, PORT)
HEADER = 64 # bytes to reprersent a number.
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# This is where the protocol goes
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # blocking, #bytes
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) # blocking, msg
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECTED] fom host: {addr}")
             
        print(f"[{addr}] {msg}")
        # conn.send("Msg recieved".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()  # blocking
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIOINS] {threading.active_count() - 1}")


print(f"[STARTING] host: {HOST}, port: {PORT}")
start()