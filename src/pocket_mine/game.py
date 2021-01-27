import random 

import pygame
from .mine import Mine

GAME_TITLE = 'PC Mine'

INITIAL_WINDOW_W = 512
INITIAL_WINDOW_H = 910
WINDOW_ASPECT_RATIO = 9 / 16

FRAMES_PER_SECOND = 60

class Game:
    def __init__(self):
        # Create Game Display
        self.GAME_DISPLAY = pygame.display.set_mode((INITIAL_WINDOW_W, INITIAL_WINDOW_H))
        pygame.display.set_caption(GAME_TITLE)

        # Initialize Game Clock
        self.clock = pygame.time.Clock()

    def run(self):
        self.mine = Mine()

        # Game Loop
        crashed = False
        while not crashed:
            # Get Input / Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for section in self.mine.mine:
                        for row in section:
                            for tile in row:
                                if not tile:
                                    continue
                                if tile.rect.collidepoint(pos):
                                    if tile.visible:
                                        self.mine.remove_tile(tile)
                                    # print(tile.rect.center)
                # print(event)

            # Update
            self.GAME_DISPLAY.fill((0, 0, 0))
            self.clock.tick(FRAMES_PER_SECOND)
            for section in self.mine.mine:
                for row in section:
                    for tile in row:
                        if not tile:
                            continue
                        if not tile.on_screen():
                            self.mine.remove_tile(tile)
                            continue
                        tile.update()
                        tile.draw(self.GAME_DISPLAY)

            # Render
            pygame.display.update()

        # On Close
        pygame.quit()
        quit()