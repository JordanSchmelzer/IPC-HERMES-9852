'''
sent via Hermes vertical channel to a supervisory system to indicate that a PCB
has left this machine. This message shall be sent immediatly after sending the
coorresponding TransportFinished Message.
'''

class BoardDeparted:
    def __init__(self):
        self.MachineId = ""
        self.DownstreamLaneId = 1
        self.DownstreamInterfaceId = ""
        self.MagazineId = ""
        self.SlotId = 1
        self.BoardTransfer = 1
        self.BoardId = ""
        self.BoardIdCreatedBy = ""
        self.FailedBoard = 0
        self.ProductTypeId = ""
        self.FlippedBoard = 0
        self.TopBarcode = ""
        self.BottomBarcode = ""
        self.Length = 1.0
        self.Width = 1.0
        self.Thickness = 1.0
        self.ConveyorSpeed = 1.0
        self.TopClearanceHeight = 1.0
        self.BottomClearanceHeight = 1.0
        self.Weight = 1.0
        self.WorkOrderId = ""