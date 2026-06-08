import pygame
from defs import *
pygame.init()
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

#Da set no tamanho da tela e tbm o nome do game
tela = pygame.display.set_mode((1280 , 720))
pygame.display.set_caption("Python Game")


rodando = True
obj_ativo = True #isso faz com que futuramente, todos o objs morram, ent tem que ver isso
#talvez usar dicionario, ia ser bom, porem longo
#Carregar Sprites

player = Player(
    player_x,
    player_y,
    carregarSprite("player.png", 2)
)
kill_sprite = carregarSprite("bloco.png", 4)

#x horizontal
#faz fechar
while rodando:
    tela.fill((80,80,80))
    pygame.draw.rect(tela, (100, 65, 154), (0, chao_y, 1280, 120))
    player_col = player.sprite.get_rect(
    topleft=(player.x, player.y)
)
    player.desenhar(tela)

    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    # Só pula se estiver no chão
                    if player_y + player_altura >= chao_y:
                        vely = forca_pulo

    vely += gravidade
    player_y += vely
    if player.y + player_altura >= chao_y:
        player.y = chao_y - player_altura
        vely = 0

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_a]:
        player.x -= 5
    if tecla[pygame.K_d]:
         player.x += 5
    


    if obj_ativo == True:
        object = pygame.Rect(500, 550, 64, 64)
        tela.blit(kill_sprite,(500,550), object)
        print(kill_sprite)

        if player_col.colliderect(object):
            print("HIT!")
            obj_ativo = False
    

   
    pygame.display.update()
pygame.quit()

