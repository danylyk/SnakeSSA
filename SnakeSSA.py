import pygame
from pygame.locals import *
import os

class App:
    def __init__(self):
        pygame.init()
        window_info = pygame.display.Info()
        w, h = window_info.current_w, window_info.current_h
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (((w/2)-423),((h/2)-292))
        pygame.display.set_caption("Snake SSA")
        self.window = pygame.display.set_mode((846, 584))
        self.bg = pygame.image.load(os.path.join("assets", "bg.png"))
        self.run = True
        
        self.add_button_default = pygame.image.load(os.path.join("assets", "add.png"))
        self.add_button_hover = pygame.image.load(os.path.join("assets", "add_hover.png"))
        self.add_button = self.add_button_default
        self.add_button_rect = self.add_button.get_rect()
        self.add_button_rect.x, self.add_button_rect.y = 98,12

        self.play_button_default = pygame.image.load(os.path.join("assets", "play.png"))
        self.play_button_hover = pygame.image.load(os.path.join("assets", "play_hover.png"))
        self.play_button = self.play_button_default
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x, self.play_button_rect.y = 202,16

        self.fps = 17 # 1000/60 - 60 fps
        self.__Run()

    def __Run(self):
        while self.run:
            pygame.time.delay(self.fps)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False
            if self.add_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.add_button = self.add_button_hover
            else:
                self.add_button = self.add_button_default

            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                self.play_button = self.play_button_hover
            else:
                self.play_button = self.play_button_default

            self.__Draw()
            pygame.display.update()
        
        pygame.quit()

    def __Draw (self):
        self.window.blit(self.bg, (0,0))
        self.window.blit(self.add_button, (98,12))
        self.window.blit(self.play_button, (202,16))


app = App()