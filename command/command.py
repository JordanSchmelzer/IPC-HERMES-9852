from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """
    The command interface decalers a method for executing a command.
    """
    
    @abstractmethod
    def execute(self)->None:
        pass
    
class SimpleCommand(Command):
    """
    Some commands can implement simple operations on tehir own.
    """
    
    def __init__(self, payload: str)->None:
        self._payload = payload
        
    def execute(self)->None:
        print(f"simplecommand: {self._payload}")
        
class ComplexCommand(Command):
    """
    some commands can delegate morre complex operations to other objects called receiverrs
    """
    
    def __init__(self, receiver: Receiver, a: str, b: str)-> None:
        """
        this can accept lots of inputs if we need it to 
        """
        
        self._receiver = receiver
        self._a = a
        self._b = b
        
    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)
    
class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")
        
class Invoker:
    """
    The Invoker is associated with one or several commands. it sends a request to the command.
    """
    
    _on_start = None
    _on_finish = None
    
    """
    Initialize commands
    """
    
    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
            
        if isinstance(self._on_start, Command):
            self._on_finish.execute()
    
if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
    invoker.do_something_important()