import pygame.font
 
class Button:
 
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Support a base color and a highlighted color.
        self.base_color = (0, 135, 0)
        self.highlighted_color = (0, 65, 0)
        # Store the message so we can call _prep_msg() when 
        #   the button color changes.
        self.msg = msg
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = self.base_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped initially.
        self._prep_msg()

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _update_msg_position(self):
        """If the button has been moved, the text needs to be moved as well."""
        self.msg_image_rect.center = self.rect.center

    def set_highlighted_color(self):
        """Set the button to the highlighted color."""
        self.button_color = self.highlighted_color
        self._prep_msg()

    def set_base_color(self):
        """Set the button to the base color."""
        self.button_color = self.base_color
        self._prep_msg()

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)