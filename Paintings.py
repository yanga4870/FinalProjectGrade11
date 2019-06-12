import pygame
import random

class Paintings(pygame.sprite.Sprite):#create paintings
    Paints = [(pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint1.png"), (32 * 2, 2 * 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint2.png"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint3.png"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint4.png"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint5.png"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint6.png"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint7.png"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint8.jpg"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint9.jpg"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint10.jpg"), (32, 32))),
              (pygame.transform.scale(pygame.image.load("Graphics/Painting Images/Paint11.jpg"), (32, 32)))]
    def __init__(self,x,y,width,height,group,points):
        self.groups = group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((width, height),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points=points
        if self.points==1000:
            self.image.blit(self.Paints[random.randint(5,10)], (0,0))
            self.image.blit(pygame.transform.scale(pygame.image.load("Graphics/Painting Images/painting1.png"),(32,32)),(0,0))
        elif self.points==5000:
            self.image.blit(self.Paints[random.randint(1, 4)], (0, 0))
            self.image.blit(pygame.transform.scale(pygame.image.load("Graphics/Painting Images/painting2.png"),(32,32)),(0,0))
        elif self.points==50000:
            self.image.blit(self.Paints[0], (0, 0))
            self.image.blit(pygame.transform.scale(pygame.image.load("Graphics/Painting Images/painting3.png"),(32*2,2*32)),(0,0))

class Key(pygame.sprite.Sprite):#create key
    def __init__(self,x,y,width,height,group):
        self.groups = group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((width, height),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.blit(pygame.transform.scale(pygame.image.load("Graphics/Game Images/key.png"), (32, 32)), (0,0))
        self.points = 0