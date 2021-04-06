import random
from Blob import Blob
GREEN = (0, 255, 0)

class GreenBlob(Blob):
  def __init__(self, color, x_boundary, y_boundary):
    super().__init__(color, x_boundary, y_boundary)
    self.color = GREEN
    self.size = 20
  
  def move_fast(self):
    self.x += random.randrange(-4, 5)
    self.y += random.randrange(-4, 5)