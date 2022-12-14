import pygame, sys, time
from button import Button
from jump_game import JumpGame
from settings import Settings
from gametext import Gametext
from person import Person
from pygame import mixer


class Main:

    def __init__(self):
        pygame.init()
        mixer.init()
        self.jump_game = JumpGame()
        self.settings = Settings()
        self.gametext = Gametext()
        self.person = Person()



        self.play_button = pygame.image.load("assets/Play Rect.png")
        self.play_button_rect = self.play_button.get_rect()

        self.background = pygame.transform.scale(pygame.image.load("assets/space.png"),
                                                 (self.settings.screen_W, self.settings.screen_H))

        self.background_music = mixer.music.load("assets/Electronic-background-music-90-bpm.wav")
        self.background_noise = mixer.music.set_volume(0.7)
        mixer.music.play()

        self.PLAY = False

    def get_font(self, size):
        return pygame.font.Font("assets/ChunkFive-Regular.ttf", size)

    def play(self):
        self.PLAY = True
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            mixer.music.pause()
            self.jump_game.run_game()

            pygame.display.update()

    def main_menu(self):
        while True:
            self.settings.screen.blit(self.background, (0, 0))

            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = self.get_font(58).render("ROBOT JUMP GAME", True, "#FDFF00")
            menu_rect = menu_text.get_rect(center=(300, 50))

            play_button = Button(image=self.play_button, pos=(300, 300),
                                 text_input="PLAY", font=self.get_font(60), base_color="#00FFFF",
                                 hovering_color="White")

            quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300, 500),
                                 text_input="QUIT", font=self.get_font(60), base_color="#00FFFF",
                                 hovering_color="White")

            self.settings.screen.blit(menu_text, menu_rect)

            for button in [play_button, quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(self.settings.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(menu_mouse_pos):
                        self.play()

                    if quit_button.check_for_input(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


    def run_game(self):
        while True:
            self.main_menu()
            self.play()


main = Main()
main.run_game()
