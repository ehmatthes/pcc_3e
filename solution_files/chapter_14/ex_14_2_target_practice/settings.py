class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 12.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Target settings
        self.target_height = 120
        self.target_width = 15
        self.target_color = (180, 60,10)

        self.target_speed = 1.5

        # Overall game dynamics.
        self.miss_limit = 3