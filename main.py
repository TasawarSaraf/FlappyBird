from cmath import pi
import pygame 
import sys
import random 


pygame.init()

# this is the window setup for the game
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Bird')


#Set up the clock for decent framerate

clock = pygame.time.Clock()

#Bird properites

#rgb(172, 215, 147) for nice green 

bird_color = (255, 166, 47)
bird_radius = 20
bird_x = bird_radius * 4
bird_y = window_height // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -10 # it will only go up by 10 up


# we then create general pipe for the flappy bird not to hit 
pipe_width = 80
pipe_height = 450
pipe_color = (64, 165, 120)
pipe_gap = 200 # always enough for the flappy bird to squeeze in
pipe_speed = 5 # the speed it is coming towards the bird to create the illusion the bird is moving


#pipe list
pipe_list = []

#Scores
score = 0 #default is 0
font = pygame.font.Font(None, 36)


class Pipe:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x,y,width, height)
        self.passed = False

reset_button = pygame.Rect(window_width // 2 - 50, window_height // 2 + 20, 100, 50)

def generate_pipes():
    gap_start = random.randint(100, window_height - pipe_gap - 50)
    # it starts from the end of the screen 
    top_pipe = Pipe(window_width, gap_start - pipe_height, pipe_width, pipe_height)
    bottom_pipe = Pipe(window_width, gap_start + pipe_gap, pipe_width, pipe_height)
    # you want to return these two randomly generated pipes for both the bottom and top 
    # the randomly generated will randomize the gap size when menuvering through the obstacles
    return top_pipe, bottom_pipe

#Main game loop that will always run 

# it will append a newly generated top_pipe and bottom_pipe
pipe_list.append(generate_pipes())

def reset_game():
    global bird_x, bird_y, bird_velocity, pipe_list, score, game_over_flag
    bird_x = bird_radius * 4
    bird_y = window_height // 2
    bird_velocity = 0
    # reset the score
    score = 0
    # clear the list
    pipe_list.clear()
    # and regenerate the pipe_list when it comes through
    pipe_list = [generate_pipes()]
    game_over_flag = False


def game_over():
    global game_over_flag
    game_over_flag = True

    # if the game over flag is true only then run this while condition
    while game_over_flag:
        for event in pygame.event.get():
            # this should always be the condition
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # meaning you mousedown clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the mousedown is on the poisition of the reset button
                if reset_button.collidepoint(event.pos):
                    reset_game()
        
        # in this while loop draw this screen that will display the score and the reset button
        window.fill((0,0,0))

        game_over_text = font.render(f'Game Over! Score: {score}', True, (255,255,255))
        # now draw it within the window
        window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - 50))

        # draw the reset button
        pygame.draw.rect(window, (255, 0, 0), reset_button)
        reset_text = font.render('Reset', True, (255, 255, 255))
        window.blit(reset_text, (reset_button.x + reset_button.width // 2 - reset_text.get_width() // 2, reset_button.y + reset_button.height // 2 - reset_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

running = True
game_over_flag = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #exit out of the loop
            running = False 
        if event.type == pygame.KEYDOWN:
            # now we need to see which key is being pressed down
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength # the velocity will go by -10

    #no matter what unless if it is pressing down on space you apply gravity to bring it down (because of gravity)
    bird_velocity += gravity
    bird_y += bird_velocity

    # check the condition so it doesn't fall off the screen from the bottom 
    if bird_y > window_height - bird_radius:
        bird_y = window_height - bird_radius
        bird_velocity = 0
    # if it goes above the screen set it to the edge of the screen if the user keeps pressing up to go off the screen 
    if bird_y < bird_radius:
        bird_y = bird_radius
        bird_velocity = 0

    # now to create the illusion the flpapy bird is moving 
    for pipe in pipe_list:
        # it goes at the speed of -5
        pipe[0].rect.x -= pipe_speed
        pipe[1].rect.x -= pipe_speed


    # remove the pipes once they go off screen (need to figure out what this does)
    pipe_list = [pipe for pipe in pipe_list if pipe[0].rect.x + pipe_width > 0]

    # and once removed you append the new pipes
    if pipe_list and pipe_list[-1][0].rect.x < window_width - 300:
        pipe_list.append(generate_pipes())


    #now we are going to check for collisions

    #frame collision for the flappy bird 
    bird_collision_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)

    for pipe in pipe_list:
        if bird_collision_rect.colliderect(pipe[0].rect) or bird_collision_rect.colliderect(pipe[1].rect):
            # go to the game over function instead
            game_over()


    #check if it passes through the pipe with no collision and increment the score
    for pipe in pipe_list:
        if pipe[0].rect.x + pipe_width < bird_x and not pipe[0].passed:
            score += 1 
            pipe[0].passed = True
            pipe[1].passed = True
  

    #rgb(202, 244, 255)
    window.fill((202, 244, 255)) 

    pygame.draw.circle(window, bird_color, (bird_x, bird_y), bird_radius)

    #now draw the pipes 
    for pipe in pipe_list:
        # make sure you draw the rect not the entire pipe object
        pygame.draw.rect(window, pipe_color, pipe[0].rect)
        pygame.draw.rect(window, pipe_color, pipe[1].rect)


    # Draw the score (before updating the window)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    #update the window 
    pygame.display.flip()

    #Set the framwerate to 60 
    clock.tick(60)

#Rememebr the entire game runs on that main loop so once you are done you quit

pygame.quit()
sys.quit()






