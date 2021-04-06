import random
from Blob import Blob
from constants import GREEN

class GreenBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(GREEN, x_boundary, y_boundary)
    self.size = 20
  
  def move(self, stay_within_bounds=True):
    self.x += random.randrange(-4, 5)
    self.y += random.randrange(-4, 5)
    if stay_within_bounds:
      self.check_bounds()