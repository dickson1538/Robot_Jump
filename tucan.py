import pygame
import random
from settings import Settings
from pygame.sprite import Sprite


class Tucan(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/parrot.png"), (20, 20))

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.settings.screen_W)
        self.rect.y = random.randint(0, self.settings.screen_H)
        self.x = float(self.rect.x)
        self.count = 0

    def update(self):
        self.x -= self.settings.tucan_speed
        self.rect.x = self.x

        if self.rect.left < 0:
            self.rect.x = 600
            self.settings.screen.blit(self.image, self.rect)

        self.settings.screen.blit(self.image, self.rect)
