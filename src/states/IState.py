
class IState:
    def __init__(self, handler) -> None:
        self.name = handler
        pass

    def update(self):
        pass

    def handleInput(self, event):
        pass

    def render(self):
        pass
