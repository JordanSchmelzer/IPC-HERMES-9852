'''
The BoardArrived message is sent via Hermes vertical channel to a
supervisory system to indicate that a PCB has  arrived  at  this  machine.
The  BoardArrived  message  shall  be  sent  immediately  after  
sending  the corresponding StopTransport message. 

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