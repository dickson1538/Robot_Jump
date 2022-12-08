import pygame
from pygame.sprite import Sprite
from settings import Settings

class Wall(Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/brick.png"), (40, 100))
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect(center= (250,550))

    def draw(self):
        self.settings.screen.blit(self.image, (100,400))
