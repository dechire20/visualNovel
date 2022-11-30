from states import IState
import pygame


class HomeState(IState.IState):
    def __init__(self, handler) -> None:
        self.handler = handler
        self.hasSaved = False

        self.defaultFont = pygame.font.Font(None, 40)
        self.chalkFont = pygame.font.Font("../res/fonts/chawp.ttf", 60)

        # Home screen
        self.home = pygame.image.load("../res/background/home.jpg")
        self.home = pygame.transform.scale(self.home, self.handler.getGameScreenSize())
        
        # Buttons
        self.continueButton = self.chalkFont.render("Continue", True, "White")
        self.continueButtonRect = self.continueButton.get_rect(midbottom=(handler.getGameScreenSize()[0] / 2, handler.getGameScreenSize()[1] / 2))

        self.newGameButton = self.chalkFont.render("New Game", True, "White")
        self.newGameButtonRect = self.newGameButton.get_rect(midbottom=(handler.getGameScreenSize()[0] / 2, (handler.getGameScreenSize()[1] / 2) + 80))

        self.settingsButton = self.chalkFont.render("Settings", True, "White")
        self.settingsButtonRect = self.settingsButton.get_rect(midbottom=(handler.getGameScreenSize()[0] / 2, (handler.getGameScreenSize()[1] / 2 + 160)))

        # Sound
        self.clickSound = pygame.mixer.Sound("../res/soundEffects/click_002.ogg")

        # Music
        pygame.mixer.music.load("../res/home/music/door.ogg")
        self.isMusicOn = False

        pygame.mixer.music.play(-1)
        self.hasNewGame = False

    def update(self):
        if not self.isMusicOn:
            pygame.mixer.music.play()
            self.isMusicOn = True

    def handleInput(self, event):
        mousePos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.newGameButtonRect.collidepoint(mousePos):
                pygame.mixer.music.fadeout(500)
                pygame.mixer.Sound.play(self.clickSound)
                self.handler.getStateMachine().change("playingState")
                self.handler.gameReset()
                self.hasNewGame = True
            elif self.continueButtonRect.collidepoint(mousePos) and not self.hasSaved and self.hasNewGame:
                pygame.mixer.music.fadeout(500)
                pygame.mixer.Sound.play(self.clickSound)
                self.handler.getStateMachine().change("playingState")
            elif self.settingsButtonRect.collidepoint(mousePos):
                pygame.mixer.music.fadeout(500)
                pygame.mixer.Sound.play(self.clickSound)
                self.handler.getStateMachine().change("settingsState")

    def render(self):
        self.handler.getScreen().blit(self.home, (0, 0))
        if not self.hasSaved:
            self.handler.getScreen().blit(self.continueButton, self.continueButtonRect)
        self.handler.getScreen().blit(self.newGameButton, self.newGameButtonRect)
        self.handler.getScreen().blit(self.settingsButton, self.settingsButtonRect)

