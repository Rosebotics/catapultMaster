import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    frame_color = (0, 0, 0)

    instruction_text = 'Click in the circle'
    text_color = (122, 237, 201)
    text_background_color = frame_color

    instructions_image = font.render(instruction_text, True, text_color, text_background_color)

    circle_color = (182, 210, 110)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 5

    pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_position = event.pos
                distance_from_circle = distance(click_position, circle_center)
                if distance_from_circle < circle_radius:
                    message_text = 'Bullseye!'
                else:
                    message_text = 'You missed!'

        screen.fill(frame_color)

        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        onscreen_message = font.render(message_text, True, (122, 237, 201), (0, 0, 0))

        screen.blit(instructions_image, (25, 25))
        screen.blit(onscreen_message, (25, 375))

        pygame.display.update()


main()
