import sys
from bird import Bird
from pipes import generate_pipes
from settings import window, clock
import pygame

def reset_game():
    # you reintialize the bird 
    # you regenerate the pipes
    # you reset the scores
    # and game_over_flag reset to false
    global pipe_list, score, game_over_flag
    bird = Bird()
    pipe_list = [generate_pipes()]
    score = 0
    game_over_flag = False

def game_over(bird, pipe_list, score):
    game_over_flag = True
    font = pygame.font.Font(None, 36)
    reset_button = pygame.Rect(window.get_width() // 2 - 50, window.get_height() // 2 + 20, 100, 50)

    while game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the user presses down anywhere on the rect of the reset button you hit the reset_game() function
                if reset_button.collidepoint(event.pos):
                    reset_game()

        window.fill((0, 0, 0))
        game_over_text = font.render(f'Game Over! Score: {score}', True, (255, 255, 255))
        window.blit(game_over_text, (window.get_width() // 2 - game_over_text.get_width() // 2, window.get_height() // 2 - 50))

        pygame.draw.rect(window, (255, 0, 0), reset_button)
        reset_text = font.render('Reset', True, (255, 255, 255))
        window.blit(reset_text, (reset_button.x + reset_button.width // 2 - reset_text.get_width() // 2, reset_button.y + reset_button.height // 2 - reset_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)
