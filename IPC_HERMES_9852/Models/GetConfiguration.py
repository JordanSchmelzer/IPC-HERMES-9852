'''
The CurrentConfiguration message is sent by a machine in response to the GetConfiguration message.

For the definition of UpstreamConfiguration and DownstreamConfiguration see section 3.19. 
If  no  MachineId  has  been  configured  yet,  the  CurrentConfiguration  message  does  not  contain  the  attribute 
MachineId.
'''

class GetConfiguration:
    def __init__(self):
        self.MachineId = ""
        self.SupervisorySystemPort = 65535
        self.UpstreamConfigurations = []
        self.DownstreamConfigurations = []