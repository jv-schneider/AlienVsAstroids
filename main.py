import pygame
from pygame import display
from pygame import image
from pygame.display import update
import os
import random
import time

message = ""
size = 50
textX = 0
textY = 0
pygame.init()

# Spiel Daten
WINDOWWIDTH = 1750
WINDOWHEIGHT = 900
FPS = 60
ALIEN_RAUMSCHIFF_WIDTH = 190
ALIEN_RAUMSCHIFF_HEIGHT = 110
SPEED = 4
ASTERIOD_SPEED = 10
MAX_ASTROIDS_ONSCREEN = 3
ITEM_WIDTH = 50
ITEM_HEIGHT = 50

WINDOW = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Alien VS Asteroids")

# change path
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

except:
    print("Folder not found! For help please type \"h\" or click the question mark symbol in the menue")

try:
    ALIEN_RAUMSCHIFF = pygame.image.load("assets/AlienRaumschiff.png")
    ALIEN_RAUMSCHIFF = pygame.transform.scale(
        ALIEN_RAUMSCHIFF, (ALIEN_RAUMSCHIFF_WIDTH, ALIEN_RAUMSCHIFF_HEIGHT))
except:
    print("Alien image not found!")
    ALIEN_RAUMSCHIFF = pygame.Surface((10, 10))
    ALIEN_RAUMSCHIFF = pygame.transform.scale(
        ALIEN_RAUMSCHIFF, (ALIEN_RAUMSCHIFF_WIDTH, ALIEN_RAUMSCHIFF_HEIGHT))

    ALIEN_RAUMSCHIFF.fill((0, 200, 255))
try:
    ASTEROID1 = pygame.image.load("assets/Asterioid1.png")
    ASTEROID2 = pygame.image.load("assets/Asterioid2.png")
    ASTEROID3 = pygame.image.load("assets/Asterioid3.png")
    ASTEROID4 = pygame.image.load("assets/Asterioid4.png")
except:
    print("Asteroid image not found!")
    ASTEROID1 = pygame.Surface((10, 10))
    ASTEROID1 = pygame.transform.scale(
        ASTEROID1, (300, 150))
    ASTEROID2 = pygame.Surface((10, 10))
    ASTEROID2 = pygame.transform.scale(
        ASTEROID2, (300, 150))
    ASTEROID3 = pygame.Surface((10, 10))
    ASTEROID3 = pygame.transform.scale(
        ASTEROID3, (300, 150))
    ASTEROID4 = pygame.Surface((10, 10))
    ASTEROID4 = pygame.transform.scale(
        ASTEROID4, (300, 150))

    ASTEROID1.fill((255, 0, 0))
    ASTEROID2.fill((255, 0, 0))
    ASTEROID3.fill((255, 0, 0))
    ASTEROID4.fill((255, 0, 0))
try:
    SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(
        "assets/SpaceBackground.png"), (WINDOWWIDTH, WINDOWHEIGHT))

    BLURED_SPACE_BACKGROUND = pygame.image.load(
        "assets/StartMenueSpaceBackground.png")
    BLURED_SPACE_BACKGROUND = pygame.transform.scale(
        BLURED_SPACE_BACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))
    
except:
    print("Background image not found!")
    SPACE_BACKGROUND = pygame.Surface((10, 10))
    SPACE_BACKGROUND = pygame.transform.scale(
        SPACE_BACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))

    BLURED_SPACE_BACKGROUND = pygame.Surface((10, 10))
    BLURED_SPACE_BACKGROUND = pygame.transform.scale(
        BLURED_SPACE_BACKGROUND, (WINDOWWIDTH, WINDOWHEIGHT))

try:
    TELEPORT_ITEM = pygame.image.load(
        "assets/TeleportItem.png")
    TELEPORT_ITEM = pygame.transform.scale(
        TELEPORT_ITEM, (ITEM_WIDTH, ITEM_HEIGHT))
    HEART_ITEM = pygame.image.load(
        "assets/HeartItem.png")
    HEART_ITEM = pygame.transform.scale(
        HEART_ITEM, (ITEM_WIDTH, ITEM_HEIGHT))
