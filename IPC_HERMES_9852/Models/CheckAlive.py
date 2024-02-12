'''
The CheckAlive message is used to detect connection losses. It therefore does not have to transport data and 
can be ignored by the receiver. Accordingly there is no response. 
However, if a machine supports the FeatureCheckAliveResponse, it must answer CheckAlive messages with 
Type  set  to  1  with  a  CheckAlive  message  with  Type  set  to  2  and  the  same  Id  as  the  received  CheckAlive 
message.

Type may be one of the following values: 
1 Ping: CheckAlive request. 
2 Pong:CheckAlive response. 
The  machine  sending  CheckAlive  message  with  Type  set  to  1  chooses  a  unique  for  Id  (e.g.  GUID  or  time 
stamp). The machine responding with CheckAlive message with Type set to 2 has to answer using the same 
Id. 
'''

class CheckAlive:
    def __init__(self):
        self.Type = 1
        self.Id = ""