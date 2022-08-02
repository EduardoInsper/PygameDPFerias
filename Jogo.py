import pygame
import random
pygame.init()

#Configuração da tela do jogo
tela_tamanho=(750, 750)
tela=pygame.display.set_mode(tela_tamanho)
pygame.display.set_caption("Doodle Jump")
tela.fill(0, 0, 255)
pygame.disply.flip()
timer=pygame.time.Clock()
self.running=True
self.show=True

score=0
max_score=0
saved_max_sore=0
game_over= False

for event in pygame.event.get():
    if event.key == pygame.K_SPACE and game_over:
        game_over=False
        score=0
        