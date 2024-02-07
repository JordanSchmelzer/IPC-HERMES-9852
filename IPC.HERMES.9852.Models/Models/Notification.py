'''
The Notification message is sent by both machines before a connection is terminated, e.g. after protocol errors 
or before shutdown. It could also be used for general notification purposes.

The following NotificationCodes are defined: 
1 Protocol error (invalid transition in the corresponding state machine) 
2 Connection refused because of an established connection 
3 Connection reset because of changed configuration 
4 Configuration error 
5 Machine shutdown 
6 BoardForecast error 
 
Possible values for Severity: 
1 Fatal error 
2 Error 
3 Warning 
4 Info
'''

class Notification:
    def __init__(self):
        self.NotificationCode = ""
        self.Severity = 0
        self.Description = ""