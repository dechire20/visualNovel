import pygame
import time
import KeyManager
from sys import exit

class Game:
    keyManager = None
    handler = None
    screen = pygame.surface
    #screenSize = None
    def __init__(self):
        startTime = time.time()


        pygame.init()


        self.states = ["home", "game", "load", "settings", "return"]
        self.currentState = self.states[1]


        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.NOFRAME, display=0)
        pygame.display.set_caption("Visual novel")

        self.clock = pygame.time.Clock()
        self.screenSize = pygame.display.get_surface().get_size()
        #print(self.screenSize)
        self.screen
        # Font
        self.defaultFont = pygame.font.Font(None, 40)
        self.chalkFont = pygame.font.Font("../res/fonts/chawp.ttf", 60)

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


        # Home screen
        self.home = pygame.image.load("../res/background/home.jpg")
        self.home = pygame.transform.scale(self.home, self.screenSize)

        # Game background
        self.gameBackground = pygame.image.load("../res/game/background/2.png")
        self.gameBackground = pygame.transform.scale(self.gameBackground, self.screenSize)

        # Load background
        self.loadBackground = pygame.image.load("../res/background/load.jpeg")
        self.loadBackground = pygame.transform.scale(self.loadBackground, self.screenSize)

        # Settings background
        self.settingsBackground = pygame.image.load("../res/background/settings.jpeg")
        self.settingsBackground = pygame.transform.scale(self.settingsBackground, self.screenSize)

        # Dialogue box
        self.dialogueBox = pygame.Surface((1200, 300))
        self.dialogueBoxRect = self.dialogueBox.get_rect(midbottom = ((self.screenSize[0] / 2) , (self.screenSize[1] / 2) + 520))
        self.dialogueBox.fill("Black")

        # Character
        self.character = pygame.image.load("../res/game/character/flusterlook_1.png")
        self.ext = self.character.get_rect()[2:4]
        size = 0.8
        self.character = pygame.transform.scale(self.character, (int(self.ext[0] * size), int(self.ext[1] * size)))
        #self.characterRect = self.character.get_rect(midbottom = (self.screenSize[0] / 2, self.screenSize[1] / 2))

        self.keyManager = KeyManager.KeyManager()
        self.handler = Handler(self)
        self.tester = Tester(self.handler)
        self.tester.fard()
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
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Keyboard pressed
                self.keyManager.keyInput(event.key, True)

            elif event.type == pygame.KEYUP:
                self.keyManager.keyInput(event.key, False)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse pressed
                if self.homeButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[0]
                elif self.loadButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[2]
                elif self.settingsButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[3]
                elif self.returnButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[4]
            elif self.homeButtonRect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif pygame.mouse.get_cursor != pygame.SYSTEM_CURSOR_ARROW:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self):
        self.keyManager.update()

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
                self.screen.blit(self.gameBackground, (0, 0))
                self.screen.blit(self.character, (200, -100))
                self.screen.blit(self.dialogueBox, self.dialogueBoxRect)
                self.screen.blit(self.testMessage, (500, 800))
            case "load":
                self.screen.blit(self.loadBackground, (0, 0))
            case "settings":
                self.screen.blit(self.settingsBackground, (0, 0))
            case "return":
                self.currentState = "game"
        self.screen.blit(self.homeButton, self.homeButtonRect)
        self.screen.blit(self.loadButton, self.loadButtonRect)
        self.screen.blit(self.settingsButton, self.settingsButtonRect)
        self.screen.blit(self.returnButton, self.returnButtonRect)

    def displayTextAnimation(self, string):
        text = ""
        for i in range(len(string)):
            text += string[i]
            textSurface = self.defaultFont.render(text, True, "Black")
            textRect = textSurface.get_rect()
            textRect.center = (self.screenSize[0] / 2, self.screenSize[1] / 2)
            self.screen.blit(textSurface, textRect)
            pygame.time.wait(100)

    def getScreen(self):
        return self.screen
    def getScreenSize(self):
        print(self.screenSize)
        return self.screenSize
    def getKeyManager(self):
        return self.keyManager

class Handler:
    def __init__(self, game) -> None:
        self.game = game

    def getKeyManager(self):
        return self.game.getKeyManager()

    def getGameScreenSize(self):
        return self.game.getScreenSize()

    def getScreen(self):
        return self.game.getScreen()

class Tester:
    def __init__(self, handler: Handler) -> None:
        self.handler = handler

    def fard(self):
        print(self.handler.getGameScreenSize())


game = Game()
game.run()