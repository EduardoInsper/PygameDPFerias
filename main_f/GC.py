import pygame
pygame.init()

#constantes
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
cinza = (100, 100, 100)
largura = 400
altura = 500
jogador_img = pygame.transform.scale(pygame.image.load("spritekkkk.png"), (90, 120))
fps = 60
fonte_p = pygame.font.Font('aladdin.ttf', 16)
fonte_g = pygame.font.Font('aladdin.ttf', 32)
timer = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aladdin")
rodando = True

#variaveis
jogador_x = 150
jogador_y = 370
#loop do jogo
while rodando:
    timer.tick(fps)
    tela.fill(azul)
    tela.blit(jogador_img, (jogador_x, jogador_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    pygame.display.flip()
pygame.quit()