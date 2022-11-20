from states import IState
import pygame


class HomeState(IState.IState):
    def __init__(self, handler) -> None:
        self.handler = handler

        # Home screen
        self.home = pygame.image.load("../res/background/home.jpg")
        self.home = pygame.transform.scale(self.home, self.handler.getGameScreenSize())

    def update(self):
        pass

    def handleInput(self, event):
        pass

    def render(self):
        self.handler.getScreen().blit(self.home, (0, 0))
