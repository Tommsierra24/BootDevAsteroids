from constants import SHOT_RADIUS, LINE_WIDTH
import pygame
from circleshape import CircleShape


class Shot(CircleShape):
   def __init__(self, x, y):
      super().__init__(x,y,SHOT_RADIUS)

   def draw(self, screen) -> None:
      pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

   def update(self, dt: float) -> None:
      self.position += self.velocity * dt
