import pygame

class Ship:

    def __init__(self,ai_game):
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottonm of the center
        self.rect.midbottom = self.screen_rect.midbottom

        #Store the decimal values for the ship's hortizentl ppostion 
        self.x = float(self.rect.x)

        #moving flag:start with the ship that is not moving 
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship movement based om the moveent flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
             self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update the rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)