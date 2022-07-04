'''
Name: Rahil Mehta
This is a simple train game implemented using PyGame.
'''
import sys
import pygame
from pygame import mixer
import time

pygame.init()
mixer.init()
mixer.music.load('train-horn.mp3')
#loss_sound = mixer.Sound('failure.mp3')
size = width, height = 800, 800
speed = [1, 0]
black = 0, 0, 0


screen = pygame.display.set_mode(size)

tracks = pygame.image.load("railroad.png")
tracks = pygame.transform.scale(tracks, (700, 800))
tracksrect = tracks.get_rect()
tracksrect = tracksrect.move((0, 0))

train = pygame.image.load("train.png")
train = pygame.transform.scale(train, (200, 200))
trainrect = train.get_rect()
trainrect = trainrect.move((width / 2.8, height / 1.6))

sheep = pygame.image.load("sheep.png")
sheep = pygame.transform.scale(sheep, (100, 100))
sheeprect = sheep.get_rect()
sheeprect = sheeprect.move((width / 1.4, height / 5))
# Set preferred volume
mixer.music.set_volume(0.2)
running = True
# Play the music
mixer.music.play(loops=-1)
#screen.blit(tracks, tracksrect)
#screen.blit(train, trainrect)
def show_loss_screen():
    # game over
    screen.fill(black)
    bg = pygame.image.load("LossScreen.png")
    screen.blit(bg,(0,0))
    pygame.display.flip()
    mixer.music.load('failure.mp3')
    mixer.music.play()
    time.sleep(20)
    #mixer.Sound.play(loss_sound)
    running = False
status = 1 # 1 = active, -1 = paused
while 1:
    if running:
        screen.fill(black)
    if trainrect.colliderect(sheeprect):
        print('You lose')
        show_loss_screen()
        continue
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_p: 
                status = -status
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[ord('w')]:
        print('Up')
        trainrect.y -= 2
    if keys[pygame.K_DOWN] or keys[ord('s')]:
        print('Down')
        trainrect.y += 2
                #pygame.display.update(trainrect)
    
    '''if status == -1: 
        mixer.music.pause()
    if status == 1:
        mixer.music.unpause()
        tracksrect = tracksrect.move(speed)'''
    sheeprect = sheeprect.move(speed)
    if sheeprect.left < 0 or sheeprect.right > width:
        speed[0] = -speed[0]
    '''if tracksrect.top < 0 or tracksrect.bottom > height:
        speed[1] = -speed[1]'''

    if running:
        screen.blit(tracks, tracksrect)
        screen.blit(sheep, sheeprect)
        screen.blit(train, trainrect)

    pygame.display.flip()