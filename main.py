# Import the pygame library and initialise the game egine.
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()


# Define colours.
BLACK = (0,0,0)
WHITE = (255,255,255)
LPINK = (255,209,220)
LBROWN = (196,164,132)

# Open window.
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(LBROWN, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(LBROWN, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(LBROWN,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# Continue loop, until user exists the game.
carryOn = True

# Clock will control how fast the screen updates
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

# Main programm loop
while carryOn:
    # Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            carryOn = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: # Pressing x will quite game.
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # Game logic
    all_sprites_list.update()
    

    # Check if ball bounces against a wall
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


    # Drawing 
    screen.fill(LPINK)
    pygame.draw.line(screen, LBROWN, [349, 0], [349, 500], 5)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, LBROWN)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, LBROWN)
    screen.blit(text, (420, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()