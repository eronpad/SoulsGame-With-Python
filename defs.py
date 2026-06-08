import pygame

def carregarSprite(nome, escala = 1):
    sprite = pygame.image.load(f"sprites/{nome}").convert_alpha()

    if(escala != 1):
        largura = int(sprite.get_width() * escala)
        altura = int (sprite.get_height() * escala)

        sprite = pygame.transform.scale(
            sprite,(largura, altura)
        )