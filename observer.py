from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class IObservable(ABC):
    '''
    The Observable interface declares a set of methods for managing subscribers
    '''
    
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        """
        Attach an observer to the subject.
        """
        pass
    
    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        """
        Detach an obserrver from the subject.
        """
        pass
    
    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event
        """
        pass
    

class ObservableMachine(IObservable):
    """
    The Observable owns some important state and notifies observers when the state changes.
    This could be the Hermes machine or protocol
    """
    
    _state: str = "not_connected"
    """
    For simplicity the Subject's state, essential to all subscribers, is storerd in this variable
    This could be the state of the state machine?
    """
    
    _observers: List[IObserver] = []
    """
    List of subscribers. there's more ways to do this, you can seperate
    subscribers by type, ect...
    This could be the machine layer like a conveyor belt
    """
    
    def attach(self, observer: IObserver) -> None:
        print("Subject: Attached an observer")
        self._observers.append(observer)
        
    def detach(self, observer: IObserver) -> None:
        self._observers.remove(observer)
        
    """
    The subscription management methods.
    """
    
    def notify(self)->None:
        for observer in self._observers:
            observer.update(self)
            
    def some_business_logic(self)->None:
        """
        Usually, the subsciption logic is only a fraction of what a Subject
        can really do. Subjects commonly hold some imporrrtant buisness
        logic, that triggers a notification method whenever something imporrtant is about
        to happen (or after it).
        
        this business logic could be protocol stuff
        """
    
        print("\nSubject: I'm doing something important.")
        self._state = "service_description_downstream"

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
        
        
class IObserver(ABC):
    """
    The Observer interrface declarers the update method, used by Observables
    """
    
    @abstractmethod
    def update(self, subject: IObservable)->None:
        """
        Recieve update from subject.
        """
        pass
    

"""
Concrete Observers react to the updates issued by the Observable they had been attached to.
These could be machine parts like a belt or light
"""    


class ConcreteObserverConveyorBelt(IObserver):
    def update(self, subject: IObservable)->None:
        if subject._state == "not_connected":
            print("ConcreteObserverConveyorBelt: Conveyor Belt is off, not_connected")
        elif subject._state == "service_description_downstream":
            print("ConcreteObserverConveyorBelt: Conveyor Belt still off, service_description_downstream")
            

class ConcreteObserverConnectionLight(IObserver):
    def update(self, subject: IObservable)->None:
        if subject._state == "not_connected":
            print("ConcreteObserverConnectionLight: Conveyor Belt is off, not_connected")
        elif subject._state == "service_description_downstream":
            print("ConcreteObserverConnectionLight: Conveyor Belt still off, service_description_downstream")
    
    
if __name__ == "__main__":
    # The client code.
    observable_object = ObservableMachine()
    
    observer_a = ConcreteObserverConveyorBelt()
    observable_object.attach(observer_a)
    
    observer_b = ConcreteObserverConnectionLight()
    observable_object.attach(observer_b)
    
    observable_object.some_business_logic()
    observable_object.some_business_logic()
    
    observable_object.detach(observer_a)
    
    observable_object.some_business_logic()