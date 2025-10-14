class settings:
    """A class that store all the setting of the game"""

    def __init__(self):
        '''Intilze the game settings for the allian ivasion.'''
        #SCREEN SETTINGS
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250 ,250 ,250)
        self.ship_speed = 1.5
        #bullet settings 

        self.bullet_speed = 2.5 
        self.bullet_width = 2
        self.bullet_height = 8
        self.bullet_color = (130,60,40)
        self.bullets_allowed = 3

        #alien speed 

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction 1 represents right and the -1 represents left.
        self.fleet_direction = 1