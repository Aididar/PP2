# Task 1: Mickey Mouse Clock
import pygame
import sys
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
mickey_img = pygame.image.load('mickeyclock.jpeg')
mickey_rect = mickey_img.get_rect(center=(300, 300))

right_hand = pygame.Surface((5, 140), pygame.SRCALPHA)
right_hand.fill((0, 0, 0))
left_hand = pygame.Surface((3, 180), pygame.SRCALPHA)
left_hand.fill((255, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    second_angle = now.second * -6
    minute_angle = now.minute * -6

    screen.fill((255, 255, 255))
    screen.blit(mickey_img, mickey_rect)

    rotated_right_hand = pygame.transform.rotate(right_hand, second_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, minute_angle)

    screen.blit(rotated_right_hand, rotated_right_hand.get_rect(center=mickey_rect.center))
    screen.blit(rotated_left_hand, rotated_left_hand.get_rect(center=mickey_rect.center))

    pygame.display.flip()
    clock.tick(60)