except:
    print("Item image not found!")
    TELEPORT_ITEM = pygame.Surface((10, 10))
    TELEPORT_ITEM = pygame.transform.scale(
        TELEPORT_ITEM, (ITEM_WIDTH, ITEM_HEIGHT))

    HEART_ITEM = pygame.Surface((10, 10))
    HEART_ITEM = pygame.transform.scale(
        HEART_ITEM, (ITEM_WIDTH, ITEM_HEIGHT))

    TELEPORT_ITEM.fill((0, 0, 255))
    HEART_ITEM.fill((0, 0, 255))
try:
    gameOverImageError = False
    GAMEOVER = pygame.image.load(
        "assets/GameOverScreen.png")
    LOGO = pygame.image.load(
        "assets/Logo.png")
    PLAY_BUTTON = pygame.image.load(
        "assets/PlayButton.png")
    AKTIVE_PLAY_BUTTON = pygame.image.load(
        "assets/AktivePlayButton.png")
    STATS_BUTTON = pygame.image.load(
        "assets/StatsButton.png")
    AKTIVE_STATS_BUTTON = pygame.image.load(
        "assets/AktiveStatsButton.png")
    HELP_BUTTON = pygame.image.load(
        "assets/HelpButton.png")
    EXIT_BUTTON = pygame.image.load(
        "assets/ExitButton.png")
    EXIT_BUTTON = pygame.transform.scale(
        EXIT_BUTTON, (115, 115))
    AKTIVE_EXIT_BUTTON = pygame.image.load(
        "assets/AktiveExitButton.png")
    AKTIVE_EXIT_BUTTON = pygame.transform.scale(
        AKTIVE_EXIT_BUTTON, (115, 115)) 
except:
    print("Button image not found!")
    gameOverImageError = True
    GAMEOVER = pygame.Surface((10, 10))
    GAMEOVER = pygame.transform.scale(
        GAMEOVER, (WINDOWWIDTH, WINDOWHEIGHT))
    
    LOGO = pygame.Surface((10, 10))
    PLAY_BUTTON = pygame.Surface((10, 10))
    PLAY_BUTTON = pygame.transform.scale(
        PLAY_BUTTON, (607, 129))
    AKTIVE_PLAY_BUTTON = PLAY_BUTTON
    STATS_BUTTON = pygame.Surface((10, 10))
    STATS_BUTTON = pygame.transform.scale(
        STATS_BUTTON, (607, 129))
    AKTIVE_STATS_BUTTON = STATS_BUTTON
    HELP_BUTTON = pygame.Surface((10, 10))
    HELP_BUTTON = pygame.transform.scale(
        HELP_BUTTON, (607, 129))
    EXIT_BUTTON = pygame.Surface((129, 129))
    AKTIVE_EXIT_BUTTON = pygame.Surface((129, 129))

    PLAY_BUTTON.fill((255, 255, 255))
    STATS_BUTTON.fill((255, 255, 255))
    HELP_BUTTON.fill((255, 255, 255))


# Variablen

clock = pygame.time.Clock()

alien = pygame.Rect(
        WINDOWWIDTH/2, WINDOWHEIGHT/2, ALIEN_RAUMSCHIFF_WIDTH, ALIEN_RAUMSCHIFF_HEIGHT)
    
teleportsLeft = 1
lives = 1
score = 0
roundsSurvived = 0
asteroids = 1
asteroidsAbstand = 100
highScore = 0
highScoreTextColour = (255, 255, 255)
averageScore = 0
gamesPlayed = 0
gesammtScore = 0
mausPos = pygame.mouse.get_pos()

# Funktionen

def drawAlien(alien):
    WINDOW.blit(SPACE_BACKGROUND, (0, 0))
    WINDOW.blit(ALIEN_RAUMSCHIFF, (alien.x, alien.y))

