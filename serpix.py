import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Snake with Usman")

snake_x = 50
snake_y = 65
snake_size = 12

fps = 30
exit_game = False
game_over = False
initial_velocity = 10
score = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

current_direction_x = 1
current_direction_y = 0

border_thickness = 5
border_color = black

snake_list = []
snake_length = 1


def display_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def show_game_over_screen():
    game_over_text = font.render(
        "Game Over! Your Score: " + str(score * 10), True, red)
    gameWindow.blit(game_over_text, [400, 250])
    pygame.display.update()
    pygame.time.delay(2000)


food_x = random.randint(0, 800)
food_y = random.randint(0, 400)

while not exit_game:
    gameWindow.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and current_direction_x != -1:
                current_direction_x = 1
                current_direction_y = 0
            if event.key == pygame.K_LEFT and current_direction_x != 1:
                current_direction_x = -1
                current_direction_y = 0
            if event.key == pygame.K_UP and current_direction_y != 1:
                current_direction_x = 0
                current_direction_y = -1
            if event.key == pygame.K_DOWN and current_direction_y != -1:
                current_direction_x = 0
                current_direction_y = 1

    snake_x += current_direction_x * initial_velocity
    snake_y += current_direction_y * initial_velocity

    if snake_x < 0 or snake_x > 1200 or snake_y < 0 or snake_y > 500:
        game_over = True
        current_direction_x = 1
        current_direction_y = 0

    if [snake_x, snake_y] in snake_list[:-1]:
        game_over = True
        current_direction_x = 1
        current_direction_y = 0

    if game_over:
        show_game_over_screen()
        game_over = False
        snake_x = 50
        snake_y = 65
        snake_list = []
        snake_length = 1
        score = 0

    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score += 1
        food_x = random.randint(0, 1000)
        food_y = random.randint(0, 400)
        snake_length += 2.5

    display_text("Score: " + str(score * 10), black, 5, 5)
    pygame.draw.rect(gameWindow, black,
                     (food_x, food_y, snake_size, snake_size))

    for segment in snake_list:
        pygame.draw.rect(
            gameWindow, red, (segment[0], segment[1], snake_size, snake_size))

    head = [snake_x, snake_y]
    snake_list.append(head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    pygame.draw.rect(gameWindow, border_color,
                     (0, 0, 1200, border_thickness))
    pygame.draw.rect(gameWindow, border_color,
                     (0, 0, border_thickness, 500))
    pygame.draw.rect(gameWindow, border_color, (0, 500 -
                     border_thickness, 1200, border_thickness))
    pygame.draw.rect(gameWindow, border_color, (1200 -
                     border_thickness, 0, border_thickness, 500))

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
