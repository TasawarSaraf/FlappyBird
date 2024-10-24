import pygame
import sys
from settings import window, clock, bird_color, bird_radius, window_height, gravity, jump_strength, pipe_speed, pipe_gap
from bird import Bird
from pipes import generate_pipes, Pipe
from utils import reset_game, game_over

pygame.init()

# Initialize the bird and pipes
bird = Bird()
pipe_list = [generate_pipes()]
score = 0
game_over_flag = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update bird and pipe positions
    bird.update()
    
    # Move pipes
    for pipe_pair in pipe_list:
        pipe_pair[0].rect.x -= pipe_speed
        pipe_pair[1].rect.x -= pipe_speed

    # Remove off-screen pipes
    pipe_list = [pipe_pair for pipe_pair in pipe_list if pipe_pair[0].rect.x + pipe_pair[0].width > 0]

    # Add new pipes
    if pipe_list[-1][0].rect.x < window.get_width() - 300:
        pipe_list.append(generate_pipes())

    # Check for collisions
    bird_rect = pygame.Rect(bird.x - bird_radius, bird.y - bird_radius, bird_radius * 2, bird_radius * 2)
    for pipe_pair in pipe_list:
        if bird_rect.colliderect(pipe_pair[0].rect) or bird_rect.colliderect(pipe_pair[1].rect):
            game_over(bird, pipe_list, score)

    # Check if bird passes the pipes and increase score
    for pipe_pair in pipe_list:
        if pipe_pair[0].rect.x + pipe_pair[0].width < bird.x and not pipe_pair[0].passed:
            score += 1
            pipe_pair[0].passed = True

    # Drawing section
    window.fill((202, 244, 255))
    bird.draw(window)

    for pipe_pair in pipe_list:
        pygame.draw.rect(window, pipe_pair[0].color, pipe_pair[0].rect)
        pygame.draw.rect(window, pipe_pair[1].color, pipe_pair[1].rect)

    score_text = pygame.font.Font(None, 36).render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
