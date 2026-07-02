import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
   def  __init__(self, x: float, y: float, radius: float) -> None:
      super().__init__(x, y, radius)

   def draw(self, screen) -> None:
      pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

   def update(self, dt: float) -> None:
      self.position += self.velocity * dt

   def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
         return
      else:
         log_event("asteroid_split")
         split_angle = random.uniform(20,50)
         first_move = self.velocity.rotate(split_angle)
         second_move = self.velocity.rotate(-split_angle)
         new_radius = self.radius - ASTEROID_MIN_RADIUS
         first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
         second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
         first_asteroid.velocity = first_move * 1.2
         second_asteroid.velocity = second_move * 1.2
