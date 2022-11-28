import pygame, sys
from button import Button
from jump_game import JumpGame
from settings import Settings


class Main:

    def __init__(self):
        pygame.init()
        self.jump_game = JumpGame()
        self.settings = Settings()

        self.SCREEN = pygame.display.set_mode((self.settings.screen_W, self.settings.screen_H))
        self.screen_rec = self.SCREEN.get_rect()

        self.play_button = pygame.image.load("assets/Play Rect.png")
        self.play_button_rect = self.play_button.get_rect()

        self.center = self.screen_rec.center
        self.mid_top = self.screen_rec.midtop
        self.play_button_rect.midleft = self.screen_rec.midleft

        pygame.display.set_caption("Menu")

        self.BG = pygame.transform.scale(pygame.image.load("assets/space.png"),(self.settings.screen_W, self.settings.screen_H))

        self.PLAY = False

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def play(self):
        self.PLAY = True
        while True:
            self.PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("black")

            self.PLAY_TEXT = self.get_font(45).render("", True, "White")
            self.PLAY_RECT = self.PLAY_TEXT.get_rect(center=(400,400))
            self.SCREEN.blit(self.PLAY_TEXT, self.PLAY_RECT)

            self.topleft = self.screen_rec.topleft
            self.PLAY_BACK = Button(image=None, pos=(self.topleft),
                                    text_input="BACK", font=self.get_font(50), base_color="White",
                                    hovering_color="Green")

            self.PLAY_BACK.changeColor(self.PLAY_MOUSE_POS)
            self.PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.PLAY_BACK.checkForInput(self.PLAY_MOUSE_POS):
                        self.main_menu()

            self.jump_game.run_game()

            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            self.MENU_MOUSE_POS = pygame.mouse.get_pos()

            self.MENU_TEXT = self.get_font(30).render("ROBOT JUMP GAME", True, "#b68f40")
            self.MENU_RECT = self.MENU_TEXT.get_rect(center=(300,20))

            self.PLAY_BUTTON = Button(image=self.play_button, pos=(300,300),
                                      text_input="PLAY", font=self.get_font(30), base_color="#b68f40",
                                      hovering_color="White")

            self.QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(300,500),
                                      text_input="QUIT", font=self.get_font(30), base_color="#ff00d0",
                                      hovering_color="White")

            self.SCREEN.blit(self.MENU_TEXT, self.MENU_RECT)

            for button in [self.PLAY_BUTTON, self.QUIT_BUTTON]:
                button.changeColor(self.MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.PLAY_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                        self.play()

                    if self.QUIT_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def run_game(self):
        while True:
            self.main_menu()
            self.play()


main = Main()
main.run_game()
