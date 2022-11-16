import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.NOFRAME, display=0)
        pygame.display.set_caption("Visual novel")

        self.clock = pygame.time.Clock()
        self.screenSize = pygame.display.get_surface().get_size()
        
        # Text
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("Save", True, "Red")
        
        # Background
        self.background = pygame.image.load("res/background/rooftop.png")
        self.background = pygame.transform.scale(self.background, self.screenSize)

        # Dialogue box
        self.dialogueBox = pygame.Surface((1200, 300))
        self.dialogueBoxRect = self.dialogueBox.get_rect(midbottom = ((self.screenSize[0] / 2) , (self.screenSize[1] / 2) + 520))
        self.dialogueBox.fill("Blue")
    
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
    
    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))     
        self.screen.blit(self.dialogueBox, self.dialogueBoxRect)
        self.screen.blit(self.text, (500, 1055))


game = Game()
game.run()




    