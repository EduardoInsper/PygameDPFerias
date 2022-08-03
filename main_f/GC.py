import pygame
pygame.init()

#constantes
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
cinza = (100, 100, 100)
jogador_img = pygame.transform.scale(pygame.image.load("spritekkkk.png"), (90, 70))
fps = 60
fonte_p = pygame.font.Font('aladdin.ttf', 16)
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

#Update posicao a cada loop
def update_jogador(y_pos):
    global jump 
    global y_change
    jump_height=9
    gravidade= 0.3
    if jump:
        y_change= -jump_height
        jump=False
    y_pos+= y_change
    y_change+= gravidade
    return y_pos

#Update plataformas


#Caso haja colisão
def caso_colisao(rect_list, j):
    global jogador_x
    global jogador_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([jogador_x+20, jogador_y + 60, 90, 5]) and jump==False and y_change>0:
            j=True
    return j

#loop do jogo
while rodando:
    timer.tick(fps)
    tela.fill(azul)
    tela.blit(jogador_img, (jogador_x, jogador_y))
    blocos= []
    for i in range(len(plataformas)):
        bloco= pygame.draw.rect(tela, preto, plataformas[i], 0, 3)
        blocos.append(bloco)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -velojogador
            if event.key == pygame.K_d:
                x_change = velojogador
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0

    jogador_y= update_jogador(jogador_y)
    jump=caso_colisao(blocos, jump )
    jogador_x+= x_change
    jogador_y = update_jogador(jogador_y)
    plataformas=update_plataformas()
    pygame.display.flip(plataformas, jogador_y, y_change)

pygame.quit()