import sys

import pygame

from settings import settings

class AlienInvasion:
    """Overall Class to manage game assests and the behivor,"""
    def __init__(self):
        """Initilize The Game and Create the game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = settings()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Aliem Invasion")
        #set the background color

    def run_game(self):
        "Start the main loop for the game."
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            #Redraw the screen During eah pass through the loop.
            self.screen.fill(self.settings.bg_color)
            #Make most recently drawn screen visible."
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    #MAke a game instance and run the game
    ai=AlienInvasion()
    ai.run_game()
