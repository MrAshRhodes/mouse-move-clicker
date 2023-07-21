import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("The 'w' key has been pressed")  # Debug output
                run = False

pygame.quit()
