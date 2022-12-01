import pygame


class Settings:

    def __init__(self):
        # Screen settings
        self.screen_H = 600
        self.screen_W = 600
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.screen_H, self.screen_W))
        self.screen_rect = self.screen.get_rect()

        # robot settings
        self.robot_height = 70
        self.robot_width = 90
        self.robot_speed = 3
        self.run_cooldown = 8
        self.health = 30

        # owl settings
        self.owl_speed = 1
        self.owl_direction = 1

        # Platform settings
        self.platform_color = (200, 0, 0)


