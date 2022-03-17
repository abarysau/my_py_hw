# HOME WORK 7.0

print('\n----------------\nHOME WORK 7.0\n----------------\n')


print('\nMy PyGame program\n')

# my modules

import pygame


# my program

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render('Welcome to PyGame', True, (127, 255, 255))
text_center = ((width - text.get_width()) // 2, text.get_height())
screen.blit(text, text_center)
pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
pygame.display.quit()

print('\nBye')    




           
