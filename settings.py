class settings:
    """A class that store all the setting of the game"""

    def __init__(self):
        '''Intilze the game settings for the allian ivasion.'''
        #SCREEN SETTINGS
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230 ,230 ,230)
        self.ship_speed = 1.5
        #bullet settings 

        self.bullet_speed = 4.0 
        self.bullet_width = 2
        self.bullet_height = 8
        self.bullet_color = (130,60,40)
        self.bullets_allowed = 3