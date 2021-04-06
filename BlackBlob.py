import pygame
import random
from Blob import Blob
from constants import BLACK

class BlackBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(BLACK, x_boundary, y_boundary)
    self.size = 20


  def move(self, stay_within_bounds=True):
    move = pygame.mouse.get_rel()
    self.x += move[0]
    self.y += move[1]
    if stay_within_bounds:
      self.check_bounds()

