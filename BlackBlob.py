import random
from Blob import Blob
from constants import BLACK

class BlackBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(BLACK, x_boundary, y_boundary)


  def move(self, stay_within_bounds=True):
    self.x += random.randrange(-4, 5)
    self.y += random.randrange(-4, 5)
    if stay_within_bounds:
      self.check_bounds()