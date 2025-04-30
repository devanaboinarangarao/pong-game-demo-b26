import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)  # Color for paddles, ball, and divider
BLACK = (0, 0, 0)  # Background color

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100  # Width and height of paddles
BALL_RADIUS = 7  # Radius of the ball

# Speeds
PADDLE_SPEED = 5  # Speed of paddle movement
BALL_SPEED_X, BALL_SPEED_Y = 4, 4  # Initial speed of the ball

# Initialize paddles and ball
player1 = pygame.Rect(10, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)  # Player 1 paddle
player2 = pygame.Rect(WIDTH - 20, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)  # Player 2 paddle
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)  # Ball

# Ball direction
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y  # Ball movement direction

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for quit event
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:  # Move Player 1 paddle up
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:  # Move Player 1 paddle down
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:  # Move Player 2 paddle up
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:  # Move Player 2 paddle down
        player2.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx  # Update ball's x position
    ball.y += ball_dy  # Update ball's y position

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:  # Reverse direction if ball hits top/bottom
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):  # Reverse direction if ball hits paddle
        ball_dx *= -1

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:  # Reset ball position if it goes out of bounds
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dx, ball_dy = BALL_SPEED_X * random.choice([-1, 1]), BALL_SPEED_Y * random.choice([-1, 1])

    # Draw everything
    screen.fill(BLACK)  # Fill screen with background color
    pygame.draw.rect(screen, WHITE, player1)  # Draw Player 1 paddle
    pygame.draw.rect(screen, WHITE, player2)  # Draw Player 2 paddle
    pygame.draw.ellipse(screen, WHITE, ball)  # Draw ball
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))  # Draw center divider

    pygame.display.flip()  # Update display
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()