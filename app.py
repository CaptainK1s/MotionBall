import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MotionBall")

clock = pygame.time.Clock()

balls = []

for _ in range(12):
    balls.append({
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(50, HEIGHT - 50),
        "dx": random.choice([-4, -3, 3, 4]),
        "dy": random.choice([-4, -3, 3, 4]),
        "radius": random.randint(10, 30),
        "color": (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
    })

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((10, 10, 20))

    for ball in balls:
        ball["x"] += ball["dx"]
        ball["y"] += ball["dy"]

        if ball["x"] - ball["radius"] <= 0 or ball["x"] + ball["radius"] >= WIDTH:
            ball["dx"] *= -1

        if ball["y"] - ball["radius"] <= 0 or ball["y"] + ball["radius"] >= HEIGHT:
            ball["dy"] *= -1

        pygame.draw.circle(
            screen,
            ball["color"],
            (ball["x"], ball["y"]),
            ball["radius"]
        )

    pygame.display.flip()
    clock.tick(60)
