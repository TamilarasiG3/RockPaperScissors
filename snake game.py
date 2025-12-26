import pygame
import sys
import random

# Game settings
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_snake(screen, snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

def random_food():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return (x, y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = 'RIGHT'
    food = random_food()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Move snake
        x, y = snake[0]
        if direction == 'UP':
            y -= BLOCK_SIZE
        elif direction == 'DOWN':
            y += BLOCK_SIZE
        elif direction == 'LEFT':
            x -= BLOCK_SIZE
        elif direction == 'RIGHT':
            x += BLOCK_SIZE
        new_head = (x, y)

        # Check collisions
        if (
            x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or
            new_head in snake
        ):
            print(f"Game Over! Your score: {score}")
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = random_food()
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)
        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()