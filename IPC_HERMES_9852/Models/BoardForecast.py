'''
The  BoardForecast  message  is  sent  to  the  downstream  machine  to  indicate  some  changes  /  command 
execution are needed or to give advanced information about the next board but a PCB is not yet available. If 
the ForecastId attribute is set then the downstream machine must at some point respond with a MachineReady 
carrying the same ForecastId. If needed downstream machine must send a RevokeMachineReady message 
first.  If  the  forecasted  product  is  not  accepted  by  the  downstream  machine,  then  it  must  respond  with  a 
Notification of type “BoardForecastError”. 
'''

class BoardDeparted:
    def __init__(self):
        self.ForecastId = ""
        self.TimeUntilAvailable = ""
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
        self.TopClearanceHeight =1.0
        self.BottomClearanceHeight = 1.0
        self.Weight = 1.0
        self.WorkOrderId = ""