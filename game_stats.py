class GameStats:
    """trace statistics for alien Invasion"""

    def __init__(self,ai_game):
        """intilize statics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game.."""
        self.ship_left = self.settings.ship_limit
    