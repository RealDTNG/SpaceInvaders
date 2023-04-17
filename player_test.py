import pygame, sys

class thing(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load):
        super().__init__()
        self.image = pygame.transform.scale(image_load, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        
    def move(self):
        t_f_list = {True : 1, False: 0}
        key_input = pygame.key.get_pressed()
        
        self.movex = (t_f_list[key_input[pygame.K_LEFT]] * -2) + (t_f_list[key_input[pygame.K_RIGHT]] * 2)

        self.rect.x += self.movex

        
    def back(self):
        self.rect.x -= self.movex

