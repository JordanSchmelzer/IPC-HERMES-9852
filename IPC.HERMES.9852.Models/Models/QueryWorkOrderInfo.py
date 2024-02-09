'''
The QueryWorkOrderInfo message is sent via Hermes vertical channel
from a machine to a supervisory system to query the work order and
initial board data for a PCB or a set of PCBs.
Three scenarios are covered:
    a) PCBs arrive within a magazine
    b) A stack of PCBs arrives
    c) A PCB is inserted and its barcode is known

Optional, if this is specified in SupervisoryServiceDescription, it must
be fully supported, else ignore.
'''

class QueryWorkOrderInfo:
    def __init__(self):
        self.QueryId = ""
        self.MachineId = ""
        self.MagazineId = ""
        self.SlotId = 1
        self.Barcode = ""
        
