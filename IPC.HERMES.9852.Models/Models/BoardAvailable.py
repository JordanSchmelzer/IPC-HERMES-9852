'''
this message is sent to the downstream machine to indicate the readiness
of the upstreram machine to handover a PCB. When an optional attribute is
received from an upstream machine, then it must be passed on (?altered)
to the next downstream machine.
'''
import xml.etree.ElementTree as ET

class BoardAvailable:
    def __init__(self):
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
        
    def GenerateXML():
        root = ET.Element("Hermes",{"Timestamp":"somedate"})
        print(ET.tostring(root, encoding='utf8').decode('utf8'))
        print(root.atrib)
    
x = BoardAvailable()
x.GenerateXML