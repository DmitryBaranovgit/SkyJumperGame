import os

# Константы игры
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = -10
PLATFORM_SPEED = 2
SCORE_INCREMENT = 10
OBSTACLE_SPEED = 3
LEADERBOARD_FILE = os.path.join(os.getcwd(), "leaderboard.json")