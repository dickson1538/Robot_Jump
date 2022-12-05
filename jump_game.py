import pygame
import sys
from settings import Settings
from person import Person
from platform import Platform
from bird import Bird
from tucan import Tucan
from gametext import Gametext


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

        self.timer = 0

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
        #collision_tucans = pygame.sprite.spritecollide(self.person, self.tucans, True)

        platform_collision = pygame.sprite.collide_rect(self.platform, self.person)


        if owl_collision:
            self.settings.robot_health -= 2
            if self.settings.robot_health >= 0:
                print(self.settings.robot_health)

        if pygame.sprite.spritecollide(self.person, self.tucans, True):
            print("hit")

        if platform_collision:
            print("Hit hit hit hit hit hit hit hit hit hit hit")

    def time(self):
        font = pygame.font.SysFont('Arial', 20)
        game_time_text = font.render(f"TIME SURVIVED: {self.timer // 60}", True, (200, 200, 200))
        game_time_text_rec = game_time_text.get_rect(
            center=(100, 30))
        self.settings.screen.blit(game_time_text, game_time_text_rec)

    def tucan_army(self):
        number_t = 5
        i = 0
        if i <= number_t:
            new_tucan = Tucan()
            self.tucans.add(new_tucan)
            self.game_objects.add(new_tucan)
            i+=1
        print(i)
