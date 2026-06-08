import pygame

def carregarSprite(nome, escala = 1):
    sprite = pygame.image.load(f"sprites/{nome}").convert_alpha()

    if(escala != 1):
        largura = int(sprite.get_width() * escala)
        altura = int (sprite.get_height() * escala)

        sprite = pygame.transform.scale(
            sprite,
            (largura, altura)
        )

    return sprite

def carregarBg(nome):
    bg = pygame.image.load(f"sprite/{nome}").convert()

    bg = pygame.transform.scale(
        bg,
        (1280, 720)
    )

    return bg


def colisao(nome,  obj_x, obj_y):
    pass


def colisaoPlayer(player_sprite, player_x, player_y):
    player_rect = player_sprite.get_rect(
        topleft=(player_x, player_y)
    )
    return player_rect