import pygame
from settings import Settings
from pygame.sprite import Sprite
import random


class Bear(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/bear.png"), (50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.settings.screen_W)
        self.rect.y = 550
        self.x = float(self.rect.x)
        self.count = 0
    def update(self):
        self.x -= self.settings.bear_speed
        self.rect.x = self.x

        if self.rect.left < 0:
            self.settings.bear_speed = -1
        if self.rect.x > self.settings.screen_W - 50:
            self.settings.bear_speed = 1

        self.settings.screen.blit(self.image, self.rect)