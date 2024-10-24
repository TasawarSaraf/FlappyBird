import pygame

# Window setup
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Bird')

# Clock setup
clock = pygame.time.Clock()

# Bird settings
bird_radius = 20
bird_color = (255, 166, 47)

# Pipe settings
pipe_width = 80
pipe_height = 450
pipe_gap = 200
pipe_speed = 5
pipe_color = (64, 165, 120)

# Game mechanics
gravity = 0.5
jump_strength = -10
