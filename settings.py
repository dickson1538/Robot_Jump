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
        self.robot_health = 100



        #
        self.bear_speed = 2
        self.moose_speed = 1
        # owl settings
        self.owl_speed = 3

        # tucan settings
        self.tucan_speed = 4
        self.number_of_tucans = 8







