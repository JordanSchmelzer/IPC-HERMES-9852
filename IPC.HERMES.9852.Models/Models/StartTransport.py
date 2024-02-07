'''
The StartTransport message is sent to the upstream machine to initiate the PCB
handover process.

The downstream machine is responsible for selecting the acutal conveyor speed
according to the preferred conveyor speed sent in the BoardAvailable message.
In general the highest possible speed supported by both machines will be selected.

If a StartTransport message is recieved for a BoardID which is not the one received
with the last BoardAvailable message the transport shall be canceled.
This case is not to be treated as a protocol error.
'''

class StartTransport:
    def __init__(self):
        self.BoardId=""
        self.ConveyorSpeed=1.0