import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake block size
BLOCK_SIZE = 10

# Clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, GREEN)
    screen.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLUE, [block[0], block[1], block_size, block_size])

def display_message(msg, color):
    message = font_style.render(msg, True, color)
    screen.blit(message, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    # Initial position
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Initial movement
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            display_message("You lost! Press Q-Quit or C-Play Again", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()

# Run the game
game_loop()