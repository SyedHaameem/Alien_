import pygame

from pygame.sprite import Sprite


class Alien(Sprite):


    def __init__(self, ai_game):

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start each new alien at the top left 


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the exactt horizntal postiom of the alien 

        self.x = float(self.rect.x)

    def update(self):
        """Mpve the alian to the right."""

        self.x += self.settings.alien_speed
        self.rect.x = self.x