#NAO RODAR- BASE
import pygame
import random
from telas import *
from GC import *
pygame.init()

bg = pygame.image.load("tela_inicial.jpg")
bg = pygame.transform.scale(bg, (400, 500))
largura = 400
altura = 500
tela = pygame.display.set_mode((largura, altura))
cor_clara = (170,170,170)
cor_escura = (100,100,100)
preto = (0,0,0)
fonte_p = pygame.font.Font('aladdin.ttf', 27)
branco = (255,255,255)
menu = True

branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
cinza = (100, 100, 100)
background= azul
jogador_img = pygame.transform.scale(pygame.image.load("spritekkkk.png"), (90, 70))
fps = 60
fonte_p = pygame.font.Font('aladdin.ttf', 27)
fonte_g = pygame.font.Font('aladdin.ttf', 32)
timer = pygame.time.Clock()
largura = 400
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aladdin")
rodando = True

#variaveis
jogador_x = 170
jogador_y = 400
plataformas=[[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10],[175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump= False
y_change= 0 
x_change=0
velojogador=3

#Pontuação
score=0
max_score=0
saved_max_sore=0
score_last=0

menu_tela()