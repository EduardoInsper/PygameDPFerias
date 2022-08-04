import pygame
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
fonte_g = pygame.font.Font('aladdin.ttf', 60)
branco = (255,255,255)
def menu_tela():
    menu = True
    while menu:
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                menu = False
                
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if largura/2 <= mouse[0] <= largura/2+140 and altura/2 <= mouse[1] <= altura/2+40:
                    menu = False
                    pygame.quit()
                if largura/6 <= mouse[0] <= largura/6+140 and altura/2 <= mouse[1] <= altura/2+40:
                    tela.fill(preto)
                    pygame.display.update()
                    pygame.time.delay(400)
                    menu = False
                    return True
        tela.blit(bg, (0,0))
        mouse = pygame.mouse.get_pos()

        if largura/6 <= mouse[0] <= largura/6+130 and altura/2 <= mouse[1] <= altura/2+40:
            pygame.draw.rect(tela, cor_clara, (largura/6-10, altura/2, 140, 40))
        else:
            pygame.draw.rect(tela, cor_escura, (largura/6-10, altura/2, 140, 40))
        
        if largura/2 <= mouse[0] <= largura/2+140 and altura/2 <= mouse[1] <= altura/2+40:
            pygame.draw.rect(tela,cor_clara,[largura/2,altura/2,140,40])      
        else:
            pygame.draw.rect(tela,cor_escura,[largura/2,altura/2,140,40])
        

        tela.blit(fonte_p.render('Sair' , True , branco) , (largura/2+40,altura/2))
        tela.blit(fonte_p.render('Jogar' , True , branco) , (largura/6+40,altura/2))
        tela.blit(fonte_g.render('Aladdin' , True , branco) , (largura/4,altura/6))
        
        pygame.display.update()
menu_tela()