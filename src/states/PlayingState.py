from states import IState
import pygame

class PlayingState(IState.IState):
    def __init__(self, handler) -> None:
        super().__init__(handler)
        super().name = "john"

        self.defaultFont = pygame.font.Font(None, 40)
        self.chalkFont = pygame.font.Font("res/fonts/chawp.ttf", 60)

        # Buttons
        self.homeButton = self.defaultFont.render("Home", True, "Yellow")
        self.homeButtonRect = self.homeButton.get_rect(midbottom = (700, 1085))

        self.loadButton = self.defaultFont.render("Load", True, "Yellow")
        self.loadButtonRect = self.loadButton.get_rect(midbottom = (self.homeButtonRect.centerx + 200, self.homeButtonRect.top + 26))

        self.settingsButton = self.defaultFont.render("Settings", True, "Yellow")
        self.settingsButtonRect = self.settingsButton.get_rect(midbottom = (self.homeButtonRect.centerx + 400, self.homeButtonRect.top + 27))

        self.returnButton = self.defaultFont.render("Return", True, "Yellow")
        self.returnButtonRect = self.returnButton.get_rect(midbottom = (self.homeButtonRect.centerx + 600, self.homeButtonRect.top + 27))

        self.testMessage = self.chalkFont.render("Baka!!!!", True, "White")

        # Game background
        self.gameBackground = pygame.image.load("res/background/rooftop.png")
        #print(self.handler.getGameScreenSize())
        self.gameBackground = pygame.transform.scale(self.gameBackground, self.handler.getGameScreenSize())

        # Dialogue box
        self.dialogueBox = pygame.Surface((1200, 300))
        self.dialogueBoxRect = self.dialogueBox.get_rect(midbottom = ((self.screenSize[0] / 2) , (self.screenSize[1] / 2) + 520))
        self.dialogueBox.fill("Black")

        # Character
        self.character = pygame.image.load("res/character/flusterlook_1.png")
        self.ext = self.character.get_rect()[2:4]
        size = 0.8
        self.character = pygame.transform.scale(self.character, (int(self.ext[0] * size), int(self.ext[1] * size)))

    def update(self):
        self.handleInput()

    def handleInput(self):
        pass
    
    def render(self):
        self.handler.getScreen().blit(self.gameBackground, (0, 0))
        self.handler.getScreen().blit(self.character, (200, -100))
        self.handler.getScreen().blit(self.dialogueBox, self.dialogueBoxRect)
        self.handler.getScreen().blit(self.testMessage, (500, 800))