import sys

import pygame

from settings import settings
from ship import Ship

class AlienInvasion:
    """Overall Class to manage game assests and the behivor,"""
    def __init__(self):
        """Initilize The Game and Create the game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = settings()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")

        self.ship = Ship(self)

    def run_game(self):
        "Start the main loop for the game."
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
       
            self.clock.tick(60)

    def _check_events(self):
        #respond to events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
            

    def _update_screen(self):
        """updating images on the screen """
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
            #Make most recently drawn screen visible."
        pygame.display.flip()

if __name__ == "__main__":
    #MAke a game instance and run the game
    ai=AlienInvasion()
    ai.run_game()
