

class Handler:
    
    def __init__(self, game) -> None:
        self.game = game

    def getKeyManager(self):
        return self.game.getKeyManager()

    def getGameScreenSize(self):
        return self.game.getScreenSize()
    
    def getScreen(self):
        return self.game.getScreen()

    def getStateMachine(self):
        return self.game.getStateMachine()

    def gameReset(self):
        return self.game.gameReset()


