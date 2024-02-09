'''
The SendWorkOrderInfo message is sent via Hermes vertical channel from a supervisory system to a machine 
to  provide  the  work  order  and  the  initial  board  data  for  a  PCB  or  a  set  of  PCBs.  If  the  supervisory  system 
cannot find any work order information it will nevertheless send the SendWorkOrderInfo message without any 
attributes except QueryId, if provided upon reqeuest. 
 
Note:  The  function  of  SendWorkOrderInfo  is  optional.  If  FeatureSendWorkOrderInfo  is  specified  in  the 
SupervisoryServiceDescription, it must be fully supported. Otherwise it can be ignored.

GUID must match the regular expression 
[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12} 
 
FailedBoard may be one of the following values: 
0 Board of unknown quality available 
1 Good board available
2 Failed board available 
 
FlippedBoard may be one of the following values: 
0 Side up is unknown 
1 Board top side is up 
2 Board bottom side is up
'''

class SendWorkOrderInfo:
    def __init__(self):
        self.QueryId = ""
        self.WorkOrderId = ""
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