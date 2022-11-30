from states import IState
import json
import pygame


class PlayingState(IState.IState):
    def __init__(self, handler) -> None:
        self.handler = handler
        self.stateMachine = handler.getStateMachine()

        self.defaultFont = pygame.font.Font(None, 35)
        self.chalkFont = pygame.font.Font("../res/fonts/chawp.ttf", 25)

        # Buttons
        self.homeButton = self.defaultFont.render("Home", True, "Yellow")
        self.homeButtonRect = self.homeButton.get_rect(midbottom=((self.handler.getGameScreenSize()[0] / 2) , (self.handler.getGameScreenSize()[1] / 2) + 540))

        # Load all backgrounds
        self.currentScene = 0
        self.backgrounds = []
        self.backgroundNames = ["ammusmentPark", "booths", "magicShow", "foodstall", "photoBooth", "darts", "dartsGame"]
        for i in range(len(self.backgroundNames)):
            self.backgrounds.append(pygame.image.load(f"../res/game/background/{i}.png"))
            self.backgrounds[i] = pygame.transform.scale(self.backgrounds[i], self.handler.getGameScreenSize())

        self.boxTemplate = pygame.image.load("../res/game/box.png")

        # Dialogue box
        self.dialogueBox = pygame.transform.scale(self.boxTemplate, (2000, 800))
        self.dialogueBoxRect = self.dialogueBox.get_rect(
            midbottom=((self.handler.getGameScreenSize()[0] / 2), (self.handler.getGameScreenSize()[1] / 2) + 530))

        # Choices box
        self.choicesText = self.chalkFont.render("AKHSFDKAHFJADSFasjflasfjklsadjflasjkflsdjlfasklfjadsfasdfjsakfsjlfasdklfjasdjfklasjfkaslfjaslkfjalsjfkadlsf", True, "White")
        self.choicesBoxRect = self.choicesText.get_rect(midbottom=((self.handler.getGameScreenSize()[0] / 2), (self.handler.getGameScreenSize()[1] / 2) - 100))
        self.isInChoices = False
        self.arrChoice = []
        self.currentChoice = 0

        # Character
        self.expressions = []
        self.expressionsName = ["blush", "blushSmile", "sad", "pointSmile", "smile0", "smile1", "curious"]
        size = 0.8
        for i in range(len(self.expressionsName)):
            self.expressions.append(pygame.image.load(f"../res/game/character/{i}.png"))
            self.ext = self.expressions[i].get_rect()[2:4]
            self.expressions[i] = pygame.transform.scale(self.expressions[i], (int(self.ext[0] * size), int(self.ext[1] * size)))
        self.characterPos = self.expressions[i].get_rect(midbottom=(self.handler.getGameScreenSize()[0] / 2, (self.handler.getGameScreenSize()[1] / 2) + 450))
        self.currentExpression = ""

        #  Dialogue message
        file = open("../res/game/dialogues/dialogues.json")
        self.scenes = json.load(file)
        self.dialogues = self.scenes["scene0"]["dialogues"]

        self.textDisplayed = ""

        # Dialogue animation
        self.activeDialogueIndex = 0
        self.dialogue = self.dialogues[self.activeDialogueIndex]
        self.textSurface = self.chalkFont.render("", True, "White")
        self.counter = 0
        self.animationSpeed = 1
        self.animationDone = False

        # Dialogue speaker
        self.speaker = self.dialogue["name"]
        self.speakerName = self.chalkFont.render("", True, "White")
        self.speakerNameRect = self.speakerName.get_rect(midbottom=((self.handler.getGameScreenSize()[0] / 2) - 300, (self.handler.getGameScreenSize()[1] / 2) + 230))

        # Screen filter
        self.darkFilter = pygame.Surface(self.handler.getGameScreenSize())
        self.darkFilter.fill("black")
        self.darkFilter.set_alpha(160)

        # Button released
        self.isMouseReleased = True

    def update(self):
        if self.dialogue["name"] == "you":
            if self.dialogue["type"] == "question":
                self.isInChoices = True
        else:
            self.speaker = self.dialogue["name"]

        self.speaker = self.dialogue["name"]

        self.speakerName = self.chalkFont.render(self.speaker, True, "White")

        self.currentScene = self.backgroundNames.index(self.dialogue["background"])

        self.updateTextScroll()

    def handleInput(self, event: pygame.event):
        mousePos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.isInChoices:
                if self.homeButtonRect.collidepoint(mousePos):
                    pygame.mixer.music.load("../res/home/music/door.ogg")
                    pygame.mixer.music.play(-1)
                    self.stateMachine.change("homeState")
            else:
                for i in range(len(self.arrChoice)):
                    if self.arrChoice[i].collidepoint(mousePos) and self.isMouseReleased:
                        if "ending" in self.dialogue["responses"][i]:
                            self.dialogues = self.scenes[self.dialogue["responses"][i]]["dialogues"]
                            self.activeDialogueIndex = 0
                            self.nextDialogue()
                            response = {
                                'name': 'isla',
                                'expression': self.dialogue["expression"],
                                'background': self.dialogue["background"],
                                'dialogue': self.dialogue["dialogue"]
                            }
                        else:
                            response = {
                                'name': 'isla',
                                'expression': self.dialogue["expressions"][i],
                                'background': self.dialogue["background"],
                                'dialogue': self.dialogue["responses"][i]
                            }
                        self.dialogue = json.loads(json.dumps(response))
                        self.isMouseReleased = False
                        self.isInChoices = False
        elif event.type == pygame.MOUSEBUTTONUP:
            self.isMouseReleased = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.activeDialogueIndex < len(self.dialogues) - 1 and not self.isInChoices:
                self.activeDialogueIndex += 1
                self.nextDialogue()
            elif event.key == pygame.K_r:
                self.reset()

    def render(self):
        self.handler.getScreen().blit(self.backgrounds[self.currentScene], (0, 0))
        if not self.dialogue["expression"] == "none":
            self.handler.getScreen().blit(self.expressions[self.expressionsName.index(self.dialogue["expression"])], self.characterPos)
        self.handler.getScreen().blit(self.dialogueBox, self.dialogueBoxRect)

        # Buttons
        self.handler.getScreen().blit(self.homeButton, self.homeButtonRect)

        # Dialogue text
        dialogueTextPos = ((self.handler.getGameScreenSize()[0] / 2) - 400, (self.handler.getGameScreenSize()[1] / 2) + 270)
        self.displayMultiLinedText(self.textDisplayed, dialogueTextPos, self.chalkFont, "white")
        self.handler.getScreen().blit(self.speakerName, self.speakerNameRect)

        # Choices box

        if self.isInChoices:
            self.displayChoices(self.dialogue["choices"])

    def reset(self):
        self.currentScene = 0
        self.activeDialogueIndex = 0
        self.dialogue = self.dialogues[self.activeDialogueIndex]
        self.counter = 0

    def updateTextScroll(self):

        if self.counter < self.animationSpeed * len(self.dialogue["dialogue"]):
            self.counter += 1
        elif self.counter >= self.animationSpeed * len(self.dialogue["dialogue"]):
            self.animationDone = True

        self.textDisplayed = self.dialogue["dialogue"][0:self.counter//self.animationSpeed]

    def displayMultiLinedText(self, text, pos, font, color):
        collection = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        x,y = pos
        for lines in collection:
            for words in lines:
                wordSurface = font.render(words, True, color)
                wordWidth, wordHeight = wordSurface.get_size()

                if x + wordWidth >= 1450 or words == "\n":
                    x = pos[0]
                    y += wordHeight
                self.handler.getScreen().blit(wordSurface, (x,y))
                x += wordWidth + space

            x = pos[0]
            y += wordHeight

    def displayChoices(self, choices):
        spaceSize = -100
        self.arrChoice = []
        self.handler.getScreen().blit(self.darkFilter, (0, 0))
        for choice in choices:
            text = self.chalkFont.render(choice, True, "White")
            textPos = text.get_rect(midbottom=(self.choicesBoxRect.midbottom[0], self.choicesBoxRect.midbottom[1] + spaceSize))
            self.arrChoice.append(textPos)
            self.handler.getScreen().blit(text, textPos)
            spaceSize += 100

    def nextDialogue(self):
        self.animationDone = False
        self.dialogue = self.dialogues[self.activeDialogueIndex]
        self.counter = 0






