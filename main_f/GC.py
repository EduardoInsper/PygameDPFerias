from string import whitespace
import pygame
import random

from telas import menu_tela
pygame.init()

#Constantes
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
cinza = (100, 100, 100)
background= azul
#jogador_img = pygame.transform.scale(pygame.image.load("spritekkkk.png"), (90, 70))
jogador_idle = pygame.image.load("alladin_jogador/sprite_alladinF00.png")
tapete = pygame.image.load("tapete/sprite_tapete0.png")
fps = 60
fonte_p = pygame.font.Font("aladdin.ttf", 25)
fonte_pontos = pygame.font.Font("freesansbold.ttf", 16)
fonte_g = pygame.font.Font('aladdin.ttf', 40)
timer = pygame.time.Clock()

#Tela
largura = 400
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aladdin")
rodando = False

#variaveis
jogador_x = 180
jogador_y = 400
plataformas=[[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10],[175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump= False
y_change= 0 
x_change=0
velojogador=3
game_over=False

#Pontuação
score=0
max_score=0
saved_max_sore=0
score_last=0


#Update posicao a cada loop
def update_jogador(y_pos):
    global jump 
    global y_change
    jump_height=10
    gravidade= 0.4
    if jump:
        y_change= -jump_height
        jump=False
    y_pos+= y_change
    y_change+= gravidade
    return y_pos

#Update plataformas
def update_plataformas(minhalista, y_pos, change):
    global score
    if y_pos<250 and change<0:
        for i in range(len(minhalista)):
            minhalista[i][1]-= change
    else:
        pass
    for item in range(len(minhalista)):
        if minhalista[item][1]>500:
            minhalista[item]=[random.randint(0, 320), random.randint(-50, -10), 70, 10]
            score+=1
    return minhalista


#Caso haja colisão
def caso_colisao(rect_list, j):
    global jogador_x
    global jogador_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([jogador_x-2, jogador_y + 40, 40, 15]) and jump==False and y_change>0:
            j=True
    return j

#loop do jogo(principal)
menu_tela()
while rodando == False:
    pygame.mixer.music.load("MusicaJogo.mp3")
    pygame.mixer.music.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rodando = True
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
        tela.blit(fonte_p.render('Para começar/recomeçar aperte espaço' , True , branco) , (largura/12,altura/6))
        tela.blit(fonte_p.render('Ande com as teclas"A" e "D"' , True , branco) , (largura/7,altura/2))
        tela.blit(fonte_p.render('Para sair aperte ESC' , True , branco) , (largura/4.5,altura/1.5))
        
        pygame.display.update()
while rodando:
    timer.tick(fps)
    tela.fill(background)
    tela.blit(jogador_idle, (jogador_x, jogador_y))
    blocos= []
    #Textos de pontuação
    texto_pontuacao= fonte_pontos.render("Score: "+  str(score), True, branco, background )
    tela.blit(texto_pontuacao,(300,20))
    texto_maxpontuacao= fonte_pontos.render("High Score: "+  str(max_score), True, branco, background )
    tela.blit(texto_maxpontuacao,(280,40))
    #Criação de blocos
    for i in range(len(plataformas)):
        bloco= pygame.draw.rect(tela, preto, plataformas[i], 0, 3)
        blocos.append(bloco)
    #Jogando o jogo
    for event in pygame.event.get():
        #Caso o usuario saia
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            #Para reiniciar, clicando em space
            if event.key==pygame.K_SPACE and game_over:
                game_over=False
                score=0
                jogador_x=170
                jogador_y=400
                background=azul
                score_last=0
                plataformas=[[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10],[175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
            #Funcionamento do jogo
            if event.key == pygame.K_a:
                x_change = -velojogador
            if event.key == pygame.K_d:
                x_change = velojogador
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0

    #Verificar colisão
    jump=caso_colisao(blocos, jump )
    #Update
    jogador_x+= x_change

    if jogador_y < 440:
        jogador_y = update_jogador(jogador_y)
    else:
        game_over=True
        y_change=0
        x_change=0

    plataformas=update_plataformas(plataformas, jogador_y, y_change)
    
    if jogador_x < -20:
        jogador_x= -20
    elif jogador_x>330:
        jogador_x=330
    # Espelha personagem de acordo com sentido do movimento
    if x_change >0:
        jogador_idle = pygame.image.load("alladin_jogador/sprite_alladinF00.png")
    elif x_change<0:
        jogador_idle = pygame.transform.flip(pygame.image.load("alladin_jogador/sprite_alladinF00.png"), 1, 0)
    #Contabiliza high score
    if score>max_score:
        max_score=score
    #Muda fundo de 15 em 15 blocos
    if score-score_last>15:
        score_last= score
        background=(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    pygame.display.flip()

pygame.quit()