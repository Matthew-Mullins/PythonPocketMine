import random
import pygame

class Tile(object):
    TILE_W = 64
    TILE_H = 64

    def __init__(self, row, col, value):
        self.rect = pygame.rect.Rect((col * Tile.TILE_W, row * Tile.TILE_H, Tile.TILE_W, Tile.TILE_H))
        self.color = (random.randint(0, 255), 0, 0)
        self.visible = False
        self.value = value

    def update(self):
        self.rect.move_ip(0, -1)

    def on_screen(self):
        return False if self.rect.bottom < 0 else True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color if self.visible else (50, 50, 50), self.rect)