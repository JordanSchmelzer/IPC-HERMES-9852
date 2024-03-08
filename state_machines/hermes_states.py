import asyncio
import xml.etree.ElementTree as ET

class ProtocolState:
    def handle(self) -> None:
        raise NotImplementedError()
        
class NotConnected(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self, message: str):
        # I expect to see a ServiceDescription from the downstream machine/client
        #what is the machine_id of the message?
        parser = ET.XMLParser(encoding="UTF-8")
        
        test = """<?xml version="1.0"?>"""
        try:
            tree = ET.fromstring(message,parser=parser)
            tree.find
            machine_id = tree.find("MachineId")
            #print(machine_id.text)
            for elem in tree.iter():
                print(elem)
        except Exception as e:
            print(f"[ERROR]: {e}")

class ServiceDescriptionDownstream(ProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
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
    def __init__(self):
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
        
    def handle(self):
        self.state.handle()
        
if __name__ == "__main__":
    this_machine = Machine() # initialize not connected
    this_machine.handle()