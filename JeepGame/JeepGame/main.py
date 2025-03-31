import pygame
from pygame import mixer
import random
import time
pygame.init()

pygame.display.set_caption("Jeep Jumper")
window = pygame.display.set_mode((800, 600))
mixer.music.load('Doom OST - E2M8 - Nobody Told Me About Id.wav')
top_icon = pygame.image.load('cactus.png')
pygame.display.set_icon(top_icon)
BG = pygame.image.load('DesertBG.png')
BG = pygame.transform.scale(BG, (800, 600))

Cactus = pygame.image.load('cactus.png')
Cactus = pygame.transform.scale(Cactus, (64, 64))
CactusX = 1000


def cacti(x):
    window.blit(Cactus, (x, 500))


def bg():
    window.blit(BG, (0, 0))


TNT = pygame.image.load('tnt.png')
TNT = pygame.transform.scale(TNT, (64, 64))

Score = 0
Meter = 0
highScore = 0
font = pygame.font.Font('freesansbold.ttf', 22)
ScoreX = 65
ScoreY = 50
displayHighScore = 560


def Travel(s, x, y):
    travel = font.render("Distance: " + str(s) + "M", True, (139, 0, 139))
    window.blit(travel, (x, y))


def displayHS(h):
    display = font.render("High Score: " + str(h) + "M", True, (139, 0, 139))
    window.blit(display, (displayHighScore, ScoreY))


Game = pygame.font.Font('freesansbold.ttf', 35)
stopCount = 0
isOver = False


def gameOver():
    over = Game.render("You Died. You lasted for " + str(stopCount) + " Metres", True, (255, 255, 0))
    window.blit(over, (150, 460))
    high = Game.render("High Score: " + str(highScore) + " Metres", True, (255, 255, 0))
    window.blit(high, (230, 500))


screenInitial = pygame.font.Font('freesansbold.ttf', 64)
inst = pygame.font.Font('freesansbold.ttf', 28)
loadingScreen = pygame.image.load('cactus.png')
c = False


def initialScreen():
    window.fill((255, 140, 0))
    window.blit(loadingScreen, (350, 200))
    if c:
        gameOver()
    i = screenInitial.render("Jeep Jumper", True, (255, 215, 0))
    window.blit(i, (200, 250))
    instructions = inst.render("press spacebar to jump, x to shoot and r to start", True, (255, 255, 255))
    window.blit(instructions, (65, 350))
    pygame.display.flip()
    wait = True
    while wait:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_r:
                    wait = False


def tnt(x, y):
    window.blit(TNT, (x, y))


tntX = 800
tntY = 320
speedCounter = 1.6
position = 0

Jeep = pygame.image.load('JeepIconTransparent.png')
Jeep = pygame.transform.scale(Jeep, (125, 125))


def jeep(x, y):
    window.blit(Jeep, (x, y))


jeepX = 200
jeepY = 370
heightCounter = 0
heightCounter2 = 1
jumpBool = False
jumpTime = 0
invincibility = False
invincible = 0

Bullet = pygame.image.load('bullet (2).png')
Bullet = pygame.transform.scale(Bullet, (32, 32))


def bullet(x, y):
    window.blit(Bullet, (x, y))


bulletX = 300
bulletY = jeepY
bulletActivated = False
bulletSpeed = False


Sign = pygame.image.load('SignBoard.png')
Sign = pygame.transform.scale(Sign, (400, 300))


def sign(x, y):
    window.blit(Sign, (x, y))


signX = 500
signY = 300
timer = 0
timer2 = 0
counting = False
transport = False

running = True

initial = True
while running:
    if initial:
        initialScreen()
        initial = False
        c = True
        isOver = False
        mixer.music.play(-1)
        Score = 0
        Meter = 0
        tntX = 800
        tntY = 320
        speedCounter = 1.6
        position = 0
        jeepX = 200
        jeepY = 290
        heightCounter = 0
        heightCounter2 = 1
        jumpBool = False
        jumpTime = 0
        invincibility = False
        invincible = 0
        bulletX = 300
        bulletY = jeepY
        bulletActivated = False
        bulletSpeed = False
        stopCount = 0
        timer = 0
        timer2 = 0
        counting = False
        transport = False
        bg()
        tnt(tntX, tntY)
        jeep(jeepX, jeepY)
        sign(signX, signY)
        signX = 500
        cacti(CactusX)
        CactusX = 900
    timer += 1
    bg()
    Meter += 1
    if Meter % 10 == 0 and stopCount == False:
        Score = Meter // 10
    Travel(Score, ScoreX, ScoreY)
    displayHS(highScore)
    if Score > highScore:
        highScore = Score
    tnt(tntX, tntY)
    jeep(jeepX, jeepY)
    sign(signX, signY)
    cacti(CactusX)
    CactusX -= speedCounter
    if CactusX <= -100:
        CactusX = 900
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumpSound = mixer.Sound('Jump.wav')
                jumpSound.play()
                jumpBool = True
                jeepY = 200
            if event.key == pygame.K_x:
                bulletActivated = True
                bulletSound = mixer.Sound('gunshot.wav')
                bulletSound.play()
    if jumpBool:
        jumpTime += 1
    if jumpTime == 100:
        jumpBool = False
        landSound = mixer.Sound('Land.wav')
        landSound.play()
        jeepY = 290
        jumpTime = 0
        heightCounter = 0
        heightCounter2 = 1
        invincibility = True
    if invincibility:
        invincible += 1
    if invincible == 200:
        invincibility = False
        invincible = 0
    if jeepY == 290 and heightCounter2 > heightCounter:
        jeepY = 295
        heightCounter += 2
    elif jeepY == 295 and heightCounter > heightCounter2:
        jeepY = 290
        heightCounter2 += 2
    tntX -= speedCounter
    if tntX <= -20 or transport:
        transport = False
        position = random.randrange(3)
        if position == 0:
            tntX = 800
        elif position == 1:
            tntX = 950
        else:
            tntX = 1000
        speedCounter += 0.01

    if bulletActivated:
        bullet(bulletX, bulletY)
        bulletSpeed = True

    if bulletSpeed:
        bulletX += 10
    if bulletX == 800:
        bulletActivated = False
        bulletX = 300
    if timer == 600:
        signX = 900
        counting = True

    if counting:
        timer2 += 1
    if timer2 == 700:
        counting = False
        timer = 0
        timer2 = 0
        signX = 500
    elif timer2 < 700 and timer2 != 0:
        if bulletActivated and tntX > 300:
            transport = True

    # not jumping when sign is there death:
    if tntX <= jeepX and jeepY != 200 and invincible == 0 and counting == False:
        isOver = True
        stopCount = Score
    # shooting when sign is there death:
    elif bulletActivated and counting == False:
        isOver = True
        stopCount = Score
    # jumping when sign is not there death:
    elif jeepY == 200 and timer2 > 200:
        isOver = True
        stopCount = Score
    # colliding with tnt when sign is not there death:
    elif tntX <= jeepX and timer2 > 100:
        isOver = True
        stopCount = Score
    if isOver:
        time.sleep(2)
        initial = True
    pygame.display.update()
