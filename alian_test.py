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
        self.movex = 1
    def move(self,x,y):
        self.rect.x+=x
        self.rect.y+=y
            
    def update(self, type1, type2):
        if self.alive == False and self.pop==False:
            self.image = pygame.transform.scale(img_pop, (44, 32)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)
            self.count -= 1
            if self.count == 0:
                self.pop = True
        elif self.pop==True:
            self.image = pygame.transform.scale(img_clear, (20, 20)).convert_alpha()
            self.mask  = pygame.mask.from_surface(self.image)  
         
        if type1 == False:  
            if type2 == True:    
                    self.movex = -self.movex
                    self.rect.x += self.movex
                    self.rect.y += 10
            if type2 == False:
                    self.rect.x += self.movex
        
        if type1 == True:    
            if self.rect.x > 1100:
                self.movex = -1
                self.rect.x += -5
                self.rect.y += 10
                self.rect.x += self.movex
            elif self.rect.x < 400:
                self.movex = 1
                self.rect.x += 5
                self.rect.y += 10
                self.rect.x += self.movex
            else:
                self.rect.x += self.movex 
        return self.rect.x, self.rect.y
               
          
        
    
