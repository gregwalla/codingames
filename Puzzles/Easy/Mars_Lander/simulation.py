import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
WINDOW_SIZE = (700, 700)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mars Lander")

# Define function to draw surface
def draw_surface(surface_points):
    for i in range(len(surface_points) - 1):
        pygame.draw.line(screen, WHITE, surface_points[i], surface_points[i + 1], 2)

# Function to draw the lander
def draw_lander(x, y):
    lander_rect = pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(screen, WHITE, lander_rect)

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface_points = []
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    surface_points.append((land_x, land_y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw surface
    draw_surface(surface_points)

    # Read lander data
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Draw lander
    draw_lander(x, y)

    # Update the display
    pygame.display.flip()

pygame.quit()
