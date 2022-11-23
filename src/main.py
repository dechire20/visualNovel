import pygame
import time
import KeyManager
import Handler
from states import StateMachine, PlayingState, HomeState, SettingsState
from sys import exit


class Game:
    def __init__(self):
        startTime = time.time()

        pygame.init()

        self.states = ["homeState", "playingState", "settingsState"]
        self.currentState = self.states[1]

        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.NOFRAME,
                                              display=0)
        pygame.display.set_caption("Visual novel")

        self.clock = pygame.time.Clock()

        self.keyManager = KeyManager.KeyManager()
        self.handler = Handler.Handler(self)

        self.stateMachine = StateMachine.StateMachine()

        # Load states
        self.homeState = HomeState.HomeState(self.handler)
        self.gameState = PlayingState.PlayingState(self.handler)
        self.settingsState = SettingsState.SettingsState(self.handler)

        # Add states
        self.stateMachine.add(self.states[0], self.homeState)
        self.stateMachine.add(self.states[1], self.gameState)
        self.stateMachine.add(self.states[2], self.settingsState)

        # Initial state
        self.stateMachine.change(self.states[0])

        print("----------------------------------")
        print(f"Execution Time: {time.time() - startTime}")
        print("----------------------------------")

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

            self.stateMachine.handleInput(event)

    def update(self):
        self.keyManager.update()
        self.stateMachine.update()

        if self.keyManager.one:
            self.currentState = self.stateMachine.change(self.states[0])
        elif self.keyManager.two:
            self.currentState = self.stateMachine.change(self.states[1])
        elif self.keyManager.three:
            self.currentState = self.stateMachine.change(self.states[2])

    def render(self):
        self.stateMachine.render()

    def getScreen(self):
        return self.screen

    def getScreenSize(self):
        return pygame.display.get_surface().get_size()

    def getKeyManager(self):
        return self.keyManager

    def getStateMachine(self):
        return self.stateMachine


game = Game()
game.run()
