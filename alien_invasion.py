import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


# main function
def run_game():
    # intial a game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # the main loop
    while True:

        # watch the keyboard and mouse
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # every loop, redraw the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the plot screen seen
        pygame.display.flip()


# run the game
run_game()


