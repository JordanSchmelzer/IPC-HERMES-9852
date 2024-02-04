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

Params:
QueryId: (string)
    Indicates the ID of QueryWorkOrder message. The ID must be unambiguous
    and e.g. can be a timestamp or a GUID
MachineId: (string)
    ID/name of this machine for identifying it in a Hermes 
    enabled production line.
MagazineId: (string)
    Barcode of the magazine, required to identify the magazine
SlotId: (int)
    Indicates the slot in the magazine. enumerated from bottom to top,
    beginning with 1
Barcode: (string)
    The barcode of the PCB
'''


class QueryWorkOrderInfo:
    __slots__ = ("QueryId"
                 ,"MachineId"
                 ,"MagazineId"
                 ,"SlotId"
                 ,"Barcode"
                 )
    
    def __init__(self):
        self.QueryId = "asdf"
        self.MachineId = "asdf"
        self.MagazineId = "asdf"
        self.SlotId = 1
        self.Barcode = "asdf"
        
