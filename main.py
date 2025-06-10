# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    c = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    af = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    while 1:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  return
        
        dt = c.tick(60)/1000
        screen.fill((0, 0, 0))
        updateable.update(dt)
        for a in asteroids:
             for s in shots:
                  if s.collision_check(a):
                       a.split()
             if p.collision_check(a):
                  print("Game over!")
                  pygame.quit()
                  quit()
        for d in drawable:
             d.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
        main()
