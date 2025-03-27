import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

road = pygame.Rect(0, 0, 400, 600)
player = pygame.Rect(180, 500, 40, 60)
coin = pygame.Rect(random.randint(40, 360), -30, 20, 20)

score = 0
font = pygame.font.SysFont("Arial", 24)
speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < 400:
        player.x += 5

    coin.y += speed
    if coin.y > 600:
        coin.y = -30
        coin.x = random.randint(40, 360)

    if player.colliderect(coin):
        score += 1
        coin.y = -30
        coin.x = random.randint(40, 360)

    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (100, 100, 100), road)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.ellipse(screen, (255, 215, 0), coin)

    score_text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_text, (280, 10))

    pygame.display.flip()
    clock.tick(60)
