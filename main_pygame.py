import pygame

pygame.font.init()




class Person(pygame.sprite.Sprite):
    # TODO #2 : сделать коллизию 
    ableToMove = True

    def __init__(self, x=0, y=0):
        super().__init__()
        self.position = [x, y]

        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy
        self.rect.center = (self.position[0], self.position[1])

    def freeze(self):
        self.ableToMove = False


class Player(Person):

    def __init__(self, num, color):
        super().__init__()
        self.number = num
        self.color = color
        self.image.fill(self.color)
        self.font = pygame.font.SysFont("default", 90)
        self.numtext = self.font.render(num, False, (0, 0, 0))
        self.image.blit(self.numtext, (0, 0))


pl1 = Player("1", "blue")
pl2 = Player("2", "red")

pl1.move(2, 2)
pl2.move(100, 100)
pygame.init()
scr = pygame.display.set_mode((400, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    scr.fill((255, 255, 255))
    scr.blit(pl1.image, pl1.rect)
    scr.blit(pl2.image, pl2.rect)
    pygame.display.update()
    pygame.time.delay(200)

    pl1.move(1, 1)
