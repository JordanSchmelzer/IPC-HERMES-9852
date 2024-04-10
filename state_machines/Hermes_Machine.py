import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod 
from typing import List
import asyncio


class IProtocolState:
    async def handle(self) -> None:
        raise NotImplementedError()
        
    def notify_observer() -> None:
        raise NotImplementedError()
    
    
class IObservable(ABC):
    '''
    The Observable Interface declares a set of methods for managing subscribers
    '''
    pass


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
                
                # invoke a command here to send something to server and await a response
                # dododo i am waiting for a response from the connected client
                # i do something with this information
                #   I go to NotAvailableNotReady
                #   I go to not connected
                #   I throw an error?
        except Exception as e:
            print(f"[ERROR]: {e}")
        
class NotAvailableNotReady(IProtocolState):
    """
    Determine if the machine is sending or receiving a board.
    Optional Fully Supported Board Forecast Feature
    """
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        parser = ET.XMLParser(encoding="UTF-8")
        try:
            root = ET.fromstring(message, parser=parser)
            message_type = root.find("")
            if message_type.tag == "":
                machine_id = [message_type.find("MachineId").text]
                print("do something with the message")
                self.machine.state = self.machine.service_description_downstream
                
                # [Optional] first thing i do is a board forecast message to downstream machine
                # [Optional] board forecastId attribute is set then the downstream machine must respond w/ machineready
                # [Optional] if needed downstream machine is going to make a ReveokeMachineReady message
                # [Optional] if the forecasted product is not accepted by the downstream machine then it musut respond with a Notification of type boardForrecast error
                # [Optional] response message must have that same forecstId
                # I await some method from another component. This could be an observer observable thing.
                # maybe like check_for_update or something
                # when i get the thing im after, this happens....
                # either I go to MachineReady or BoardAvailable
            if message == "machine_ready":
                # if i go to machine ready, i will send a message to the upstream machine to indicate downstream machine is ready to accpet pcb
                self.machine.state = self.machine.machine_ready
            if message == "board_available":
                # if I go board available, im asking the downstream machine if its ready for my board
                self.machine.state = self.machine.board_available
        except Exception as e:
            print(f'[ERROR]: {e}')
 
class BoardAvailable(IProtocolState):
    """
    This state waits
    """
    
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        try:
            print("do something with the message")
        except Exception as e:
            print("Error: {e}")
            
    
        
class MachineReady(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        try:
            print("do something with the message")
        except Exception as e:
            print("Error: {e}")
  
class AvailableAndReady(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        try:
            print("do something with the message")
        except Exception as e:
            print("Error: {e}")
        
class Transporting(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        try:
            print("do something with the message")
        except Exception as e:
            print("Error: {e}")
       
class TransportStopped(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        try:
            print("do something with the message")
        except Exception as e:
            print("Error: {e}")

class TransportFinished(IProtocolState):
    def __init__(self, machine):
        self.machine = machine
    
    async def handle(self, message: str):
        try:
            print("do something with the message")
        except Exception as e:
            print("Error: {e}")


class Observer(IObserver):
    """
    This is a compound class of Observer and Receiver
    """
    def update(self, observable: IObservable)->None:
        print(f"Observer: The conveyor belt got an update from {observable}")
        
    def reciever_action(self)->None:
        print("I'm the receiver. Recieved a message from a command")


class Command(ABC):
    """
    The command interface declarrers a method for executing a command
    """

    @abstractmethod
    def execute(self)->None:
        pass
    

class SimpleCommand(Command):
    """
    Do something
    """
    
    def __init__(self, payload: str)->None:
        self._payload = payload 
    
    
    def execute(self)->None:
        print(f"simplecommand: {self._playload}")



class Machine(IObservable):
    """
    State machine state holder/notifier object.
    Also the invoker for now
    ALSO THE INVOKER TOO
    """
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
        self.observers: List[IObserver] = []
        
        self._on_start = None
        self._on_finish = None
        
        
    def set_on_start(self, command: Command):
        self._on_start = command
        

    async def attach(self, observer) -> None:
        print("Observable: Attached an observer")
        self.observers.append(observer)

    async def detatch(self, observer) -> None:
        print("Observable: Detatched an observer")
        self.observers.remove(observer)

    def notify(self)-> None:
        for observer in self.observers:
            observer.update(self)

    async def handle(self, message):
        await self.state.handle(message)
        """
        Handle the TCP payload in one of the finite states
        """

    def do_something_important(self)->None:
        print("CheckOnDone")
        if isinstance(self._on_start, Command):
            self._on_finish.execute()
            
    def transition_state(self, new_state: IProtocolState)->None:
        print(new_state)
        self.state = self.new_state
        

if __name__ == "__main__":
    this_machine = Machine() # initialize not connected
    # this_machine.handle() # make the state change to connected 
    this_machine.state = this_machine.service_description_downstream # do it manually
    this_machine.set_on_start(SimpleCommand("Some data i typed"))    # set a command to be queued
    receiver = Observer
    this_machine.transition_state()