import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
done =  False
posX = 400
posY = 400
speed = 100
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if posY > speed:
                posY -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if posY < 750:
                posY += speed  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if posX > speed:
                posX -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if posX < 765:
                posX += speed

    screen.fill((255, 255, 255))
        # circle on surface with color red, on center(400, 400), and with radius 25 
    pygame.draw.circle(screen, (255, 0, 0), (posX, posY), 25)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()