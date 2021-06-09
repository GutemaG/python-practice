import pygame
pygame.init()

win=pygame.display.set_mode((800,600))
pygame.display.set_caption("Trying")
bgImg=pygame.image.load('background.png')

#Player
playerImg=pygame.image.load('space-invaders.png')
playerX,playerY=400,530
playerx_change=0

#Bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=playerX+16
bulletY=playerY-16
bullet_change=10
bullet_state='ready'
def move_player(playerX,playerY):
    win.blit(playerImg,(playerX,playerY))
def fire(bulletX,bulletY):
    global bullet_state
    bullet_state='fire'
    win.blit(bulletImg,(bulletX+16,bulletY-16))

running=True
while running:
    win.fill((128,128,128))
    win.blit(bgImg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_LEFT:
                playerx_change=-5
            if event.key==pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX=playerX
                    fire(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change=0
    playerX+=playerx_change
    if playerX<0:
        playerX=0
    elif playerX>740:
        playerX=740
    if bulletY<0:
        bulletY=playerY-16
        bullet_state='ready'
    if bullet_state is 'fire':
        fire(bulletX,bulletY)
        bulletY-=bullet_change
    move_player(playerX,playerY)
    pygame.display.update()
