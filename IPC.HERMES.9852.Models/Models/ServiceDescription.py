'''
The ServiceDescription message is sent by both machines after a connection is established. The downstream 
machine  sends  its  ServiceDescription  first  whereupon  the  upstream  machine  answers  by  sending  its  own 
ServiceDescription. 
'''

class ServiceDescription:
    def __init__(self):    
        self.MachineId = ""
        self.LaneId = 0
        self.InterfaceId = ""
        self.Version = [
            [],
            [],
            [],
            []   
        ]
    