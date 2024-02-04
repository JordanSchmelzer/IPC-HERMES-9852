'''
The QueryBoardInfo message is sent to the upstream machine
to request information about one of the last boards.

If FeatureQueryBoarrdInfo is specified in ServiceDescription,
it must be fully supported, else ignored.

Either top or bottom barcode must be specified

PARAMS:
TopBarcode: (String)
    The barcode of the top side of the PCB.
BottomBarcode: (string)
    The barcode of the bottom side of the PCB.
'''

class QueryBoardInfo:
    __slots__ = ("TopBarcode","BottomBarcode")
    
    def __init__(self):
        self.TopBarcode = ""
        self.BottomBarcode = ""