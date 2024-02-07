'''
The MachineReady message is sent to the upstream mavhine to indicate the readiness
of the downstream machine to accept a PCB.
'''

class MachineReady:
    def __init__(self):
        self.FailedBoard = 0
        self.ForecastId=""
        self.BoardId=""
        self.ProductTypeId=""
        self.FlippedBoard=0
        self.Length=1.0
        self.Width=1.0
        self.Thickness=1.0
        self.ConveyorSpeed=1.0
        self.TopClearanceHeight=1.0
        self.BottomClearanceHeight=1.0
        self.Weight=1.0
        self.WorkOrder=""