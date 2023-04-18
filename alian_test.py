import pygame, sys
immage = pygame.image.load("space_invaders_imgs/clear.png")
class alian(pygame.sprite.Sprite):
    
    def __init__(self, startX,startY,width,height,image_load):
        super().__init__() 
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.alive=True
            
    def update(self):
        if self.alive == False:
            self.image = pygame.transform.scale(immage, (20, 20)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)
    
