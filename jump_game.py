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
from duck import Duck
from pygame import mixer
from wall import Wall


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
        self.duck = Duck()
        self.wall = Wall()


        self.background_music = mixer.music.load("assets/Electronic-background-music-90-bpm.wav")
        self.background_noise = mixer.music.set_volume(0.7)
        mixer.music.play()

        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.tucan,self.bear, self.person, self.moose, self.owl, self.duck, self.wall)

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

            self.timer += 1
            print(self.settings.robot_health)
            if self.settings.robot_health <= 0:
                while True:

                    pygame.display.update()
                    self.gametext.play_again_menu()
                    self.score()
                    if self.gametext.restart:
                        self.playagain()
                        pygame.display.update()
                        break

                    if self.gametext.quit:
                        break
            clock.tick(60)

    def update_screen(self):
        self.person.screen.fill((0, 0, 0))
        self.health_Bar()
        self.time()
        self.game_objects.update()
        self.game_objects.draw(self.settings.screen)
        pygame.display.flip()

    def collisions(self):
        bear_collision = pygame.sprite.collide_rect(self.bear, self.person)
        moose_collision = pygame.sprite.collide_rect(self.moose, self.person)
        owl_collision = pygame.sprite.collide_rect(self.owl, self.person)
        wall_collision = pygame.sprite.collide_rect(self.wall, self.person)
        tucan_wall = pygame.sprite.collide_rect(self.wall, self.tucan)
        # tucan_collision = pygame.sprite.spritecollide(self.person, self.tucans, False)

        if bear_collision:
            self.settings.robot_health -= 2

            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)

        if moose_collision:
            self.settings.robot_health -= 2
            self.person.rect = self.person.rect

        if owl_collision:
            self.settings.robot_health -= 2
            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)

        if wall_collision:
            if self.person.moving_left:
                self.person.rect.x = self.wall.rect.right
            if self.person.moving_right:
                self.person.rect.x = 100

        if tucan_wall:
            self.settings.tucan_speed= self.settings.tucan_speed * -1

    def time(self):
        font = pygame.font.SysFont('Arial', 20)
        game_time_text = font.render(f"TIME SURVIVED: {self.timer // 60}", True, (200, 200, 200))
        game_time_text_rec = game_time_text.get_rect(
            center=(100, 30))
        self.settings.screen.blit(game_time_text, game_time_text_rec)

    def health_Bar(self):
        pygame.draw.rect(self.settings.screen, (255, 0, 0),
                         (self.person.rect.x, self.person.rect.y + self.person.image.get_height() - 80,
                          self.person.image.get_width(), 10))
        pygame.draw.rect(self.settings.screen, (0, 255, 0), (
            self.person.rect.x, self.person.rect.y + self.person.image.get_height() - 80,
            self.person.image.get_width() * (self.settings.robot_health / 100),
            10))

    #######################################################################################################################
    def score(self):
        font = pygame.font.Font("assets/ChunkFive-Regular.ttf", 30)
        game_time_text = font.render(f"TIME SURVIVED: {self.timer // 60} SECONDS", True, (200, 200, 200))
        game_time_text_rec = game_time_text.get_rect(
            center=(300, 200))
        self.settings.screen.blit(game_time_text, game_time_text_rec)

    #################################################
    def playagain(self):

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
