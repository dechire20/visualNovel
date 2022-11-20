import pygame
import time
import KeyManager
import Handler
from states import StateMachine, PlayingState
from sys import exit


class Game:
    keyManager = None
    handler = None
    screen = pygame.surface

    # screenSize = None
    def __init__(self):
        startTime = time.time()

        pygame.init()

        self.states = ["home", "game", "load", "settings", "return"]
        self.currentState = self.states[1]

        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.NOFRAME,
                                              display=0)
        pygame.display.set_caption("Visual novel")

        self.clock = pygame.time.Clock()
        self.screenSize = pygame.display.get_surface().get_size()

        # Home screen
        self.home = pygame.image.load("../res/background/home.jpg")
        self.home = pygame.transform.scale(self.home, self.screenSize)

        # Load background
        self.loadBackground = pygame.image.load("../res/background/load.jpeg")
        self.loadBackground = pygame.transform.scale(self.loadBackground, self.screenSize)

        # Settings background
        self.settingsBackground = pygame.image.load("../res/background/settings.jpeg")
        self.settingsBackground = pygame.transform.scale(self.settingsBackground, self.screenSize)

        self.keyManager = KeyManager.KeyManager()
        self.handler = Handler.Handler(self)

        self.stateMachine = StateMachine.StateMachine()
        self.gameState = PlayingState.PlayingState(self.handler)
        self.stateMachine.add("playingState", self.gameState)
        self.stateMachine.change("playingState")

        print("--------------------------")
        print(f"Execution Time: {time.time() - startTime}")
        print("--------------------------")

    def run(self):
        while True:
            game.processEvents()
            game.update()
            game.render()

            pygame.display.update()
            game.clock.tick(60)

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Keyboard pressed
                self.keyManager.keyInput(event.key, True)

            elif event.type == pygame.KEYUP:
                self.keyManager.keyInput(event.key, False)

            self.stateMachine.handleInput(event.type)

    def update(self):
        self.keyManager.update()
        self.stateMachine.update()

        if self.keyManager.one:
            self.currentState = self.states[0]
        elif self.keyManager.two:
            self.currentState = self.states[1]
        elif self.keyManager.three:
            self.currentState = self.states[2]
        elif self.keyManager.four:
            self.currentState = self.states[3]

    def render(self):
        match self.currentState:
            case "home":
                self.screen.blit(self.home, (0, 0))
            case "game":
                self.stateMachine.render()
            case "load":
                self.screen.blit(self.loadBackground, (0, 0))
            case "settings":
                self.screen.blit(self.settingsBackground, (0, 0))
            case "return":
                self.currentState = "game"

    def getScreen(self):
        return self.screen

    def getScreenSize(self):
        return self.screenSize

    def getKeyManager(self):
        return self.keyManager


game = Game()
game.run()
