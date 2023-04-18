import pygame, sys
img_clear = pygame.image.load("space_invaders_imgs/clear.png")
img_pop = pygame.image.load("space_invaders_imgs/alian_pop.png")
class alian(pygame.sprite.Sprite):
    
    def __init__(self, startX,startY,width,height,image_load):
        super().__init__() 
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.alive=True
        self.pop =False
        self.count=20
            
    def update(self):
        if self.alive == False and self.pop==False:
            self.image = pygame.transform.scale(img_pop, (20, 20)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)
            self.count -= 1
            if self.count == 0:
                self.pop = True
        elif self.pop==True:
            self.image = pygame.transform.scale(img_clear, (20, 20)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)    
        
    
