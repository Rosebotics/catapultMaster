import pygame
import sys
import time


class Ball():
    def __init__(self, screen):
        self.screen = screen
        self.ball_color = pygame.Color("green")
        starting_x = 70
        starting_y = 70
        self.radius = 10
        ball_width = 0
        self.circle_image = pygame.draw.circle(screen, self.ball_color, (starting_x, starting_y), self.radius, ball_width)
        self.x_direction = 2
        self.y_direction = 4

    def draw(self):
        pygame.draw.ellipse(self.screen, self.ball_color, self.circle_image)

    def move_ball(self):
        self.check_for_bounce()
        self.circle_image = self.circle_image.move(self.x_direction, self.y_direction)

    def check_for_bounce(self):
        if self.circle_image.centerx + self.radius >= self.screen.get_width():
            self.x_direction = -self.x_direction

        if self.circle_image.centery + self.radius >= self.screen.get_height():
            self.y_direction = -self.y_direction

        if self.circle_image.centerx - self.radius <= 0:
            self.x_direction = -self.x_direction

        if self.circle_image.centery - self.radius <= 0:
            self.y_direction = -self.y_direction


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

        ball.move_ball()
        ball.draw()


        pygame.display.update()


main()
