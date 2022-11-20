
class State:

    currentState = None
    #handler = None

    def __init__(self, handler) -> None:
        self.handler = handler
        self.name = str()

    def setState(self, state):
        self.currentState = state
    
    def getState(self):
        print(self.name)
        return self.currentState

    def update(self):
        pass
    def handleInput(self):
        pass
    def render(self):
        pass
    