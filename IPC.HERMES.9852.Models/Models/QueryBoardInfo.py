'''
The QueryBoardInfo message is sent to the upstream machine
to request information about one of the last boards.

If FeatureQueryBoarrdInfo is specified in ServiceDescription,
it must be fully supported, else ignored.

Either top or bottom barcode must be specified
'''

class QueryBoardInfo:
    def __init__(self):
        self.TopBarcode = ""
        self.BottomBarcode = ""