def movement(alien, keysPressed):
    if keysPressed[pygame.K_w] and alien.y - SPEED > 0: # Oben
        alien.y -= SPEED
    if keysPressed[pygame.K_a] and alien.x - SPEED > 0: # Links
        alien.x -= SPEED
    if keysPressed[pygame.K_s] and alien.y + SPEED < WINDOWHEIGHT - 110: # Unten
        alien.y += SPEED + 0.25
    if keysPressed[pygame.K_d] and alien.x + SPEED < WINDOWWIDTH - 160: # Rechts
        alien.x += SPEED + 0.25

def teleport(alien, mausPos):
    global teleportsLeft
    if teleportsLeft > 0:
        alien.center = mausPos
        teleportsLeft -= 1


def showText():
    font = pygame.font.Font(None, size)
    textSurface = font.render(str(message), True, (255, 255, 255))
    textRect = textSurface.get_rect()
    textRect.center = (textX, textY)
    WINDOW.blit(textSurface, textRect)

def writeHighscore():
    datei = "AlienGameHighScore.txt"

    if os.path.isfile(datei):
        os.remove(datei)

    try:
        datei = open("AlienGameHighScore.txt", "w")
        datei.write(str(score))

    except FileNotFoundError:
        print("File not found!")
    finally:
        datei.close()

def setHighscore():
    global highScore

    try:
        datei = open("AlienGameHighScore.txt", "r")
        highScore = datei.read()

    except:
        print("AlienHighScoreFile not found!")
    finally:
        datei.close()

def showHighScore(x, y, colour):
    font = pygame.font.Font(None, 120)
    textSurface = font.render(str(highScore), True, colour)
    textRect = textSurface.get_rect()
    textRect.center = (x, y)
    WINDOW.blit(textSurface, textRect)

def handleStats():
    """
    Please dont consider this function its painful...
    """
    global gamesPlayed
    global averageScore

    datei1 = open("AlienStatsGamesPlayed.txt", "a+")
    datei1.close()

    datei1 = open("AlienStatsGamesPlayed.txt", "r+")
    datei1.write("1\n")
    for line in datei1:
        gamesPlayed += 1

def handleGesammtScore():
    global gesammtScore
    datei = open("AlienStatsGesammtScore.txt", "a+")
    datei.close
    datei = open("AlienStatsGesammtScore.txt", "r+")
    datei.write(str(score) + "\n")
    for line in datei:
        gesammtScore += int(line)
    datei.close()

def handleAverageScore():
    global averageScore
    averageScore = int(gamesPlayed) / int(gesammtScore)

def showStats(statsButton):
    global message
    global size
    global textX
    global textY
    WINDOW.blit(BLURED_SPACE_BACKGROUND, (0, 0))
    size = 125
    textX = WINDOWWIDTH / 2
    textY = 300
    message = "TOTAL SCORE:    " + str(gesammtScore)
    showText()
    textY = 430
    message = "GAMES PLAYED:   " + str(gamesPlayed)
    showText()
    statsButton.draw()

def delStats():
    if os.path.isfile("AlienStatsGamesPlayed.txt"):
        os.remove("AlienStatsGamesPlayed.txt")
    if os.path.isfile("AlienStatsGesammtScore.txt"):
        os.remove("AlienStatsGesammtScore.txt")

def showHelp():
    global message
    global size
    global textX
    global textY
    WINDOW.blit(BLURED_SPACE_BACKGROUND, (0, 0))
    size = 50
    textX = WINDOWWIDTH / 2
    message = "You can Move by Pressing WASD on your Keyboard. You can teleport by Picking"
    textY = 50
    showText()
    message = "up a teleport item and Pressing the left mouse button. You can see your"
    textY = 125
    showText()
    message = "current statistiks by holding the stats button in the munue. You can reset your"
    textY = 200
    showText()
    message = "stats by pressing the button next to the stats button. To see the original"
    textY = 275
    showText()
    message = "Grafiks you need to put the file of this game into a folder and next to it"
    textY = 350
    showText()
    message = "there must be a new folder named \"assets\". In this folder you can put the images of the game."
    textY = 425
    showText()
    message = "Name them: AktiveExitButton.png, ExitButton.png, HelpButton.png,"
    textY = 550
    showText()
    message = "StatsButton.png, AktivePlayButton.png, PlayButton.png, GameOverScreen.png, HeartItem.png,"
    textY = 625
    showText()
    message = "StartMenueSpaceBackground.png, SpaceBackground.png, Asterioid4.png, TeleportItem.png,"
    textY = 700
    showText()
    message = "Asterioid3.png, Asterioid2.png, Asterioid1.png, AlienRaumschiff.png"
    textY = 775
    showText()
    helpButton.draw()



