class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0
        # Start Alien Invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can chane during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
