import sys
import random

import pygame

pygame.init()

HEIGHT = 500
WIDTH = 800

Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Arkanoid')
clock = pygame.time.Clock()
FPS = 30


class Rectangular:
    def __init__(self):
        self.left = 300
        self.top = 480
        self.rect = pygame.Rect(self.left, self.top, 200, 10)
        self.color = (0, 0, 128)

    def draw(self):
        pygame.draw.rect(Surface, self.color, self.rect, 0)

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if 0 <= self.left <= 600:
                    self.rect.move_ip(max([-10, -self.left]), 0)
                    self.left += max([-10, -self.left])
            if event.key == pygame.K_RIGHT:
                if 0 <= self.left <= 600:
                    self.rect.move_ip(min([10, 600 - self.left]), 0)
                    self.left += min([10, 600 - self.left])



class Circle:
    def __init__(self):
        self.x = 400
        self.y = 470
        self.radius = 10
        self.color = (0, 0, 0)
        self.delta_x = 10
        self.delta_y = -10

    def draw(self):
        pygame.draw.circle(Surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x = self.x + self.delta_x
        self.y = self.y + self.delta_y


def get_move(circle_x, circle_y, rect_left):
    if circle_x == 0 or circle_x == 800:
        circle.delta_x *= -1

    if circle_y == 0:
        circle.delta_y *= -1

    if rect_left <= circle.x <= rect_left + 200 and circle.y == rect.top:
        circle.delta_y *= -1


rect = Rectangular()
circle = Circle()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Surface.fill((240, 248, 255))

    rect.move()
    circle.move()

    get_move(circle.x, circle.y, rect.left)

    rect.draw()
    circle.draw()

    pygame.display.flip()
    clock.tick(FPS)


