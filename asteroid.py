from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        a = random.uniform(20, 50)
        v1 = self.velocity.rotate(a)
        v2 = self.velocity.rotate(-a)
        r = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, r)
        a2 = Asteroid(self.position.x, self.position.y, r)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt