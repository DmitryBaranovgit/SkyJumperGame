import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SCORE_INCREMENT
from player import Player
from platforms import Platform
from obstacle import Obstacle
from leaderboard import save_leaderboard

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.font = pygame.font.Font(None, 36)

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.platforms = [Platform(random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 50), 100, 20) for _ in range(5)]
        self.obstacles = [Obstacle(random.randint(300, SCREEN_WIDTH), random.randint(100, 500), 30) for _ in range(3)]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.alive:
                    self.player.jump()
    
    def update(self):
        if self.player.alive:
            self.player.update()
        for platform in self.platforms:
            platform.update()
            platform.increase_speed()
        
        for obstacle in self.obstacles:
            obstacle.update()
        
        # Проверка столкновения с платформами
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect) and self.player.velocity_y > 0:
                self.player.velocity_y = 0
                self.player.rect.bottom = platform.rect.top
                self.score += SCORE_INCREMENT # Начисление очков
        # Проверка столкновений с препятствиями
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.player.alive = False

        if not self.player.alive:
            save_leaderboard(self.score)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        for platform in self.platforms:
            platform.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

        if not self.player.alive:
            self.show_game_over()
        
        pygame.display.flip()
    
    def show_game_over(self):
        text = self.font.render("Game over! Press R to Restart", True, (255, 0, 0))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        self.wait_for_restart()
    
    def wait_for_restart(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__init__() # Перезапуск игры
                    return
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)