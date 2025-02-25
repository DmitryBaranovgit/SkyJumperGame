import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player
from platforms import Platform

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.platforms = [Platform(random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 50), 100, 20, 2) for _ in range(5)]
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
    
    def update(self):
        self.player.update()
        for platform in self.platforms:
            platform.update()
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        for platform in self.platforms:
            platform.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)