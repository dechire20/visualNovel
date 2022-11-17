import pygame
import helper
from sys import exit

class Game:
    def __init__(self):
        pygame.init()

        self.states = ["home", "game", "load", "settings", "return"]
        self.currentState = self.states[1]


        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.NOFRAME, display=0)
        pygame.display.set_caption("Visual novel")

        self.clock = pygame.time.Clock()
        self.screenSize = pygame.display.get_surface().get_size()
        
        # Text
        self.font = pygame.font.Font(None, 40)
        self.homeButton = self.font.render("Home", True, "Red")
        self.homeButtonRect = self.homeButton.get_rect(midbottom = (700, 1085))

        self.loadButton = self.font.render("Load", True, "Red")
        self.loadButtonRect = self.loadButton.get_rect(midbottom = (self.homeButtonRect.centerx + 200, self.homeButtonRect.top + 26))

        self.settingsButton = self.font.render("Settings", True, "Red")
        self.settingsButtonRect = self.settingsButton.get_rect(midbottom = (self.homeButtonRect.centerx + 400, self.homeButtonRect.top + 27))

        self.returnButton = self.font.render("Return", True, "Red")
        self.returnButtonRect = self.returnButton.get_rect(midbottom = (self.homeButtonRect.centerx + 600, self.homeButtonRect.top + 27))
        
        # Home screen
        self.home = pygame.image.load("res/background/home.jpg")
        self.home = pygame.transform.scale(self.home, self.screenSize)

        # Game background
        self.gameBackground = pygame.image.load("res/background/rooftop.png")
        self.gameBackground = pygame.transform.scale(self.gameBackground, self.screenSize)

        # Load background
        self.loadBackground = pygame.image.load("res/background/load.jpeg")
        self.loadBackground = pygame.transform.scale(self.loadBackground, self.screenSize)

        # Settings background
        self.settingsBackground = pygame.image.load("res/background/settings.jpeg")
        self.settingsBackground = pygame.transform.scale(self.settingsBackground, self.screenSize)

        # Dialogue box
        self.dialogueBox = pygame.Surface((1200, 300))
        self.dialogueBoxRect = self.dialogueBox.get_rect(midbottom = ((self.screenSize[0] / 2) , (self.screenSize[1] / 2) + 520))
        self.dialogueBox.fill("Blue")

        foobar = ""
        
    
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
                match event.key:
                    case pygame.K_1:
                        self.currentState = self.states[0]
                    case pygame.K_2:
                        self.currentState = self.states[1]
                    case pygame.K_3:
                        self.currentState = self.states[2]
                    case pygame.K_4:
                        self.currentState = self.states[3]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse pressed
                mouse_pos = pygame.mouse.get_pos()
                if self.homeButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[0]
                elif self.loadButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[2]
                elif self.settingsButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[3]
                elif self.returnButtonRect.collidepoint(mouse_pos):
                    self.currentState = self.states[4]

    
    def update(self):

        pass

    def render(self):
        match self.currentState:
            case "home":
                self.screen.blit(self.home, (0, 0))
            case "game":
                self.screen.blit(self.gameBackground, (0, 0))     
                self.screen.blit(self.dialogueBox, self.dialogueBoxRect)
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
            textSurface = self.font.render(text, True, "Black")
            textRect = textSurface.get_rect()
            textRect.center = (self.screenSize[0] / 2, self.screenSize[1] / 2)
            self.screen.blit(textSurface, textRect)
            pygame.time.wait(100)

game = Game()
game.run()




    