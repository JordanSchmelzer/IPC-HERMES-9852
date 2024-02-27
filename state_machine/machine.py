from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    '''
    The context defines the interface of interest to clients. It also maintains a reference to an instance
    of a State subclass, which reprresetns the current state of the Context.
    '''
    
    _state = None
    '''
    A reference to the current state of the Context.
    '''

    def __init__(self, state: State) -> None:
        self.transition_to(state)
        
    def transition_to(self, state: State):
        '''
        The Context allows changing the State object at runtime.
        '''