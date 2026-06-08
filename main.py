import pygame
from defs import * 
pygame.init()

#Da set no tamanho da tela e tbm o nome do game
tela = pygame.display.set_mode((1280 , 720))
pygame.display.set_caption("Python Game")


rodando = True

#jogador
player_x = 100
player_y = 500
player_largura = 50
player_altura = 50

vely = 0
gravidade = 0.7
forca_pulo = -15

#Chao

chao_y = 600

player_sprite = carregarSprite("player.png", 2)
#faz fechar
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Só pula se estiver no chão
                if player_y + player_altura >= chao_y:
                    vely = forca_pulo
    
    
    vely += gravidade
    player_y += vely
    if player_y + player_altura >= chao_y:
        player_y = chao_y - player_altura
        vely = 0


    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_a]:
        player_x -= 5
    if tecla[pygame.K_d]:
        player_x += 5
    
    
    tela.fill((0,0,0))
    pygame.draw.rect(tela, (100, 65, 154), (0, chao_y, 1280, 120))
    tela.blit(player_sprite,(player_x,player_y))

    pygame.display.update()



pygame.quit()