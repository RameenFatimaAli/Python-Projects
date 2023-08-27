import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH = 400
HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -4
PIPE_SPEED = 2
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(bird_img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, 300)

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        screen.blit(pipe_img, (self.x, 0), (0, 320 - self.height, 52, self.height))
        screen.blit(pipe_img, (self.x, HEIGHT - self.height - PIPE_GAP), (0, 0, 52, self.height + PIPE_GAP))

# Create bird and pipes
bird = Bird()
pipes = [Pipe(WIDTH)]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.flap()

    bird.update()

    # Add new pipe if needed
    if pipes[-1].x < WIDTH - 200:
        pipes.append(Pipe(WIDTH))

    # Update and draw pipes
    for pipe in pipes:
        pipe.update()
        pipe.draw()

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x > -52]

    # Check collisions
    for pipe in pipes:
        if bird.x + 34 > pipe.x and bird.x < pipe.x + 52:
            if bird.y < pipe.height or bird.y + 24 > pipe.height + PIPE_GAP:
                running = False

    # Draw bird
    screen.fill(WHITE)
    bird.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
