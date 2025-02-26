import pygame
import random
from settings import SCREEN_WIDTH, OBSTACLE_SPEED

class Obstacle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.x -= OBSTACLE_SPEED
        if self.x < -self.size:
            self.x = SCREEN_WIDTH
            self.y = random.randint(100, 500)
        self.rect.x = self.x
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)