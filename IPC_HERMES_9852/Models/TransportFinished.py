'''
The TransportFinished message is sent by the upstream machine afer it finished
the transport.

Transfer states: 
    1 NotStarted: The PCB never left and hence is fully inside the upstream machine. 
    2 Incomplete: The transfer was cancelled in progress. 
    3 Complete: The transfer ended successfully. 
If the BoardId does not match the one from StartTransport, this shall
be treated as a protocol error. Therefore, 
the connection would need to be re-established.
'''

class TransportFinished:
    def __init__(self):
        self.TransferState = 1
        self.BoardId = ""