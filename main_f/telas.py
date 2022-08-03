import pygame
  
pygame.init()
largura = 400
altura = 500
tela = pygame.display.set_mode((largura, altura))
cor_clara = (170,170,170)
cor_escura = (100,100,100)
roxo = (100,0,100)
menu = True
#text = GC.fonte_p.render('Sair' , True , GC.branco)
smallfont = pygame.font.SysFont('Corbel',35)
color = (255,255,255)
text = smallfont.render('quit' , True , color)
  
while menu:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            menu = False
              
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            if largura/2 <= mouse[0] <= largura/2+140 and altura/2 <= mouse[1] <= altura/2+40:
                menu = False
                  
    tela.fill(roxo)
      
    mouse = pygame.mouse.get_pos()
      
    if largura/2 <= mouse[0] <= largura/2+140 and altura/2 <= mouse[1] <= altura/2+40:
        pygame.draw.rect(tela,cor_clara,[largura/2,altura/2,140,40])
          
    else:
        pygame.draw.rect(tela,cor_escura,[largura/2,altura/2,140,40])
      

    tela.blit(text , (largura/2+50,altura/2))
      
    pygame.display.update()
pygame.quit()