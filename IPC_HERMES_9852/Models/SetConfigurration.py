'''
The  SetConfiguration  message  is  sent  by  an  engineering  station  to  configure  the  Hermes  interfaces  of  a 
machine. If the sent configuration is not accepted, the machine is expected to send a Notification message 
(see section 3.5). 
 
Note: The function of SetConfiguration is optional on the vertical channel. If FeatureConfiguration is specified 
in the SupervisoryServiceDescription, it must be fully supported. Otherwise it can be ignored. 

All connections where the machine is acting as board provider are stored in  DownstreamConfigurations. All 
connections where the machine is acting as board receiver are stored in UpstreamConfigurations. These are 
independent of the board transport direction of the SMT line. 
It is up to the user to keep MachineIds unique. 
'''

class SetConfigurration:
    def __init__(self):
        self.MachineId = ""
        self.SupervisorySystemPort = 0
        self.UpstreamConfigurations = [ {"UpstreamLaneId": 0}
                                       ,{"UpstreamInterfaceId": ""}
                                       ,{"HostAddress": ""}
                                       ,{"Port": 65535}
                                       ]
        self.DownstreamConfigurations = [ {"DownstreamLaneId":0}
                                         ,{"DownstreamInterfaceId":""}
                                         ,{"ClientAddress":""}
                                         ,{"Port":0}]