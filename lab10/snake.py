import psycopg2
import pygame
import random

def main():
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5433",
            dbname="phonebook_db",
            user="postgres",
            password="Aididar110906$"
        )


    except Exception as e:
        print("Failed to connect to the database:", e)
        return
    cur = conn.cursor()

    # Prompt for username
    username = input("Enter your username: ")

    # Check if user exists
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        user_id = result[0]
        # Retrieve the user's level from the latest entry in user_score
        cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
        res2 = cur.fetchone()
        if res2:
            level = res2[0]
        else:
            level = 1
    else:
        # Insert a new user with default level 1
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        level = 1

    # Set snake speed (frames per second) based on the level
    if level <= 1:
        fps = 5    # slow
    elif level == 2:
        fps = 10   # medium
    else:
        fps = 15   # fast

    # Initialize Pygame
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    # Define colors
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    block_size = 20

    # Initialize snake at the center of the screen
    start_x = (width // 2) // block_size * block_size
    start_y = (height // 2) // block_size * block_size
    # Start with a snake of length 3 moving to the right
    snake = [
        [start_x, start_y],
        [start_x - block_size, start_y],
        [start_x - 2 * block_size, start_y]
    ]
    dx = block_size  # initial movement on x-axis (moving right)
    dy = 0           # initial movement on y-axis

    # Place the first food at a random position not on the snake
    food_x = random.randrange(0, width, block_size)
    food_y = random.randrange(0, height, block_size)
    while [food_x, food_y] in snake:
        food_x = random.randrange(0, width, block_size)
        food_y = random.randrange(0, height, block_size)

    score = 0
    clock = pygame.time.Clock()
    game_over = False
    state = None  # will hold 'paused' or 'game_over'

    # Game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = 'game_over'  # treat window close as game over
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -block_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = block_size
                elif event.key == pygame.K_p:
                    state = 'paused'
                    game_over = True
                    print("Paused")
        if game_over:
            break

        # Move the snake: add a new head
        new_x = snake[0][0] + dx
        new_y = snake[0][1] + dy
        snake.insert(0, [new_x, new_y])

        # Check for collisions with walls or self
        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            state = 'game_over'
            game_over = True
        elif [new_x, new_y] in snake[1:]:
            state = 'game_over'
            game_over = True
        if game_over:
            break

        # Check if food is eaten
        if new_x == food_x and new_y == food_y:
            score += 1
            # Increase level (and speed) when reaching score thresholds
            if level == 1 and score >= 5:
                level = 2
                fps = 10
            elif level == 2 and score >= 10:
                level = 3
                fps = 15
            # Generate a new food location
            food_x = random.randrange(0, width, block_size)
            food_y = random.randrange(0, height, block_size)
            while [food_x, food_y] in snake:
                food_x = random.randrange(0, width, block_size)
                food_y = random.randrange(0, height, block_size)
            # (Snake grows: do not remove tail)
        else:
            # Move snake forward: remove the last segment
            snake.pop()

        # Draw the game objects
        screen.fill(black)
        pygame.draw.rect(screen, red, (food_x, food_y, block_size, block_size))  # food
        for segment in snake:
            pygame.draw.rect(screen, green, (segment[0], segment[1], block_size, block_size))  # snake body
        pygame.display.flip()
        clock.tick(fps)

    # Game over or paused; save score and level to database
    if state:
        cur.execute(
            "INSERT INTO user_score (user_id, level, score, state) VALUES (%s, %s, %s, %s)",
            (user_id, level, score, state)
        )
        conn.commit()
    if state == 'game_over':
        print("Game Over. Final score:", score)

    # Clean up
    cur.close()
    conn.close()
    pygame.quit()

if __name__ == "__main__":
    main()
