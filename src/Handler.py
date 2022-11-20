#import main

class Handler:

    
    def __init__(self, game) -> None:
        self.game = game

    def getKeyManager(self):
        return self.game.getKeyManager()

    def getGameScreenSize(self):
        print(self.game.getScreenSize())
        return self.game.getScreenSize()
    
    def getScreen(self):
        return self.game.getScreen()


