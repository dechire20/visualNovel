

class Helper:
    def displayTextAnimation(self, surface, pygame, string: str, font):
        screenSize = pygame.screensize                
        text = ''
        for i in range(len(string)):
            surface.fill("White")
            text += string[i]
            text_surface = font.render(text, True, "Black")
            text_rect = text_surface.get_rect()
            text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
            surface.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(100)
