import pygame
import sys
import datetime

pygame.init()

# Set window dimensions to 1000x1000
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mickey Clock")

# For controlling the frame rate
fps_clock = pygame.time.Clock()


bg = pygame.image.load("main-clock.png").convert_alpha()
right_hand = pygame.image.load("right-hand.png").convert_alpha()  # minutes hand (Mickey's right hand)
left_hand = pygame.image.load("left-hand.png").convert_alpha()    # seconds hand (Mickey's left hand)

# Optionally, scale the clock face to better fit the window (e.g., 800x800)
bg = pygame.transform.scale(bg, (800, 800))
# Center of the window
center_x, center_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
bg_rect = bg.get_rect(center=(center_x, center_y))

def rotate_image(image, angle, pivot):
    """
    Rotate an image around a pivot point.

    :param image: Surface to rotate.
    :param angle: Rotation angle in degrees.
    :param pivot: (x, y) pivot point for rotation.
    :return: (rotated_image, rotated_rect)
    """
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rotated_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current system time
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    # Adjust for images drawn with default pointing right:
    # 12 o'clock should be 90° relative to an image that points right.
    minute_angle = 90 - (minutes * 6)   # Correct rotation for minute hand
    second_angle = 90 - (seconds * 6)     # Correct rotation for second hand

    # Rotate the hand images using the adjusted angles
    rotated_right_hand, right_hand_rect = rotate_image(right_hand, minute_angle, (center_x, center_y))
    rotated_left_hand, left_hand_rect   = rotate_image(left_hand, second_angle, (center_x, center_y))

    # Draw everything on the screen
    screen.fill((255, 255, 255))    # White background
    screen.blit(bg, bg_rect)        # Draw the centered clock face
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)

    pygame.display.flip()           # Update display
    fps_clock.tick(30)              # Limit to 30 FPS