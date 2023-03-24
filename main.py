import sys
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


rect = Rectangular()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Surface.fill((240, 248, 255))

    rect.move()

    rect.draw()

    pygame.display.flip()
    clock.tick(FPS)


