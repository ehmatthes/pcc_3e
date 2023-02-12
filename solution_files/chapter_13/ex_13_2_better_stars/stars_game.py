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

        current_x, current_y = 2*star_width, 2*star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = 2 * star_width
            current_y += 2 * star_height


    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid."""
        # Add a random offset in each direction.
        new_star = Star(self)
        new_star.rect.x = x_position + self._get_star_offset()
        new_star.rect.y = y_position + self._get_star_offset()

        self.stars.add(new_star)

    def _get_star_offset(self):
        """Return a random adjustment to a star's position."""
        offset_size = 15
        return randint(-1*offset_size, offset_size)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sg = StarsGame()
    sg.run_game()
