import pygame
from settings import GRAVITY, JUMP_STRENGTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = 0
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.alive = True

    def jump(self):
        self.velocity_y = JUMP_STRENGTH

    def update(self):
        self.velocity_y += GRAVITY
        self.y += self.velocity_y
        self.rect.y = self.y

        # Проверка на падение
        if self.rect.top > SCREEN_HEIGHT:
            self.alive = False
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)