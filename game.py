import pygame
import sys
import random
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))
def create_pipe():
    random_pip_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pip_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pip_pos-300))
    return bottom_pipe,top_pipe
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
        
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True
        

pygame.init()

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True

bg_surface = pygame.transform.scale2x(pygame.image.load('Images/imgs/bg.png')).convert()

floor_surface = pygame.transform.scale2x(pygame.image.load('Images/imgs/base.png')).convert()
floor_x_pos = 0
bird_surface = pygame.transform.scale2x(pygame.image.load('Images/imgs/bird1.png')).convert()
bird_rect = bird_surface.get_rect(center = (100,512))
pipe_surface = pygame.transform.scale2x(pygame.image.load('Images\imgs\pipe.png')).convert()
pipe_lst = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -9
            if event.key == pygame.K_SPACE and game_active == False:
                pipe_lst = []
                bird_movement = 0
                bird_rect.center = (100,512)
                game_active = True
                
        if event.type == SPAWNPIPE:
            pipe_lst.extend(create_pipe())
            print(pipe_lst)
        
    screen.blit(bg_surface, (10,0))
    if game_active:
        # Bird
        bird_movement+=gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_lst)

        # Pipes
        pipe_lst = move_pipes(pipe_lst)
        draw_pipes(pipe_lst)

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(90)