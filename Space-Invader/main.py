import pygame
import random
import math

pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('001-spacecraft.png')
pygame.display.set_icon(icon)

spaceship = pygame.image.load('001-battleship.png')

bullet = pygame.image.load('bullet2.png')

# Player Coordinate
coorX = 370
coorY = 500
moveX = 0

enemyship = []
enemyCoorX = []
enemyCoorY = []
enemyMoveX = []
enemyMoveY = []
enemyCtr = 5
for i in range(enemyCtr):
    enemyship.append(pygame.image.load('alien.png'))
    enemyCoorX.append(random.randint(0, 736))
    enemyCoorY.append(random.randint(50, 150))
    enemyMoveX.append(0.3)
    enemyMoveY.append(40)

# Bullet Coordinate
bulletCoorX = 0
bulletCoorY = 500
bulletMoveX = 0
bulletMoveY = 0.7
bullet_state = "ready"


# moving the object
def shipCoor(x, y):
    screen.blit(spaceship, (x, y))


def enemyCoor(x, y, i):
    screen.blit(enemyship[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

def collision(enemyCoorX, enemyCoorY, bulletCoorX, bulletCoorY):
    c = math.sqrt((math.pow(enemyCoorX - bulletCoorX, 2)) + (math.pow(enemyCoorY - bulletCoorY, 2)))
    # print(c)
    if c < 27:
        # print("hit")
        return True
    else:
        return False

def scoreCoordinate(x, y):
    showScore = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(showScore, (x, y))

def gameOver():
    gameover = gameOverFont.render("GAMEOVER", True, (255, 255, 255))
    screen.blit(gameover, (200, 250))

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
scoreCoorX = 10
scoreCoorY = 10

# Running the game
run = True
while run:
    screen.fill((0, 0, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moveX = -0.4
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moveX = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletCoorX = coorX
                    fireBullet(bulletCoorX, bulletCoorY)
                # print("Space is pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moveX = 0

    # Player Movement
    coorX += moveX

    # Player Boundaries
    if coorX <= 0:
        coorX = 0
    elif coorX >= 736:
        coorX = 736

    # Enemy Movement
    for i in range(enemyCtr):
        if enemyCoorY[i] > 460:
            for j in range(enemyCtr):
                enemyCoorY[j] = 1000
            gameOver()
            break

        enemyCoorX[i] += enemyMoveX[i]

    # Enemy Boundaries
        if enemyCoorX[i] <= 0:
            enemyMoveX[i] = 0.3
            enemyCoorY[i] += enemyMoveY[i]
        elif enemyCoorX[i] >= 736:
            enemyMoveX[i] = -0.3
            enemyCoorY[i] += enemyMoveY[i]

    # collision
        isCollision = collision(enemyCoorX[i], enemyCoorY[i], bulletCoorX, bulletCoorY)
        if isCollision:
            bulletCoorY = 500
            bullet_state = "ready"
            score += 1
            # print(score)
            enemyCoorX[i] = random.randint(0, 736)
            enemyCoorY[i] = random.randint(50, 150)

        enemyCoor(enemyCoorX[i], enemyCoorY[i], i)

    # Bullet Movement
    if bulletCoorY <= 0:
        bulletCoorY = 500
        bullet_state = "ready"
    if bullet_state == "fire":
        fireBullet(bulletCoorX, bulletCoorY)
        bulletCoorY -= bulletMoveY

    shipCoor(coorX, coorY)
    scoreCoordinate(scoreCoorX, scoreCoorY)
    pygame.display.update()
