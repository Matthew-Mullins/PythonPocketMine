import pygame

import random 

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
        mouse_path = []
        cur_path = []
        def create_square():
            square = pygame.draw.rect(self.GAME_DISPLAY, (255, 255, 255), pygame.Rect(random.randint(25, INITIAL_WINDOW_W - 25), random.randint(25, INITIAL_WINDOW_H - 25), 50, 50))
            return square
    
        def draw_all_lines():
            self.GAME_DISPLAY.fill((0, 0, 0))
            for path in mouse_path:
                i = mouse_path.index(path)
                pygame.draw.lines(self.GAME_DISPLAY, ((i / len(mouse_path)) * 255, (i / len(mouse_path)) * 128, (i / len(mouse_path)) * 64), False, path)

        cur_square = create_square()
        clicked = 0

        # Game Loop
        crashed = False
        while not crashed:
            # Get Input / Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if cur_square.collidepoint(pos):
                        clicked += 1
                        self.GAME_DISPLAY.fill((0, 0, 0))
                        mouse_path.append(cur_path)
                        pygame.draw.lines(self.GAME_DISPLAY, (255, 0, 0), False, cur_path)
                        cur_path = []
                        if clicked % 10 == 0 and clicked != 0:
                            draw_all_lines()
                        cur_square = create_square()
                if event.type == pygame.MOUSEMOTION:
                    cur_path.append(event.pos)

                print(event)

            # Update
            self.clock.tick(FRAMES_PER_SECOND)

            # Render
            pygame.display.update()

        # On Close
        pygame.quit()
        quit()