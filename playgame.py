import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit
from shot import Shot

def play_game(screen):
    asteroid_game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    while True:
        #handle inputs and events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #game logic
        screen.fill((0,0,0))
        for sprite in updatable:
            sprite.update(dt)
            for asteroid in asteroids:
                if asteroid.collision(player): #game over
                    if not game_over_screen(screen):
                        pygame.quit()
                        return False
                    else:
                        print("restarting from play_game...")
                        return True
                for shot in shots:
                    if asteroid.collision(shot):
                        shot.kill()
                        asteroid.split()


        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        #framerate limit
        dt = asteroid_game_clock.tick(60) / 1000

def game_over_screen(screen):
    #"""Display GAME OVER message and ask to play again."""
    # initialize the font
    pygame.font.init()
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 50)

    #Render text surfaces
    game_over_text = font.render('GAME OVER', True, (255,0,0)) #red game over
    play_again_text = small_font.render('Play again? Y/n', True, (255,255,255))

    #get positions (centered)
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    # Display GAME OVER screen
    while True:
        screen.fill((0,0,0))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(play_again_text, play_again_rect)
        pygame.display.flip()

        #handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    print("Restart requested")
                    return True
                elif event.key== pygame.K_n:
                    print("Quit requested")
                    return False
