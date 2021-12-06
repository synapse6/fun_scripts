import pygame
from spritesheet import SpriteSheet
from pygame import image   #pip install pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG = (255, 255, 255)
line_width = 1
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
sprite = pygame.image.load('naruto_sheet.png').convert_alpha()
sprite_sheet = SpriteSheet(sprite)
def draw_lines():
   for i in range(0, 600, 50):
        pygame.draw.line(screen, (0, 0 ,0), (i, 0), (i, 600), line_width)

frame0 = sprite_sheet.get_image(0, 36, 36, 2, WHITE)
frame1 = sprite_sheet.get_image(1, 36, 36, 2, WHITE)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(BG)
    screen.blit(frame0, (0, 0))
    screen.blit(frame1, (0, 0))
    pygame.display.update()

pygame.quit()