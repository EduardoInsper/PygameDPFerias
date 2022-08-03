import pygame
pygame.init()

branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
cinza = (100, 100, 100)
largura = 400
altura = 500
jogador_img = pygame.image.load("spritekkkk.png")
fps = 60

fonte_p = pygame.font.Font('aladdin.ttf', 16)
fonte_g = pygame.font.Font('aladdin.ttf', 32)


timer = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aladdin")

rodando = True
while rodando:
    timer.tick(fps)
    tela.fill(azul)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    pygame.display.flip()
pygame.quit()