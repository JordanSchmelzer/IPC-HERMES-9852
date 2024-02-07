'''
With the RevokeBoardAvailable message the upstream machine signals that it
is not ready anymore to handover a PCB.

literally any message is allowed as long as its a string
'''

class RevokeBoardAvailable:
    def __init__(self):
        self.message = ""