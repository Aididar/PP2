import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

running = True
drawing = False
color = (0, 0, 0)
tool = "rect"
size = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "erase"
            elif event.key == pygame.K_1:
                color = (255, 0, 0)
            elif event.key == pygame.K_2:
                color = (0, 255, 0)
            elif event.key == pygame.K_3:
                color = (0, 0, 255)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        
        if drawing:
            x, y = pygame.mouse.get_pos()
            if tool == "rect":
                pygame.draw.rect(screen, color, (x - size//2, y - size//2, size, size))
            elif tool == "circle":
                pygame.draw.circle(screen, color, (x, y), size//2)
            elif tool == "erase":
                pygame.draw.rect(screen, (255, 255, 255), (x - size//2, y - size//2, size, size))

    pygame.display.flip()

pygame.quit()
