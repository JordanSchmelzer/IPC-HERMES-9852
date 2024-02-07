'''
With the RevokeMachineReady message, the downstream machine signals
that it is not ready anymore to accept PCB

anything is allowed, string is an example.
'''

class RevokeMachineReady:
    def __init__(self):
        self.message=""