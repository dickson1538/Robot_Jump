import pygame
import sys
from pygame.sprite import Sprite
from settings import Settings


class Person(Sprite):

    def __init__(self):
        super().__init__()
        self.settings = Settings()

        self.stand = pygame.transform.scale(pygame.image.load("assets/character_robot_talk.png"), (60, 80))
        self.right_0 = pygame.transform.scale(pygame.image.load("assets/robot_right_0.png"), (60, 80))
        self.right_1 = pygame.transform.scale(pygame.image.load("assets/robot_right_1.png"), (60, 80))
        self.right_2 = pygame.transform.scale(pygame.image.load("assets/robot_right_2.png"), (60, 80))
        self.left_0 = pygame.transform.scale(pygame.image.load("assets/robot_left_0.png"), (60, 80))
        self.left_1 = pygame.transform.scale(pygame.image.load("assets/robot_left_1.png"), (60, 80))
        self.left_2 = pygame.transform.scale(pygame.image.load("assets/robot_left_2.png"), (60, 80))
        self.jump = pygame.transform.scale(pygame.image.load("assets/character_robot_jump.png"), (60, 80))

        # counts how many times it goes through the loop
        self.index = 0
        self.counter = 0
        self.run_right = [self.right_0, self.right_1, self.right_2]
        self.run_left = [self.left_0, self.left_1, self.left_2]

        self.image = self.stand
        self.rect = self.image.get_rect()

        self.moving_right = False
        self.moving_left = False
        self.jumping = False

        # jumping
        self.y_gravity = .6
        self.jumping_height = 20
        self.y_velo = self.jumping_height
        self.x, self.y = self.settings.screen_W, self.settings.screen_H
        self.robot_rect = self.jump.get_rect()

        self.screen = pygame.display.set_mode((self.settings.screen_W, self.settings.screen_H))
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        print(self.rect.midbottom)
        self.userInput = pygame.key.get_pressed()

    def moving_robot(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.robot_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.robot_speed
        if self.jumping:
            self.y -= self.y_velo
            self.y_velo -= self.y_gravity
            if self.y_velo < -self.jumping_height:
                self.jumping = False
                self.y_velo = self.jumping_height

    # checks for keydown and keyup events
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                if event.key == pygame.K_SPACE:
                    self.jumping = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                if event.key == pygame.K_SPACE:
                    self.jumping = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def update(self):
        self.check_events()
        self.moving_robot()

        self.counter += 1
        if self.counter > self.settings.run_cooldown:
            self.counter = 0
            if self.moving_right:
                self.index += 1
                if self.index >= len(self.run_right):
                    self.index = 0
                self.image = self.run_right[self.index]

            if self.moving_left:
                self.index += 1
                if self.index >= len(self.run_left):
                    self.index = 0
                self.image = self.run_left[self.index]

        if self.jumping:
            self.robot_rect = self.jump.get_rect()
            self.screen.blit(self.image, self.robot_rect)
        else:
            self.screen.blit(self.image, self.rect)
