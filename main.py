import pygame,sys,random
from game import Game
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 550
OFFSET = 35

GREY = (29,29,27)
YELLOW = (243,216,63)

font = pygame.font.Font("Font/monogram.ttf",35)
level_surface = font.render("LEVEL 01",False, YELLOW)
game_over_surface =font.render("GAME OVER", False, YELLOW)
score_text_surface=font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGHSCORE",False,YELLOW)

screen = pygame.display.set_mode((SCREEN_WIDTH+OFFSET,SCREEN_HEIGHT+2*OFFSET)) #creating a screen where the game will run

pygame.display.set_caption("Python Space Invaders") # caption or title of game

clock = pygame.time.Clock() # the time for which game will run

game = Game(SCREEN_WIDTH,SCREEN_HEIGHT,OFFSET)

SHOOT_LASER=pygame.USEREVENT #used to create custom events
pygame.time.set_timer(SHOOT_LASER,300)

MYSTERYSHIP = pygame.USEREVENT +1
pygame.time.set_timer(MYSTERYSHIP,random.randint(4000,8000))


while True:
    # checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()
            
        if event.type == MYSTERYSHIP and game.run:
            game.create_mysteryship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))
            
            
        keys =  pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run==False:
            game.reset()
    #updating 
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mysteryship_group.update()
        game.check_collision()
    
    # drawing 
    screen.fill(GREY)
    
    #UI
    pygame.draw.rect(screen, YELLOW, (1, 3, 630, 610), 2, 0, 70, 70, 5, 5)
    pygame.draw.line(screen, YELLOW, (20, 565), (565, 565), 3)

    if game.run:
        screen.blit(level_surface, (SCREEN_WIDTH - 130, SCREEN_HEIGHT + 20))
    else:
        screen.blit(game_over_surface, (SCREEN_WIDTH - 130, SCREEN_HEIGHT + 20))
    

    x = 10  # Start close to the left edge
    y = SCREEN_HEIGHT +20  # Slightly above the bottom edge

    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, y))
        x += 50  # Shift each life icon to the right

    
    screen.blit(score_text_surface,(50,15,50,50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score,False,YELLOW)
    screen.blit(score_surface,(50,40,50,50))
    screen.blit(highscore_text_surface,(480,15,50,50))
    formatted_highscore=str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore,False, YELLOW)
    screen.blit(highscore_surface,(530,40,50,50))
        
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mysteryship_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # while loop will run 60 time a second
    