import random
from Blob import Blob
BLACK = (0, 0, 0)

class BlackBlob(Blob):
  def __init__(self, color, x_boundary, y_boundary):
    super().__init__(color, x_boundary, y_boundary)
    self.color = BLACK

  def move_fast(self):
    self.x += random.randrange(-4, 5)
    self.y += random.randrange(-4, 5)