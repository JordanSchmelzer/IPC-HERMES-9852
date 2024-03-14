import asyncio
import socket
import xml.etree.ElementTree as ET


class ProtocolState:
    async def handle(self) -> None:
        raise NotImplementedError()
        
        
class NotConnected(ProtocolState):
    def __init__(self, machine):
        self.machine = machine

    #TODO: Impliment XMLPullParser
    async def handle(self, message: str, conn):
        print("INFO: Checking connection request")
        try:
            root = ET.fromstring(message)
            print(root.tag, root.attrib)
            for child in root:
                print(child.tag, child.attrib)
                if child.tag == "ServiceDescription":
                    new_machine = DownstreamMachine(message, conn)
                    self.machine.downstream_connections.append(new_machine)
                    self.machine.state = self.machine.service_description_downstream
                    print(self.machine.state, new_machine.service_description)
        except Exception as e:
            print(f"[ERROR]: {e}")


class ServiceDescriptionDownstream(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        parser = ET.XMLParser(encoding="UTF-8")
        try:
            root = ET.fromstring(message,parser=parser)
            message_type = root.find("ServiceDescription")
            if message_type.tag == "ServiceDescription":   
                machine_id = [message_type.find("MachineId").text]
                print(f"[INFO]: Recieved ServiceDescription from {machine_id}")     
                self.machine.state = self.machine.service_description_downstream
        except Exception as e:
            print(f"[ERROR]: {e}")
        
class NotAvailableNotReady(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
        
class BoardAvailable(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
        
class AvailableAndReady(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
        
class MachineReady(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
        
class TransportStopped(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")

class Transporting(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
        
class TransportFinished(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
        
class Machine:
    def __init__(self):
        self.upstream_connections = []
        self.downstream_connections = []
        self.currrent_message = ""
         
        self.not_connected = NotConnected(self)
        self.service_description_downstream = ServiceDescriptionDownstream(self)
        self.not_available_not_ready = NotAvailableNotReady(self)
        self.board_available = BoardAvailable(self)
        self.available_and_ready = AvailableAndReady(self)
        self.machine_ready = MachineReady(self)
        self.transport_stopped = TransportStopped(self)
        self.transporting = Transporting(self)
        self.transport_finished = TransportFinished(self)
        
        self.state = self.not_connected
        
    async def handle(self):
        self.state.handle()

class DownstreamMachine:
    def __init__(self, message: str, conn: socket):
        self.service_description = message
        self.socket_conn = conn

class UpstreamMachine:
    def __init__(self, message:str):
        ...

if __name__ == "__main__":
    this_machine = Machine() # initialize not connected
    this_machine.handle()