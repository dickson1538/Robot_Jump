import time

import pygame
import sys
from settings import Settings
from person import Person
from platform import Platform
from bird import Bird
from tucan import Tucan
from gametext import Gametext
from button import Button


class JumpGame:

    def __init__(self):
        self.settings = Settings()
        self.person = Person()
        self.platform = Platform()
        self.bird = Bird()
        self.tucan = Tucan()
        self.gametext = Gametext()

        self.tucans = pygame.sprite.Group()
        self.tucans.add(self.tucan)
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.bird, self.person, self.platform, self.tucan)

        self.background = pygame.transform.scale(pygame.image.load("assets/space.png"),
                                                 (self.settings.screen_W, self.settings.screen_H))

        self.timer = 0
        self.PLAY_AGAIN = False
    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            # 1) check for user input  2) Update game objects   3) draw screen       4) win loose conditions
            self.update_screen()
            self.collisions()
            self.tucan_army()
            self.timer += 1
            if self.settings.robot_health <= 0:
                self.gametext.play_again_menu()
            clock.tick(60)

    def update_screen(self):
        self.person.screen.fill((0, 0, 0))
        self.time()
        self.game_objects.update()
        pygame.display.flip()

    def collisions(self):
        owl_collision = pygame.sprite.collide_rect(self.bird, self.person)
        platform_collision = pygame.sprite.collide_rect(self.platform, self.person)


        if owl_collision:
            self.settings.robot_health -= 2
            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)

        if pygame.sprite.spritecollide(self.person, self.tucans, True):
            print("hit")



        if platform_collision:
            if self.person.rect.bottom == self.platform.rect.top:
                self.person.rect = self.platform.rect.top
                print("hit")

    def time(self):
        font = pygame.font.SysFont('Arial', 20)
        game_time_text = font.render(f"TIME SURVIVED: {self.timer // 60}", True, (200, 200, 200))
        game_time_text_rec = game_time_text.get_rect(
            center=(100, 30))
        self.settings.screen.blit(game_time_text, game_time_text_rec)

    def tucan_army(self):
        count = 0
        if len(self.tucans) <= 3:
            new_tucan = Tucan()
            self.tucans.add(new_tucan)
            self.game_objects.add(new_tucan)
            time.sleep(3)

#######################################################################################################################
    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def play_again_menu(self):
        while True:
            self.settings.screen.blit(self.background, (0, 0))

            menu_mouse_pos = pygame.mouse.get_pos()

            self.person.check_events()
            game_over_text = self.get_font(50).render("GAME OVER", True, "#b68f40")
            game_over_text_rec = game_over_text.get_rect(center=(300, 30))

            play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(300, 300),
                                 text_input="PLAY AGAIN", font=self.get_font(35), base_color="#b68f40",
                                 hovering_color="White")

            quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300, 500),
                                 text_input="QUIT GAME", font=self.get_font(35), base_color="#b68f40",
                                 hovering_color="White")

            self.settings.screen.blit(game_over_text, game_over_text_rec)

            for button in [play_button, quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(self.settings.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(menu_mouse_pos):
                        self.play_again()

                    if quit_button.check_for_input(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            #pygame.display.update()

    # this is an idea to get the play again button to work
    def play_again(self):
        self.PLAY_AGAIN = True
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #if self.settings.robot_health <= 0:
                #self.jump.run_game()
            #pygame.display.update()

    def run_quit_menu(self):
        self.play_again()
        self.play_again_menu()


            

