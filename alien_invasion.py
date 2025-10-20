import sys
from time import sleep


import pygame

from settings import settings

from game_stats import GameStats

from ship import Ship
from alien import Alien

from bullet import Bullet

class AlienInvasion:
    """Overall Class to manage game assests and the behivor,"""
    def __init__(self):
        """Initilize The Game and Create the game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = settings()

        self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("ALIEN INVASION")

        #Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    def run_game(self):
        "Start the main loop for the game."
        while True:
            self._check_events()
            self.ship.update()
            #self.bullets.update()
            self._update_bullets()
            self._update_aliens()

            self._update_screen()
    
       
            self.clock.tick(60)

    def _check_events(self):
        #respond to events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

                
               
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

             
    def _check_keydown_events(self,event):
        """pespond to the key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 

        elif event.key == pygame.K_q:
            sys.exit()

        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 

    def _check_keyup_events(self,event):
         """Respond to key releases"""

         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

                
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Craete anew bulllet and add it to a new bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        self.bullets.update()
         
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to the bullets-alien collision"""

        #Remove any bullet and aliens that have collided.

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens , True , True)
        
        if not self.aliens:
            #Destroy the existing bullets and create new fleet.

            self.bullets.empty()
            self._create_fleet()

        
        

        
    def _update_aliens(self):
        """check if the fleet is at end ,then update the directioms"""
        self._check_fleet_edges()
        self.aliens.update()

        """on alien and ship hit"""

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            print("Our Ship Got it...!!!")


    def _create_fleet(self):

        """fleet of alien"""
        #make a alien
        #Creating an alien and keeping adding aliens until there is no space left
        #space between aliens is one alian width and one alien height


        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x , current_y = alien_width , alien_height

        while(current_y < (self.settings.screen_height  - 3 * alien_height)):

            while (current_x < self.settings.screen_width -3 * alien_width):

                self._create_alien(current_x,current_y)
                current_x+= 2 * alien_width

            current_x = alien_width

            current_y += 2 * alien_height


    def _create_alien(self,x_position,y_position):

            """Creating an akien and palce it in the row """

            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """Respond appropriately if any alien have reached an edge"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):

        """drop an entire fleet and change the fleets direction"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by the alien"""

        #Decrement ships_left

        self.stats.ship_left -=1
        #get rid of any remaining bullets and aliens

        self.bullets.empty()
        self.aliens.empty()

        #Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()
        #pause for moment
        sleep(0.5)
           


    def _update_screen(self):
        """updating images on the screen """
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        self.aliens.draw(self.screen)
            #Make most recently drawn screen visible."
        pygame.display.flip()

if __name__ == "__main__":
    #MAke a game instance and run the game
    ai=AlienInvasion()
    ai.run_game()
