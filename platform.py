import pygame
from pygame.sprite import Sprite
from settings import Settings


class Platform(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/platform.png"), (150, 50))
        self.rect = self.image.get_rect()

        self.rect.center = self.settings.screen_rect.center

    def update(self):
        self.settings.screen.blit(self.image, (100,400))
