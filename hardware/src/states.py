import uasyncio as asyncio 

# *******************************************************************************
# Statemachine and abstract State classes
# *******************************************************************************
class StateMachine(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state = Wake()

    def emit(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the emit function.
        self.state = self.state.emit(event)

class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        print (str(self))

    def emit(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__

# *******************************************************************************
# Device state, conditions and state transitions
# *******************************************************************************
class Wake(State):
    """
    The state just after the device has booted 
    """
    def __init__(self):
        print (str(self))
        

    def emit(self, event):
  
        if event == 'deepsleepwake':
            return Ready()

        if event == 'resetwake':
            return Ready()

        if event == 'watchdogwake':
            return Ready()
    
        return self

class Ready(State):
    """
    The state in which the device is ready for an external event to take place
    """

    def emit(self, event):

        if event == 'handinserted':
            return Dispense()

        if event == 'fluidlow':
            return Fluidlow()


        return self

class Dispense(State):
    """
    The state in which the device will dispense a quantity of fluid
    """
    def __init__(self):
        print (str(self))
        from tasks import dispense 
        asyncio.get_event_loop().create_task( dispense() )
      
        
    def emit(self, event):

        if event == 'handremoved':
            return Ready()

        return self

class Fluidlow(State):
    """
    The state in which the device jas low fluid
    """
    def __init__(self):
        print (str(self))

    
    def emit(self, event):

        if event == 'fluidfull':
            return Ready()

        return self    

class Sleep(State):
    """
    The state puts the device in deep sleep
    """
    def __init__(self):
        print (str(self))
        #asyncio.get_event_loop().create_task( sleep() )

    def emit(self, event):
        return self