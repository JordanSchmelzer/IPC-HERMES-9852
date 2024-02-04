'''
The BoardArrived message is sent via Hermes vertical channel to a
supervisory system to indicate that a PCB has  arrived  at  this  machine.
The  BoardArrived  message  shall  be  sent  immediately  after  
sending  the corresponding StopTransport message. 

Params:
MachineId: (string)
    ID / name of this machine for identifying it in a Hermes enabled production line.
UpstreamLaneId: (int)
    The lane on the upstream side. Lanes are enumerated looking 
    downstream  from  right  to  left  beginning 
    with 1.
UpstreamInterfaceId: (string)
    The  ID  of  the  transportation  interface  on 
    the upstream side.
MagazineId: (string)
    Barcode of a magazine, required to 
    identify the magazine from which the 
    Board was transferred
SlotId: (int)
    Indicates the slot in the magazine, 
    enumerated from bottom to top, beginning 
    with 1.
BoardTransfer: (int)
    A value of the list below
BoardId: (string)
    Indicating the GUID of the available board
BoardIdCreatedBy: (string)
    MachineId  of  the  machine  which  created the BoardID
    (the first machine in a 
    consecutive row of machines implementing this protocol). 
    The MachineId is part of the Hermes configuration.
FailedBoard: (int)
    A value of the list below. 
ProductTypeId: (string)
    Identifies a collection of PCBs sharing 
    common properties. 
FlippedBoard: (int)
    A value of the list below
TopBarcode: (string)
    The barcode of the top side of the PCB
BottomBarcode: (string)
    The  barcode  of  the  bottom  side  of  the PCB.
Length: (float)
    PCB transfer in millimeter per second
Width: (float)
    PCB transfer in millimeter per second
Thickness: (float)
    PCB transfer in millimeter per second
ConveyorSpeed: (float)
    The  conveyor  speed  used  for  the  PCB transfer in millimeter per second
TopClearanceHeight: (float)
    The clearance height for the top side of the PCB in millimeter. 
BottomClearanceHeight: (float)
    The clearance height for the bottom side of the PCB in millimeter
Weight: (float)
    The weight of the PCB in grams.
WorkOrderId: (string)
    Identifies the work order for production of the PCB.
    
FailedBoard may be one of the following values: 
0 Board of unknown quality available 
1 Good board available 
2 Failed board available 
 
FlippedBoard may be one of the following values: 
0 Side up is unknown 
1 Board top side is up 
2 Board bottom side is up 
 
BoardTransfer may be one of the following values: 
1 Transferred: Board arrived from upstream machine via Hermes or SMEMA. 
2 Loaded: Board was loaded from a magazine or a stack of Boards. 
3 Inserted: Board was manually inserted into the machine. 
'''

class BoardArrived:
    __slots__ = ("MachineId"
                 ,"UpstreamLaneId"
                 ,"UpstreamInterfaceId"
                 ,"MagazineId"
                 ,"SlotId"
                 ,"BoardTransfer"
                 ,"BoardId"
                 ,"BoardIdCreatedBy"
                 ,"FailedBoard"
                 ,"ProductTypeId"
                 ,"FlippedBoard"
                 ,"TopBarcode"
                 ,"BottomBarcode"
                 ,"Length"
                 ,"Width"
                 ,"Thickness"
                 ,"ConveyorSpeed"
                 ,"TopClearanceHeight"
                 ,"BottomClearanceHeight"
                 ,"Weight"
                 ,"WorkOrderId"
                 )
    
    def __init__(self):
        self.MachineId = "this_machine_id"
        self.UpstreamLaneId = 1
        self.UpstreamInterfaceId = "interface_id"
        self.MagazineId = "mag_id"
        self.SlotId = 1
        self.BoardTransfer = 1
        self.BoardId = "123e4567-e89b-12d3-a456-426655440000"
        self.BoardIdCreatedBy = "guid_origin_machine"
        self.FailedBoard = 0
        self.ProductTypeId = "part_number_content"
        self.FlippedBoard = 0
        self.TopBarcode = "top_barcode_content"
        self.BottomBarcode = "bottom_barcode_content"
        self.Length = 1.00
        self.Width = 1.00
        self.Thickness = 1.00
        self.ConveyorSpeed = 1.00
        self.TopClearanceHeight = 1.00
        self.BottomClearanceHeight = 1.00
        self.Weight = 1.00
        self.WorkOrderId = "0"