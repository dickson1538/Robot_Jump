import time
import random
import pygame
import sys
from settings import Settings
from person import Person
from platform import Platform
from bear import Bear
from tucan import Tucan
from gametext import Gametext
from moose import Moose
from owl import Owl


class JumpGame:

    def __init__(self):
        self.settings = Settings()
        self.person = Person()
        self.platform = Platform()
        self.bear = Bear()
        self.tucan = Tucan()
        self.gametext = Gametext()
        self.moose = Moose()
        self.owl = Owl()


        self.tucans = pygame.sprite.Group()
        self.tucans.add(self.tucan)
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.bear, self.person,self.tucan , self.moose, self.owl)

        self.background = pygame.transform.scale(pygame.image.load("assets/space.png"),
                                                 (self.settings.screen_W, self.settings.screen_H))
        self.play_button = pygame.image.load("assets/Play Rect.png")
        self.play_button_rect = self.play_button.get_rect()

        self.timer = 0
        self.PLAY_AGAIN = False
        self.restart = False
        self.quit = False

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            # 1) check for user input  2) Update game objects   3) draw screen       4) win loose conditions

            self.update_screen()
            self.collisions()
            self.tucan_army()
            self.timer += 1
            print(self.settings.robot_health)
            if self.settings.robot_health <= 0:
                while True:

                    pygame.display.update()
                    self.gametext.play_again_menu()
                    self.time()
                    self.settings.reset()
                    if self.gametext.restart:
                        self.playagain()
                        self.score()
                        pygame.display.update()
                        break

                    if self.gametext.quit:
                        break
            clock.tick(60)

    def update_screen(self):
        self.person.screen.fill((0, 0, 0))
        self.time()
        self.game_objects.update()
        pygame.display.flip()

    def collisions(self):
        bear_collision = pygame.sprite.collide_rect(self.bear, self.person)
        moose_collision = pygame.sprite.collide_rect(self.moose, self.person)
        owl_collision = pygame.sprite.collide_rect(self.owl,self.person)
        #tucan_collision = pygame.sprite.spritecollide(self.person, self.tucans, False)


        if bear_collision:
            self.settings.robot_health -= 2
            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)

        if moose_collision:
            self.settings.robot_health -= 2
            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)

        if owl_collision:
            self.settings.robot_health -= 2
            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)







    def time(self):
        font = pygame.font.SysFont('Arial', 20)
        game_time_text = font.render(f"TIME SURVIVED: {self.timer // 60}", True, (200, 200, 200))
        game_time_text_rec = game_time_text.get_rect(
            center=(100, 30))
        self.settings.screen.blit(game_time_text, game_time_text_rec)

    def tucan_army(self):
        if len(self.tucans) == 0:
            rand_tucans = random.randint(0, 1)
            if rand_tucans == 1:
                tucan = self.tucan
                self.tucans.append(tucan)
        print(self.tucans)





#######################################################################################################################
    def score(self):
        font = pygame.font.SysFont('Arial', 100)
        game_time_text = font.render(f"TIME SURVIVED: {self.timer // 60}", True, (200, 200, 200))
        game_time_text_rec = game_time_text.get_rect(center=(300,300))
        self.settings.screen.blit(game_time_text, game_time_text_rec)


    def playagain(self):
        self.settings.reset()
        self.person.update()
        self.platform.update()
        self.bear.update()
        self.tucan.update()
        self.moose.update()
        self.owl = Owl()
        self.collisions()
        self.time()
        self.update_screen()
        self.run_game()

