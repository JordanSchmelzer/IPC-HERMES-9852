'''
The SendBoardInfo message is sent to the downstream machine as response of a received QueryBoardInfo 
message  to  transfer  stored  information  about  one  of  the  last  boards  (see  section 4.1.3).  If  the  upstream 
machine cannot find any board information it will nevertheless send the SendBoardInfo message without the 
BoardId and BoardCreatedBy attributes. 
Machines supporting the feature  FeatureSendBoardInfo  shall be able to store and supply upon request  the 
info of at least the last 50 handled boards. 
 
Note: The function of SendBoardInfo is optional. If FeatureSendBoardInfo is specified in the 
ServiceDescription, it must be fully supported. Otherwise it can be ignored. 

FailedBoard may be one of the following values: 
0 Board of unknown quality available 
1 Good board available 
2 Failed board available 
 
FlippedBoard may be one of the following values: 
0 Side up is unknown 
1 Board top side is up 
2 Board bottom side is up
'''

class SendBoardInfo:
    def __init__(self):
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
        self.TopClearanceHeight = 1.00
        self.BottomClearanceHeight = 1.00
        self.WorkOrderId = "0"