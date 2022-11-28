import pygame
from settings import Settings
from pygame.sprite import Sprite


class Bird(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.image = pygame.transform.scale(pygame.image.load("assets/owl.png"), (50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.settings.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def _check_fleet_edges(self):
        if self.check_edges():
            self._change_owl_direction()

    def _change_owl_direction(self):
        self.settings.owl_direction *= -1

    def update(self):
        self.x += (self.settings.owl_speed * self.settings.owl_direction)  # this is the fleet direction 1,-1 changes it
        self.rect.x = self.x

        self.settings.screen.blit(self.image, self.rect)
