import pygame
import sys


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.color = pygame.Color("green")
        self.x = 70
        self.y = 70
        self.radius = 10
        self.speed_x = 2
        self.speed_y = 4

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.x + self.radius >= self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.y + self.radius >= self.screen.get_height():
            self.speed_y = -self.speed_y
        if self.x - self.radius <= 0:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    ball = Ball(screen)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        ball.move()
        ball.draw()

        pygame.display.update()


main()
