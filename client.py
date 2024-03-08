import socket
import os
import xml.etree.ElementTree as ET


ENCODING = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
DEFAULT_PORT = 50100
HOST = "127.0.0.1"
ADDR = (HOST,DEFAULT_PORT)
BUFFER_SIZE = 1024
 

def pad(data: str, pad_len: int, padding: chr, left=True) -> str:
    add_padding = pad_len - data.__len__
    
    if add_padding == 0:
        print(f'[WARN] data already at desired pad_len: {pad_len}')
        return data
    if add_padding < 0:
        print(f'[ERROR] desired final length: {pad_len} is less than data length: {data.__len__}')
        return
    
    if left:
        padded_data = add_padding * padding + data
    else:
        padded_data = data + add_padding * padding
    
    return  padded_data
    

# protocol goes here
def send(msg):
    message = msg.encode(ENCODING)
    msg_length = len(message)
    send_length = str(msg_length).encode(ENCODING)
    send_length += b' ' * (BUFFER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    
tree = ET.parse('./IPC_HERMES_9852/Messages/xml/CheckAliveMessage.xml')
hermes_message = tree.getroot()

#TIMESTAMP
timestamp = hermes_message.get('Timestamp')
# print(f'Hermes timestamp: {timestamp}')

# for child in hermes_message:
    # print(child.tag, child.attrib)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)
client.connect(ADDR)

send("""<?xml version="1.0"?>
     <Hermes Timestamp="2017-07-16T19:20:30.452">
        <ServiceDescription>
            <MachineId>rattle</MachineId>
            <LaneId></LaneId>
            <InterfaceId></InterfaceId>
            <Version></Version>
            <SupportedFeatures>
                <Feature1></Feature1>
            </SupportedFeatures>
        </ServiceDescription>
    </Hermes>""")
send(DISCONNECT_MESSAGE)