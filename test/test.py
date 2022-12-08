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
        self.rect.x = -20
        self.rect.y = random.randint(0, self.settings.screen_H)
        self.left = float(self.rect.x)
        self.right = float(self.rect.x)

        self.Left = False
        self.Right = False

    def update(self):
        count = 0
        self.side()

        if self.Right:
            self.right += self.settings.tucan_speed
            self.rect.x = self.right
            if self.rect.right > 620:
                self.rect.x = -20
                self.settings.screen.blit(self.image, self.rect)
            self.settings.screen.blit(self.image, self.rect)

        if self.Left:
            self.left -= self.settings.tucan_speed
            self.rect.x = self.left
            if self.rect.left < 0:
                self.rect.x = 600
                self.settings.screen.blit(self.image, self.rect)

            self.settings.screen.blit(self.image, self.rect)
            count += 1

    def side(self):
        left_right = random.randint(1, 2)
        if left_right == 1:
            self.Left = True
        if left_right == 2:
            self.Right = True
