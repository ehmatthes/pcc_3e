import sys
from random import randint

import pygame

from settings import Settings
from star import Star


class StarsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """Create a sky full of stars."""
        # Create a star and keep adding stars until there's no room left.
        #   Spacing between stars is two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size

        x_max = self.settings.screen_width - star_width
        y_max = self.settings.screen_height - star_height
        for _ in range(500):
            x_position = randint(star_width, x_max)
            y_position = randint(star_height, y_max)
            self._create_star(x_position, y_position)

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid."""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position

        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sg = StarsGame()
    sg.run_game()