# Classes


class Asteroid(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = WINDOWWIDTH + random.randint(200, 5000)
        self.y = random.randint(50, WINDOWHEIGHT - 400)
        self.width = 300
        self.height = 150 
        self.image = random.choice((ASTEROID1, ASTEROID2, ASTEROID3, ASTEROID4))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 12.5

    def draw(self):
        WINDOW.blit(self.image, (self.x, self.y))

    def move(self):
        self.x -= self.speed
        self.rect.center = (self.x, self.y)

    def offMap(self):
        global score
        if self.x - self.speed < 0 - self.width:
            score += 1
            self.update()
            return True

    def update(self):

        self.x = WINDOWWIDTH + self.width
        self.y = random.randint(200, WINDOWWIDTH - 200)

        self.image = random.choice((ASTEROID1, ASTEROID2, ASTEROID3, ASTEROID4))

        self.speed += 0.5
        self.rect.center = (self.x, self.y)


class Item:

    def __init__(self, image):
        self.x = WINDOWWIDTH + 50
        self.y = WINDOWHEIGHT + 50
        self.width = 50
        self.height = 50
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def itemSpawn(self):
        itemSpawnChoice = random.randint(1, 25)
        if itemSpawnChoice == 1:
            self.x = (random.randint(100, WINDOWWIDTH - 200))
            self.y = (random.randint(100, WINDOWHEIGHT - 200))
            self.draw()

    def draw(self):
        WINDOW.blit(self.image, (self.x, self.y))

    def update(self):
        self.x = WINDOWWIDTH + 50
        self.y = WINDOWHEIGHT + 50


class Button:

    def __init__(self, x, y, w, image):
        self.x = x
        self.y = y
        self.image = image
        self.h = 129
        self.w = w

    def draw(self):
        WINDOW.blit(self.image, (self.x, self.y))

    def aktiv(self, mausPos):
        if mausPos[0] > self.x and mausPos[0] < self.x + self.w and mausPos[1] > self.y and mausPos[1] < self.y + self.h:
            return True
        else:
            return False

asteroidGroup = pygame.sprite.Group()
asteroid1 = Asteroid()
asteroidGroup.add(asteroid1)
asteroid2 = Asteroid()
asteroid3 = Asteroid()
asteroid4 = Asteroid()
asteroid5 = Asteroid()

asteroidenListe = [asteroid1, asteroid2, asteroid3, asteroid4, asteroid5]

heartItem = Item(HEART_ITEM)
teleportItem = Item(TELEPORT_ITEM)

itemListe = [heartItem, teleportItem]

playButton = Button(575, 500,607, PLAY_BUTTON)
statsButton = Button(575, 650, 607, STATS_BUTTON)
helpButton = Button(WINDOWWIDTH - 100, WINDOWHEIGHT - 100, 607, HELP_BUTTON)
exitButton = Button(statsButton.x - 150, statsButton.y + 7, 129, EXIT_BUTTON)

def game():

    global ALIEN_RAUMSCHIFF
    global teleportsLeft
    global score
    global lives
    global WINDOW
    global highScoreTextColour
    global mausPos
    global message
    global size
    global textX
    global textY

    asteroidsOnScreen = 0
    rundenZähler = 0
    global WINDOWWIDTH
    global WINDOWHEIGHT


    while lives > 0:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                teleport(alien, mausPos)



        rundenZähler += 1
        if rundenZähler % 1860 == 0:
            asteroidsOnScreen += 1
            asteroidGroup.add(asteroidenListe[asteroidsOnScreen])


        if alien.colliderect(teleportItem.rect):
            score += 1
            teleportItem.update()
            teleportsLeft += 1

        if alien.colliderect(heartItem.rect):
            score += 1
            heartItem.update()
            lives += 1

        
        mausPos = pygame.mouse.get_pos()
        keysPressed = pygame.key.get_pressed()

        drawAlien(alien)
        movement(alien, keysPressed)
        asteroidGroup.draw(WINDOW)

        if keysPressed[pygame.K_ESCAPE]:
            menue()

        if keysPressed[pygame.K_q]:
            exit()

        for asteroid in asteroidGroup:
            asteroid.move()
            asteroid.offMap()
            if alien.colliderect(asteroid):
                lives -= 1
                drawAlien(alien)
                time.sleep(2)
                for asteroid in asteroidGroup:
                    asteroid.update()
                asteroid.update()
                alien.x = WINDOWWIDTH - WINDOWWIDTH
                alien.y = WINDOWHEIGHT - WINDOWHEIGHT
        message = score
        size = 125
        textX = WINDOWWIDTH - 50
        textY = 45
        showText()

        heartItem.draw()
        teleportItem.draw()

        heartItem.rect.x = heartItem.x
        heartItem.rect.y = heartItem.y

        teleportItem.rect.x = teleportItem.x
        teleportItem.rect.y = teleportItem.y

        if rundenZähler % 360 == 0: # 60 FPS = Alle 5 sekunden KANN ein Item Spawnen
                heartItem.itemSpawn()
                teleportItem.itemSpawn()


        pygame.display.update()
        
    handleGesammtScore()
    if score > int(highScore):
        writeHighscore()
        highScoreTextColour = (255, 102, 0)
    setHighscore()
    handleStats()
    endScreen()




def endScreen():  
    global message
    global size
    global textX
    global textY
    while True:
        keysPressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if keysPressed[pygame.K_q]:
            exit()

        WINDOW.fill((0, 0, 0))
        if not gameOverImageError:
            WINDOW.blit(GAMEOVER, (5, 30))
        else:
            message = "Score:"
            size = 125
            textX = 800
            textY = 540
            showText()
            message = "HighScore:"
            textY = 625
            showText()
        message = score
        textX = 1100
        textY = 540
        showText()
        showHighScore(1250, 625, highScoreTextColour)
        pygame.display.update()

def menue():
    handleGesammtScore()
    handleStats()
    global mausPos
    global message
    global size
    global textX
    global textY

    while True:
        keysPressed = pygame.key.get_pressed()
        mausPos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        WINDOW.blit(BLURED_SPACE_BACKGROUND, (0, 0))
        playButton.draw()
        statsButton.draw()
        helpButton.draw()
        exitButton.draw()
        try:
            WINDOW.blit(LOGO, (10, 25))
        except:
            size = 125
            textX = WINDOWWIDTH / 2
            textY = 75
            message = "Alien VS Asteroids"
            showText()

        if keysPressed[pygame.K_q]:
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if playButton.aktiv(mausPos):
            playButton.image = AKTIVE_PLAY_BUTTON
            if click[0] or click[2]:
                break
        else:
            playButton.image = PLAY_BUTTON
        
        if statsButton.aktiv(mausPos):
            statsButton.image = AKTIVE_STATS_BUTTON
        else:
            statsButton.image = STATS_BUTTON
        if statsButton.aktiv(mausPos) and click[0] or click[2]:
            showStats(statsButton)

        if exitButton.aktiv(mausPos):
            exitButton.image = AKTIVE_EXIT_BUTTON
        else:
            exitButton.image = EXIT_BUTTON
        if exitButton.aktiv(mausPos) and click[0] or click[2]:
            delStats()

        if helpButton.aktiv(mausPos) and click[0] or click[2]:
            showHelp()

        pygame.display.update()

    game()

if __name__ == "__main__":
    menue()