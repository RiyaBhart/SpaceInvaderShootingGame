import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,position,speed,screen_height):
        super().__init__()
        self.image = pygame.Surface((4,15)) #creates a small rectangle where width is 4px and heught is 15px
        self.image.fill((243,216,63)) # yellow color, (red,green,blue) the concentration of these three makes the new color
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height
        
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height+15 or self.rect.y<0:
            self.kill()