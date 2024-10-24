from settings import window_height, bird_radius, bird_color, gravity

class Bird:
    def __init__(self):
        self.x = bird_radius * 4   
        self.y = window_height // 2 # starts in the middle of the y axis
        self.velocity = 0

    def jump(self):
        self.velocity = -10  # Jump strength makes it move vertically up by 10

    def update(self):
        # simple gravity stuff
        self.velocity += gravity
        self.y += self.velocity

        # Prevent bird from going off-screen and the lowest height it can go is the edge of that window
        if self.y > window_height - bird_radius:
            self.y = window_height - bird_radius
            self.velocity = 0
        # preventing from the top from going away
        if self.y < bird_radius:
            self.y = bird_radius
            self.velocity = 0

    def draw(self, window):
        import pygame
        pygame.draw.circle(window, bird_color, (self.x, self.y), bird_radius)
