'''
The ServiceDescription message is sent by both machines after a connection is established. The downstream 
machine  sends  its  ServiceDescription  first  whereupon  the  upstream  machine  answers  by  sending  its  own 
ServiceDescription. 

The features specified in version 1.0 of this protocol have to be provided by any implementation and thus are 
not listed in the SupportedFeatures list of the ServiceDescription explicitly. The same applies for all mandatory 
features of the version specified in the Version attribute. All optional features or additional features of an higher 
version supported by a machine need to be listed in the SupportedFeatures list to indicate there availability.
'''

class ServiceDescription:
    def __init__(self):    
        self.MachineId = ""
        self.LaneId = 0
        self.InterfaceId = ""
        self.Version = ""
        self.SupportedFeatures = {
            "FeatureCheckAliveResponse": 1
            ,"FeatureBoardForecast":1
            ,"FeatureQueryBoardInfo":1
            ,"FeatureSendBoardInfo":1
        }
    