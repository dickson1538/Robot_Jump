import pygame
import random
from settings import Settings
from pygame.sprite import Sprite


class Duck(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/duck.png"), (40, 40))

        self.rect = self.image.get_rect()

        self.rect.x = -40
        self.rect.y = random.randint(150, 300)

        self.x = float(self.rect.x)

    def update(self):
        self.rect.x = self.x
        self.x += self.settings.tucan_speed

        if self.rect.right > 650:
            self.x = -40
            self.rect.y = random.randint(150, 300)

    def draw(self):
        self.settings.screen.blit(self.image, self.rect)
