import pygame

class KeyManager:

    keys = dict()
    
    one = two = three = four = False

    def __init__(self) -> None:
        for i in range(500):
            self.keys[i] = False
        
    def update(self):
        self.one = self.keys[pygame.K_1]
        self.two = self.keys[pygame.K_2]
        self.three = self.keys[pygame.K_3]
        self.four = self.keys[pygame.K_4]
    
    def keyInput(self, key: pygame.key, isPressed: bool):
        self.keys[key] = isPressed

    