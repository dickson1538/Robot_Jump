import pygame
import random
from settings import Settings
from pygame.sprite import Sprite


class Owl(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/owl.png"), (40, 40))

        self.rect = self.image.get_rect()

        self.rect.x = -40
        self.rect.y = random.randint(0, 300)
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.owl_speed
        self.rect.x = self.x

        if self.rect.left < 0:
            self.settings.owl_speed = -3
        if self.rect.x > self.settings.screen_W - 50:
            self.settings.owl_speed = 3


        self.settings.screen.blit(self.image, self.rect)