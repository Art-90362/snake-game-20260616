#!/usr/bin/env python3
"""
Классическая игра Змейка на Python с использованием Pygame.
Управление: Стрелки или WASD (включая русскую раскладку)
"""

import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Параметры игры
GRID_SIZE = 20
GRID_WIDTH = 20  # 400 / 20
GRID_HEIGHT = 20  # 400 / 20
WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE
FPS = 10  # Скорость игры (10 кадров в секунду)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (68, 68, 68)

# Настройка окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


class Snake:
    def __init__(self):
        self.body = [{"x": 10, "y": 10}]
        self.dx = 0
        self.dy = 0
        self.score = 0

    def move(self):
        if self.dx == 0 and self.dy == 0:
            return False

        head = {"x": self.body[0]["x"] + self.dx, "y": self.body[0]["y"] + self.dy}
        
        # Проверка столкновения со стенами
        if (head["x"] < 0 or head["x"] >= GRID_WIDTH or 
            head["y"] < 0 or head["y"] >= GRID_HEIGHT):
            return False
        
        # Проверка столкновения с хвостом
        for segment in self.body:
            if head["x"] == segment["x"] and head["y"] == segment["y"]:
                return False
        
        self.body.insert(0, head)
        return True

    def check_food(self, food):
        if self.body[0]["x"] == food["x"] and self.body[0]["y"] == food["y"]:
            self.score += 1
            return True
        else:
            self.body.pop()
            return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(
                screen, 
                GREEN, 
                (segment["x"] * GRID_SIZE, segment["y"] * GRID_SIZE, 
                 GRID_SIZE - 2, GRID_SIZE - 2)
            )

    def reset(self):
        self.body = [{"x": 10, "y": 10}]
        self.dx = 0
        self.dy = 0
        self.score = 0


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            position = {
                "x": random.randint(0, GRID_WIDTH - 1),
                "y": random.randint(0, GRID_HEIGHT - 1)
            }
            # Проверка, чтобы еда не появилась внутри змейки
            collision = False
            for segment in snake_body:
                if position["x"] == segment["x"] and position["y"] == segment["y"]:
                    collision = True
                    break
            if not collision:
                return position

    def reposition(self, snake_body):
        self.position = self.generate_position(snake_body)

    def draw(self):
        pygame.draw.rect(
            screen, 
            RED, 
            (self.position["x"] * GRID_SIZE, self.position["y"] * GRID_SIZE, 
             GRID_SIZE - 2, GRID_SIZE - 2)
        )


def draw_score(score):
    score_text = font.render(f"Счёт: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def draw_game_over(score):
    game_over_text = font.render("Игра окончена!", True, WHITE)
    score_text = font.render(f"Счёт: {score}", True, WHITE)
    restart_text = font.render("Нажми пробел для рестарта", True, WHITE)
    
    screen.blit(game_over_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 60))
    screen.blit(score_text, (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 20))
    screen.blit(restart_text, (WINDOW_WIDTH // 2 - 140, WINDOW_HEIGHT // 2 + 20))


def main():
    snake = Snake()
    food = Food(snake.body)
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # Управление стрелками или WASD
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_w, pygame.K_cyrillicYERU, pygame.K_CYRILLIC_YERU):
                    if snake.dy == 0:
                        snake.dx = 0
                        snake.dy = -1
                elif event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_s, pygame.K_cyrillic_BE, pygame.K_CYRILLIC_BE):
                    if snake.dy == 0:
                        snake.dx = 0
                        snake.dy = 1
                elif event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_a, pygame.K_cyrillic_F, pygame.K_CYRILLIC_F):
                    if snake.dx == 0:
                        snake.dx = -1
                        snake.dy = 0
                elif event.key in (pygame.K_RIGHT, pygame.K_d, pygame.K_d, pygame.K_cyrillic_VE, pygame.K_CYRILLIC_VE):
                    if snake.dx == 0:
                        snake.dx = 1
                        snake.dy = 0
                elif event.key == pygame.K_SPACE and game_over:
                    snake.reset()
                    food.reposition(snake.body)
                    game_over = False

        if not game_over:
            # Движение змейки
            if not snake.move():
                game_over = True
            
            # Проверка еды
            if snake.check_food(food.position):
                food.reposition(snake.body)

        # Отрисовка
        screen.fill(BLACK)
        
        # Сетка (опционально)
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

        snake.draw()
        food.draw()
        draw_score(snake.score)

        if game_over:
            draw_game_over(snake.score)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
