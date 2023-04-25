import pygame, sys

alian_s1 = pygame.image.load('space_invaders_imgs/alian_shot_1.png')
alian_s3 = pygame.image.load('space_invaders_imgs/alian_shot_3.png')

class bullet(pygame.sprite.Sprite):
    
    def __init__(self, startX,startY,width,height,image_load):
        super().__init__() 
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.count = 10
        self.b_img = 1
            
    def move_play(self): 
        self.rect.y -= 4
        
    def move_alian(self):
        self.rect.y += 4
        self.count -= 2
        if self.count <= 0:
            if self.b_img == 1:
                self.image = pygame.transform.scale(alian_s3, (10, 28)).convert_alpha()
                self.mask  = pygame.mask.from_surface(self.image)
                self.count = 10
                self.b_img = 2
            elif self.b_img == 2:
                self.image = pygame.transform.scale(alian_s1, (10, 28)).convert_alpha()
                self.mask  = pygame.mask.from_surface(self.image)
                self.count = 10
                self.b_img = 1
                

    
