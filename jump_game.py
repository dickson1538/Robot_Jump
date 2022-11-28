import pygame
import sys
from settings import Settings
from person import Person
from platform import Platform
from bird import Bird


class JumpGame:

    def __init__(self):
        self.settings = Settings()
        self.person = Person()
        self.platform = Platform()
        self.bird = Bird()

        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.person,self.bird, self.platform)

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            # 1) check for user input  2) Update game objects   3) draw screen       4) win loose conditions
            self.game_objects.update()
            self.game_objects.draw(self.settings.screen)
            self.update_screen()

            clock.tick(60)

    def update_screen(self):
        self.person.screen.fill((0, 0, 0))

        self.game_objects.update()
        pygame.display.flip()
