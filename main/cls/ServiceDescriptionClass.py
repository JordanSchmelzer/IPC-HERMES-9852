class ServiceDescription:
    __slots__ = ("lane_id"
                 ,"interface_id"
                 ,"class_str"
                 ,"class_int"
                 )
    
    def __init__(self, data: dict):
        self.lane_id = data["lane_id"]
        self.interface_id = data["interface_id"]

        
    def class_method(self, arg):
        print(arg)
        
x1 = ServiceDescription()
print(x1.class_int)