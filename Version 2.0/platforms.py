import pygame
import random
from settings import SCREEN_WIDTH, PLATFORM_SPEED

class Platform:
    def __init__(self, x, y, width, height, speed = PLATFORM_SPEED):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH
            self.y = random.randint(100, SCREEN_WIDTH - 100)
        self.rect.x = self.x
    
    def increase_speed(self):
        self.speed += 0.1 # Увеличение скорости платформ со верменем
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)