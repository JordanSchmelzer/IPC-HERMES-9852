'''State class: Base State class'''
class State:
    
    """Base state. This is to share functionality"""
    def switch(self):
        """Switch between conveyor belt on and off on DEK machine """
        pass
    
class ConveyorRunningState(State):
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt
        
    def switch(self):
        print("Stopping the conveyor belt...")
        self.conveyor_belt.state = self.conveyor_belt.stopped_state
            
class ConveyorStoppedState(State):
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt
        
    def switch(self):
        print("Starting the conveyor belt...")
        self.conveyor_belt.state = self.conveyor_belt.running_state
        
class ConveyorBelt:
    def __init__(self):
        self.running_state = ConveyorRunningState(self)
        self.stopped_state = ConveyorStoppedState(self)
        self.state = self.stopped_state
        
    def switch(self):
        self.state.switch()
        
conveyor_belt = ConveyorBelt()

conveyor_belt.switch()
conveyor_belt.switch()