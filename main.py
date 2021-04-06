

import pygame

from constants import WIDTH, WHITE, HEIGHT, STARTING_BLACK_BLOBS, STARTING_BLUE_BLOBS, STARTING_GREEN_BLOBS
from BlueBlob import BlueBlob
from GreenBlob import GreenBlob
from BlackBlob import BlackBlob




game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob Loblaw's Loblaw Law Blobs")
clock = pygame.time.Clock()

def draw_environment(blob_list):
    game_display.fill(WHITE)
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




