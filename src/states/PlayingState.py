from states import IState
import json
import pygame


class PlayingState(IState.IState):
    def __init__(self, handler) -> None:
        self.handler = handler
        self.stateMachine = handler.getStateMachine()

        self.defaultFont = pygame.font.Font(None, 35)
        self.chalkFont = pygame.font.Font("../res/fonts/chawp.ttf", 30)

        # Buttons
        self.homeButton = self.defaultFont.render("Home", True, "Yellow")
        self.homeButtonRect = self.homeButton.get_rect(midbottom=(700, 1080))

        self.settingsButton = self.defaultFont.render("Settings", True, "Yellow")
        self.settingsButtonRect = self.settingsButton.get_rect(
            midbottom=(self.homeButtonRect.centerx + 300, self.homeButtonRect.top + 25))

        self.saveButton = self.defaultFont.render("Save", True, "Yellow")
        self.saveButtonRect = self.saveButton.get_rect(
            midbottom=(self.homeButtonRect.centerx + 600, self.homeButtonRect.top + 24))

        # Load all backgrounds
        self.sceneCount = 5
        self.currentScene = 0
        self.backgrounds = []
        for i in range(self.sceneCount):
            self.backgrounds.append(pygame.image.load(f"../res/game/background/{i}.png"))
            self.backgrounds[i] = pygame.transform.scale(self.backgrounds[i], self.handler.getGameScreenSize())

        # Dialogue box
        self.dialogueBox = pygame.image.load("../res/game/box.png")
        self.dialogueBox = pygame.transform.scale(self.dialogueBox, (2000, 800))
        self.dialogueBoxRect = self.dialogueBox.get_rect(
            midbottom=((self.handler.getGameScreenSize()[0] / 2), (self.handler.getGameScreenSize()[1] / 2) + 530))

        # Character
        self.character = pygame.image.load("../res/game/character/flusterlook_1.png")
        self.ext = self.character.get_rect()[2:4]
        size = 0.8
        self.character = pygame.transform.scale(self.character, (int(self.ext[0] * size), int(self.ext[1] * size)))

        #  Dialogue message
        file = open("../res/game/dialogues/dialogues.json")
        self.scenes = json.load(file)
        self.messages = self.scenes["scene1"]["messages"]
        self.activeMessage = 0
        self.message = self.messages[self.activeMessage]
        self.textSurface = self.chalkFont.render("", True, "White")
        self.counter = 0
        self.animationSpeed = 1
        self.animationDone = False

    def update(self):
        if self.counter < self.animationSpeed * len(self.message):
            self.counter += 1
        elif self.counter >= self.animationSpeed * len(self.message):
            self.animationDone = True

        self.textSurface = self.chalkFont.render(self.message[0:self.counter//self.animationSpeed], True, "White")

    def handleInput(self, event: pygame.event):
        mousePos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.homeButtonRect.collidepoint(mousePos):
                self.stateMachine.change("homeState")
            elif self.settingsButtonRect.collidepoint(mousePos):
                self.stateMachine.change("settingsState")
            elif self.saveButtonRect.collidepoint(mousePos):
                print("saved!")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.currentScene < self.sceneCount - 1:
                self.currentScene += 1
            elif event.key == pygame.K_LEFT and self.currentScene > 0:
                self.currentScene -= 1
            elif event.key == pygame.K_RETURN and self.activeMessage < len(self.messages) - 1:
                self.activeMessage += 1
                self.animationDone = False
                self.message = self.messages[self.activeMessage]
                self.counter = 0

    def render(self):
        self.handler.getScreen().blit(self.backgrounds[self.currentScene], (0, 0))
        self.handler.getScreen().blit(self.character, (200, -100))
        self.handler.getScreen().blit(self.dialogueBox, self.dialogueBoxRect)

        # Buttons
        self.handler.getScreen().blit(self.homeButton, self.homeButtonRect)
        self.handler.getScreen().blit(self.settingsButton, self.settingsButtonRect)
        self.handler.getScreen().blit(self.saveButton, self.saveButtonRect)

        # Dialogue text
        self.handler.getScreen().blit(self.textSurface, (600, 750))

