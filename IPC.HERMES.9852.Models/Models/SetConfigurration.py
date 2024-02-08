'''
The  SetConfiguration  message  is  sent  by  an  engineering  station  to  configure  the  Hermes  interfaces  of  a 
machine. If the sent configuration is not accepted, the machine is expected to send a Notification message 
(see section 3.5). 
 
Note: The function of SetConfiguration is optional on the vertical channel. If FeatureConfiguration is specified 
in the SupervisoryServiceDescription, it must be fully supported. Otherwise it can be ignored. 
'''

class SetConfigurration:
    def __init__(self):
        self.MachineId = ""
        self.SupervisorySystemPort = 0
        self.UpstreamConfigurations = [{"UpstreamLaneId":1}
                                       
                                       ]
        self.DownstreamConfigurations = []