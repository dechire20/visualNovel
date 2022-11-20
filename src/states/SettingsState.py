from states import IState
import pygame


class SettingsState(IState.IState):
    def __init__(self, handler):
        self.handler = handler

        # Settings background
        self.settingsBackground = pygame.image.load("../res/background/settings.jpeg")
        self.settingsBackground = pygame.transform.scale(self.settingsBackground, self.handler.getGameScreenSize())

    def update(self):
        pass

    def handleInput(self, event):
        pass

    def render(self):
        self.handler.getScreen().blit(self.settingsBackground, (0, 0))
