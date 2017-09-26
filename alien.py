import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_sittings, screen):

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_sittings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect)