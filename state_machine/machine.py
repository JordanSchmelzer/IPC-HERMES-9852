# Define the State Interface to encapsulate behavior with a particular Context state
class ConveyorState:
    def set_conveyor(self) -> None:
        ...

    def stop_conveyor(self) -> None:
        ...

# Create Concrete State Classes that use the State Interface
class ConveyorRunningState(ConveyorState):
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt

    def set_conveyor(self):
        print("Stopping the conveyor belt...")
        self.conveyor_belt.state = self.conveyor_belt.stopped_state
        
    def stop_conveyor(self):
        print("Stopping the conveyor belt...")
        self.conveyor_belt.state = self.conveyor_belt.stopped_state
        
class ConveyorStoppedState(ConveyorState):
    def __init__(self, conveyor_belt):
        self.conveyor_belt = conveyor_belt

    def set_conveyor(self):
        print("Starting the conveyor belt...")
        self.conveyor_belt.state = self.conveyor_belt.running_state
    
    def stop_conveyor(self):
        print("Stopping the conveyor belt...")

# Create the Context Class, is the interface to clients.
class ConveyorBelt: 
    def __init__(self):
        self.running_state = ConveyorRunningState(self)
        self.stopped_state = ConveyorStoppedState(self)
        self.state = self.stopped_state
        
    def set_conveyor(self):
        self.state.set_conveyor()
        
    def stop_conveyor(self):
        self.state.stop_conveyor()

if __name__ == "__main__":
    conveyor_belt = ConveyorBelt()
    conveyor_belt.set_conveyor()
    conveyor_belt.set_conveyor()
    conveyor_belt.stop_conveyor()