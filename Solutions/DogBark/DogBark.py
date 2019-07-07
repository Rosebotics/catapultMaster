import pygame, sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()
    pygame.font.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Load the music and the image
    pygame.mixer.music.load("bark.mp3")
    image1 = pygame.image.load("2dogs.JPG")
    font1 = pygame.font.Font(None, 28)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # play the music if there's a mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the surfaces on the screen
        image1 = pygame.transform.scale(image1, (470, 470))
        screen.blit(image1, (0, 0))

        caption1 = font1.render("Two Dogs", True, BLACK)
        screen.blit(caption1, ((image1.get_width() // 2 - caption1.get_width() // 2), (image1.get_height() + 5)))

        # Update the screen
        pygame.display.update()


main()
