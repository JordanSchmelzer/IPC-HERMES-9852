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
        ForecastId = ""
        TimeUntilAvailable = ""
        BoardId = ""
        BoardIdCreatedBy = ""
        FailedBoard = 0
        ProductTypeId = ""
        FlippedBoard = 0
        TopBarcode = ""
        BottomBarcode = ""
        Length = 1.0
        Width = 1.0
        Thickness = 1.0
        ConveyorSpeed = 1.0
        TopClearanceHeight =1.0
        BottomClearanceHeight = 1.0
        Weight = 1.0
        WorkOrderId = ""