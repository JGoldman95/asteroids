# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit
from shot import Shot
from playgame import *

def main():
    os.environ['SDL_VIDEO_CENTERED'] = "1"

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        should_restart = play_game(screen) #play the game
        print(f"play_game() returned: {should_restart}")
        if not should_restart: #if game_over_screen() returned false, exit
            print("Breaking out of man loop. Exiting...")
            break

    print("Thanks for playing.")
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
