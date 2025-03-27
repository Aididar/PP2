import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

score = 0
level = 1
speed = 10
food_eaten = 0

font = pygame.font.SysFont('Arial', 24)

def show_score():
    score_surface = font.render(f'Score: {score} Level: {level}', True, (0,0,0))
    screen.blit(score_surface, [10, 10])

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        game_over = True

    if snake_pos in snake_body[1:]:
        game_over = True

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_eaten += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        while food_pos in snake_body:
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True

    if food_eaten >= 3:
        level += 1
        speed += 3
        food_eaten = 0

    screen.fill((255,255,255))

    for pos in snake_body:
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, (255,0,0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    show_score()

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
