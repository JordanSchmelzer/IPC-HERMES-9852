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
    print(f'[INFO]: sending payload of length {msg_length}')
    send_length = str(msg_length).encode(ENCODING)
    send_length += b' ' * (BUFFER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)

def recieve(msg):
    message_len = client.recv()
    print(message_len)
    message_len = client.recv(len(message_len))
    
    
print(f'[STARTUP]')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Send ServiceDescription To Upstream Machine
send("""<?xml version="1.0"?>
        <Hermes Timestamp="2017-07-16T19:20:30.452">
            <ServiceDescription>
                <MachineId>rattle</MachineId>
                <LaneId>1</LaneId>
                <InterfaceId>1</InterfaceId>
                <Version>1.2</Version>
                <SupportedFeatures>
                    <CheckAlive>True</CheckAlive>
                </SupportedFeatures>
            </ServiceDescription>
        </Hermes>""")

# Recieve the Upsteam Machines ServiceDescription                                                      
message_len = client.recv(2)
print(f'[INFO]: payload length: {message_len.decode("UTF-8")}')
message = client.recv(11)
print(f'[INFO]: payload recieved: {message.decode("UTF-8")}')


# Send MachineReady
send("""<?xml version="1.0"?>
            <Hermes Timestamp="2017-07-16T19:20:30.452">
                <MachineReady>
                    <FailedBoard>0</FailedBoard>
                    <ForecastId>1000000001234</ForecastId>
                    <BoardId>123e4567-e89b-12d3-a456-426655440000</BoardId>
                    <ProductTypeId>TestProduct</ProductTypeId>
                    <FlippedBoard>0</FlippedBoard>
                    <Length>40</Length>
                    <Width>100</Width>
                    <Thickness>2</Thickness>
                    <ConveyorSpeed>30</ConveyorSpeed>
                    <TopClearanceHeight>1</TopClearanceHeight>
                    <BottomClearanceHeight>1</BottomClearanceHeight>
                    <Weight>123</Weight>
                    <WorkOrderId>1780123</WorkOrderId>
                </MachineReady>
            </Hermes>""")


# Disconnect from the upstream machine
send(DISCONNECT_MESSAGE)
print(f'[SHUTDOWN]')