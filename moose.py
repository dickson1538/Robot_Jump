import pygame
from settings import Settings
from pygame.sprite import Sprite
from wall import Wall
import random


class Moose(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.wall= Wall()

        self.image = pygame.transform.scale(pygame.image.load("assets/moose.png"), (50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 550
        self.x = float(self.rect.x)
        self.count = 0
    def update(self):
        self.x -= self.settings.moose_speed
        self.rect.x = self.x

        if self.rect.left < 0:
            self.settings.moose_speed = -1
        if self.rect.x > self.wall.rect.x - 50:
            self.settings.moose_speed = 1

        self.settings.screen.blit(self.image, self.rect)
