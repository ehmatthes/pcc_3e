import pygame
 
class Target:
    """A class to manage the target."""

    def __init__(self, ss_game):
        """Create a target object."""
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = ss_game.settings
        self.color = self.settings.target_color

        # Create a target rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
            self.settings.target_height)
        self.center_target()

        # Positive direction is moving down, negative is moving up.
        self.direction = 1

    def update(self):
        """Move the target steadily up and down."""
        # Update the decimal position of the target.
        self.y += self.direction * self.settings.target_speed

        if self.rect.top < 0:
            # It's moved past the top of the screen. Place at top of screen,
            #   and change direction.
            self.rect.top = 0
            self.direction = 1
        elif self.rect.bottom > self.screen_rect.bottom:
            # Place at bottom, and change direction.
            self.rect.bottom = self.screen_rect.bottom
            self.direction = -1

        # Update the rect position.
        self.rect.y = self.y

    def center_target(self):
        """Center the target on the right side of the screen."""
        self.rect.midright = self.screen_rect.midright
        
        # Store the target's position as a decimal value.
        self.y = float(self.rect.y)

    def draw_target(self):
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
