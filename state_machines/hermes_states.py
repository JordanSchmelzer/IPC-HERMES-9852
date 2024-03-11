import asyncio
import xml.etree.ElementTree as ET

async def check_alive(loop: asyncio.AbstractEventLoop):
    ...

class ProtocolState:
    async def handle(self) -> None:
        raise NotImplementedError()
        
class NotConnected(ProtocolState):
    def __init__(self, machine, loop: asyncio.AbstractEventLoop):
        self.machine = machine
        self.loop = loop
    
    async def handle(self, message: str, socket):
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

class ServiceDescriptionDownstream(ProtocolState):
    def __init__(self, machine, loop: asyncio.AbstractEventLoop):
        self.machine = machine
        self.loop = loop
    
    def handle(self, socket):
         # Send this machines ServiceDescription
        await self.loop.sock_sendall(socket, "11".encode("UTF-8"))
        response = await self.loop.sock_sendall(socket, "hello world".encode("UTF-8"))
        print("do something with the message")
        
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
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.upstream_connections = []
        self.downstream_connections = []
        self.loop = loop
         
        self.not_connected = NotConnected(self, self.loop)
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
        
if __name__ == "__main__":
    this_machine = Machine() # initialize not connected
    this_machine.handle()