import pygame
import time

pygame.init()
speed = [50,50]
background = 255, 255, 255
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball test build")
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
clock = pygame.time.Clock()
running = True
while running:
    # the window and the ball
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
            break
        
    ball_rect = ball_rect.move(speed)

        # this keeps the ball going off the edge
    if ball_rect.left < 0:
         ball_rect. left = 0
         speed[0] = abs(speed[0])
    elif ball_rect.right > width:
         ball_rect.right = width
         speed[0] = -abs(speed[0])
    if ball_rect.top < 0:
        ball_rect.top = 0
        speed[1] = abs(speed[1])
    elif ball_rect.bottom > height:
        ball_rect.bottom = height
        speed[1] = -abs(speed[1])


    screen.fill(background)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
    clock.tick(120)
    pygame.quit

