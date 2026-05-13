from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rng = random.uniform(20, 50)
        first_split_vector = self.velocity.rotate(rng)
        second_split_vector = self.velocity.rotate(-rng)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid = Asteroid(self.position[0], self.position [1], new_radius)
        first_asteroid.velocity = first_split_vector * 1.2
        second_asteroid.velocity = second_split_vector * 1.2

