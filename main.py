import pygame
pygame.init()
SCREEN_WIDTH,  SCREEN_HEIGHT = 500,500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("add image and bg!!")

background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH,SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(),
    (200,200)
)

penguin_position = penguin_image.get_rect(
    center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
)

def game_loop():
    clock = pygame.time.Clock()
    done = True
    while done:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = False

        screen.blit(background_image,(0,0))
        screen.blit(penguin_image,penguin_position)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
    game_loop()
    



