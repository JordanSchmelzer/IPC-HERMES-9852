'''
The SupervisoryServiceDescription  message  is  sent  by  both  machine  and  supervisory  system  after  a 
connection is established. The supervisory system sends its SupervisoryServiceDescription first whereupon 
the machine answers by sending its own SupervisoryServiceDescription.
'''

class SupervisoryServiceDescription:
    def __init__(self):
        self.SystemId= ""
        self.Version = ""
        self.SupportedFeatures = [
             {"FeatureConfiguration":1}
            ,{"FeatureCheckAliveResponse":1}
            ,{"FeatureBoardTracking":1}
            ,{"FeatureQueryWorkOrderInfo":1}
            ,{"FeatureSendWorkOrderInfo":1}
        ]