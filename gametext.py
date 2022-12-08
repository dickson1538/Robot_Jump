import pygame
from settings import Settings
import time, sys
from button import Button
from person import Person


class Gametext:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.person = Person()

        self.play_button = pygame.image.load("assets/Play Rect.png")
        self.play_button_rect = self.play_button.get_rect()

        self.background = pygame.transform.scale(pygame.image.load("assets/balck.png"),
                                                 (self.settings.screen_W, self.settings.screen_H))

        self.play = False
        self.restart = False
        self.quit = False

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def play_again_menu(self):

        self.settings.screen.blit(self.background, (0, 0))

        menu_mouse_postion = pygame.mouse.get_pos()

        game_over_text = self.get_font(50).render("GAME OVER", True, "#b68f40")
        game_over_text_rec = game_over_text.get_rect(
            center=(300, 30))

        play_button = Button(image=self.play_button, pos=(300, 300),
                             text_input="PLAY AGAIN", font=self.get_font(35), base_color="#b68f40",
                             hovering_color="White")

        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300, 500),
                             text_input="QUIT GAME", font=self.get_font(35), base_color="#b68f40",
                             hovering_color="White")

        self.settings.screen.blit(game_over_text, game_over_text_rec)

        for button in [play_button, quit_button]:
            button.change_color(menu_mouse_postion)
            button.update(self.settings.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_postion):
                    self.restart = True
                    if self.restart:
                        self.settings.robot_health = 100



                if quit_button.check_for_input(menu_mouse_postion):
                    self.quit = True
                    if self.quit:
                        self.quit = False
                        pygame.quit()
                        sys.exit()

                pygame.display.update()