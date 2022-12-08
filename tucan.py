import pygame
import random
from settings import Settings
from pygame.sprite import Sprite


class Tucan(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/parrot.png"), (30, 30))

        self.rect = self.image.get_rect()

        self.rect.x = 600
        self.rect.y = random.randint(300, 450)

        self.x = float(self.rect.x)

    def update(self):
        self.rect.x = self.x
        self.x -= self.settings.tucan_speed

        if self.rect.left <= self.image.get_width()-60:
            self.x = self.image.get_width()+self.settings.screen_W
            self.rect.y = random.randint(300, 450)

    def draw(self):
        self.settings.screen.blit(self.image, self.rect)