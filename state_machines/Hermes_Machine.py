import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod 
from typing import List
import asyncio

class IProtocolState:
    async def handle(self) -> None:
        raise NotImplementedError()
        
    def notify_observer() -> None:
        raise NotImplementedError()
   
        
class NotConnected(IProtocolState):
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
                    # new_machine = DownstreamMachine(message, conn)
                    # self.machine.downstream_connections.append(new_machine)
                    self.machine.state = self.machine.service_description_downstream
                    #TODO: do something after setting the state here or in serverv
                    x = Observer()
                    self.machine.observers.append(x)
                    self.machine.notify()
                    # await self.machine.handle()
                    await self.machine.handle(message)
                    
        except Exception as e:
            print(f"[ERROR]: {e}")


class ServiceDescriptionDownstream(IProtocolState):
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
        
        
class NotAvailableNotReady(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
       
        
class BoardAvailable(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
     
        
class AvailableAndReady(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
     
        
class MachineReady(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
    
        
class TransportStopped(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")


class Transporting(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")
  
        
class TransportFinished(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    def handle(self):
        print("do something with the message")


class IObservable(ABC):
    '''
    The Observable Interface declares a set of methods for managing subscribers
    '''



class IObserver(ABC):
    """
    The Observer interrface declarers the update method, used by Observables
    """
    
    @abstractmethod
    def update(self, observable: IObservable)-> None:
        """
        Recieve update fom the Observable object
        """
        pass


class Observer(IObserver):
    def update(self, observable: IObservable)->None:
        print(f"Observer: The conveyor belt got an update from {observable}")


class Machine(IObservable):
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
        """
        Current state of the Machine dictated by Hermes Protocol
        """
        
        self.observers: List[IObserver] = []
        """
        List of subscribers. This could be machine components like a conveyor belt.
        """
        
    async def attach(self, observer) -> None:
        print("Observable: Attached an observer")
        self.observers.append(observer)

    async def detatch(self, observer) -> None:
        print("Observable: Detatched an observer")
        self.observers.remove(observer)

    def notify(self)-> None:
        for observer in self.observers:
            observer.update(self)

    async def some_business_logic(self, input) -> None:
        """
        template: this could have been the handle method
        """
        
        self.state = self.transporting
        print(f'Machine: my state has just changed to {input}')
        self.notify()

    async def handle(self, message):
        await self.state.handle(message)
        """
        Handle the TCP payload in one of the finite states
        """


if __name__ == "__main__":
    this_machine = Machine() # initialize not connected
    this_machine.handle()