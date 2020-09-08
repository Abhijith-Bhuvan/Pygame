import pygame


def update_screen(rec_properties, rec_color='Blue'):
    colors = {'Blue': (0, 0, 255), 'Red': (255, 0, 0), 'Green': (0, 255, 0)}
    bgcolor = (0, 0, 0)

    x, y, width, hight = rec_properties

    screen.fill(bgcolor)
    pygame.draw.rect(screen, colors[rec_color],
                     pygame.Rect(x, y, width, hight))


def run_game():

    done = False
    clock = pygame.time.Clock()

    x = 50    # The x coordinate of top-left corner
    y = 50    # The y coordinate of top-left corner
    width = 100     # The width of the rectangle
    hight = 75      # The higth of the rectangle

    rec_color = 'Blue'

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

        KeyPressed = pygame.key.get_pressed()
        if KeyPressed[pygame.K_UP]:
            y -= 3
        if KeyPressed[pygame.K_DOWN]:
            y += 3
        if KeyPressed[pygame.K_LEFT]:
            x -= 3
        if KeyPressed[pygame.K_RIGHT]:
            x += 3
        if KeyPressed[pygame.K_b]:
            rec_color = 'Blue'
        if KeyPressed[pygame.K_r]:
            rec_color = 'Red'
        if KeyPressed[pygame.K_g]:
            rec_color = 'Green'

        rec_properties = [x, y, width, hight]
        update_screen(rec_properties, rec_color)

        pygame.display.flip()       # Needed for uppdates to take place
        clock.tick(120)     # Frames per second


if '__main__' == __name__:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    run_game()
    pygame.quit()
