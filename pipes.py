import pygame
import random
from settings import pipe_width, pipe_height, pipe_gap, pipe_color, window_width, window_height

class Pipe:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.passed = False
        self.color = pipe_color

def generate_pipes():
    gap_start = random.randint(100, window_height - pipe_gap - 50)
    top_pipe = Pipe(window_width, gap_start - pipe_height, pipe_width, pipe_height)
    bottom_pipe = Pipe(window_width, gap_start + pipe_gap, pipe_width, pipe_height)
    return top_pipe, bottom_pipe
