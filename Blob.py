import pygame
import random
import math


class Blob:
  
  def __init__(self, color, x_boundary, y_boundary, size_range=(4,8), movement_range=(-1, 2)):
    self.color = color 
    self.size = random.randrange(size_range[0], size_range[1])
    self.x_boundary = x_boundary
    self.y_boundary = y_boundary
    self.x = random.randrange(0, self.x_boundary)
    self.y = random.randrange(0, self.y_boundary)
    self.movement_range = movement_range

  def draw_self(self, game_display):
    pygame.draw.circle(game_display, self.color, [self.x, self.y], self.size)



  def check_bounds(self):
    if self.x < 0: 
      self.x = 0 
    elif self.x > self.x_boundary - self.size: 
      self.x = self.x_boundary - self.size
    if self.y < 0: 
      self.y = 0
    elif self.y > self.y_boundary - self.size: 
      self.y = self.y_boundary - self.size
    


  def move(self, stay_within_bounds=True):
    self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
    self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
    self.x += self.move_x
    self.y += self.move_y

    if stay_within_bounds:
      self.check_bounds()

  # def is_touching(self, other_blob):
  #   return math.sqrt((other_blob.x-self.x)**2 + (other_blob.y-self.y)**2) < (self.size + other_blob.size)
  #   print(math.sqrt((other_blob.x-self.x)**2 + (other_blob.y-self.y)**2) < (self.size + other_blob.size))

  # def handle_collisions(blob_list):
  #   blues, reds, greens = blob_list
  #   for blue_id, blue_blob in blues.copy().items():
  #       for other_blobs in blues, reds, greens:
  #           for other_blob_id, other_blob in other_blobs.copy().items():
  #               if blue_blob == other_blob:
  #                   pass
  #               else:
  #                   if is_touching(blue_blob, other_blob):
  #                     #insert collision event here
                            
  #   return blues, reds, greens


