
import math
import pygame

from constants import WIDTH, WHITE, HEIGHT, STARTING_BLACK_BLOBS, STARTING_BLUE_BLOBS, STARTING_GREEN_BLOBS, GREY, GREEN, BLUE
from BlueBlob import BlueBlob
from GreenBlob import GreenBlob
from BlackBlob import BlackBlob




game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob Loblaw's Loblaw Law Blobs")
clock = pygame.time.Clock()



def is_touching(b1, b2):
  return math.sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2) < (b1.size + b2.size)
  print(math.sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2) < (b1.size + b2.size))

def handle_collisions(blob_list):
  blues, greens, black = blob_list
  for black_id, black_blob in black.copy().items():
      for other_blobs in blues, greens:
          for other_blob_id, other_blob in other_blobs.copy().items():
              if black_blob == other_blob:
                  pass
              else:
                  if is_touching(black_blob, other_blob):
                    eat_blobs(black_blob, other_blob)
                    
                    if other_blob.size <= 0:
                      del other_blobs[other_blob_id]
                    if black_blob.size == 0:
                      pygame.quit()

                                   
  return blues, greens, black

def eat_blobs(black_blob, other_blob):
  if other_blob.color == GREEN:
    black_blob.size += 1
    other_blob.size -= 1

  elif other_blob.color == BLUE:
    black_blob.size -= 1
    other_blob.size += 1

def draw_environment(blob_list):
    game_display.fill(GREY)
    blues, black, green = handle_collisions(blob_list)
    for blob_dict in blob_list:
      for blob_id in blob_dict: 
        blob = blob_dict[blob_id]
        blob.draw_self(game_display)
        blob.move()


    pygame.display.update()

  

def main():
  blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
  green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
  black_blobs = dict(enumerate([BlackBlob(WIDTH, HEIGHT) for i in range(STARTING_BLACK_BLOBS)]))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    draw_environment([blue_blobs, green_blobs, black_blobs])
    clock.tick(60)



if __name__ == '__main__':
  main()




