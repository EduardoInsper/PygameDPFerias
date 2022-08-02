import pygame
pygame.init()

#Configuração da tela do jogo
tela_tamanho=(750, 750)
tela=pygame.display.set_mode(tela_tamanho)
pygame.display.set_caption("Jogo da cobrinha")
branco=(255, 255, 255)
tela.fill(branco)