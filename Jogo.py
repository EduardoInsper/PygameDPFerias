#Importa e inicia pacotes
from sre_constants import JUMP
import pygame
import random

pygame.init()

screen_largura = 600
screen_altura = 800
screen = pygame.display.set_mode((screen_largura,screen_altura))
imageminicial=pygame.image.load("./imagens/tela_inicial.jpg").convert_alpha()
imageminicial = pygame.transform.scale(imageminicial,(600,800))

#Inicia assets
font = pygame.font.SysFont(None, 48)
text = font.render('Aladdin', True, (0, 0, 255))

#Configuração da tela do jogo
screen_largura = 450
screen_altura = 600
screen = pygame.display.set_mode((screen_largura,screen_altura))
imageminicial=pygame.image.load("./imagens/tela_inicial.jpg").convert_alpha()
imageminicial = pygame.transform.scale(imageminicial,(450,600))
pygame.display.set_caption("Aladdin")
screen.blit(text, (10, 10))
blue=(0, 0, 255)

pygame.display.flip()
timer=pygame.time.Clock()
self.running=True
self.show=True

#Variaveis do jogo
score=0
max_score=0
saved_max_sore=0
inicio=False
player=pygame.transform.scale(pygame.image.load("alladin.png", (90, 70)))
player_x=170
player_y=400
platforms=[[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10],[175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
y_change=0
x_change=0
player_speed=3
jump=False

#Página inicial
while not inicio:
    fps.tick(25)
    screen.blit(imageminicial, (0,0) )
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                inicio= True 

#Update posicao a cada loop
def update_player(y_pos):
    global jump 
    global y_change
    jump_height=10
    gravidade= 0.4
    if jump:
        y_change= -jump_height
        jump=False
    y_pos+= y_change
    y_change+= gravidade

#Loop principal
running=True
while running: 
    timer.tick(fps)
    screen.fill(blue)
    screen.blit(player, (player_x, player_y))
    blocks=[]
    for i in range(len(platforms)):
        block=pygame.draw.rect(screen, black, platforms[i], 0, 3)
        blocks.append(block)
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change=-player_speed
            if event.key==pygame.K_d:
                x_change=player_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                x_change=0
            if event.key==pygame.K_d:
                x_change=0
    player_x+= x_change
    player_y=update_player(player_y)
    platforms=update.platforms(platforms, player_y)

#Finalização
pygame.quit()