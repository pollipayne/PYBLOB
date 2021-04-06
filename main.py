

import pygame


from BlueBlob import BlueBlob
from GreenBlob import GreenBlob
from BlackBlob import BlackBlob


WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

STARTING_BLUE_BLOBS = 6
STARTING_GREEN_BLOBS = 5
STARTING_BLACK_BLOBS = 5

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()









def draw_environment(blob_list):
  game_display.fill(WHITE)
  for blob_dict in blob_list:
    for blob_id in blob_dict: 
      blob = blob_dict[blob_id]
      pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
      blob.check_bounds()
      blob.move_fast()

 
  pygame.display.update()
  

def main():
  blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
  green_blobs = dict(enumerate([GreenBlob(GREEN, WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
  black_blobs = dict(enumerate([BlackBlob(BLACK, WIDTH, HEIGHT) for i in range(STARTING_BLACK_BLOBS)]))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    draw_environment([blue_blobs, green_blobs, black_blobs])
    clock.tick(60)

if __name__ == '__main__':
  main()




