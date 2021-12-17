import pygame
from pygame.color import THECOLORS

pygame.font.init()
pygame.init()


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, xrec=50, yrec=50):
        super().__init__()
        self.position = [x, y]
        self.stop = False
        # создаем графический объект для визуализаци ("спрайт")
        self.image = pygame.Surface((xrec, yrec))
        self.rect = self.image.get_rect()
        self.rect.center = self.position[0], self.position[1]

    def check_collision(self, group):
        others = group.copy()
        if group.has(self):
            others.remove(self)
        collided = pygame.sprite.spritecollideany(self, others)
        if collided:
            self.collision_update()

    def collision_update(self):
        pass

    def set_position(self, value):
        self.position = value
        self.rect.center = self.position[0], self.position[1]

class Gate(GameObject)
class Person(GameObject):
    """Класс для описания любого участника игры"""

    # Аттрибуты класса
    ableToMove = True

    # Методы класса
    def __init__(self, x=0, y=0):
        super(Person, self).__init__(x, y, 50, 50)

    def move(self, dx, dy):
        """Метод класса для перемещения участника игры"""

        if not self.stop:
            self.position[0] += dx
            self.position[1] += dy
            # обновили графический объект ("спрайт")
            self.rect.center = (self.position[0], self.position[1])

    def freeze(self):
        """Метод для остановки всех участников игры"""
        self.ableToMove = False


class Player(Person):
    """Класс для описания игроков, потомок класса Person"""

    def __init__(self, num, col=THECOLORS["red"]):
        super().__init__()
        self.number = num
        self.color = col
        self.image.fill(col)
        font = pygame.font.SysFont(None, 24)
        img = font.render(self.number, True, "white")
        self.image.blit(img, self.rect.center)

    def stop_ball(self, ball):
        ball.set_speed([0, 0])

    def collision_update(self):
        pass
        # self.stop = True

    def __str__(self):
        return "Игрок %s цвет %s" % (self.number, self.color)


class Ball(GameObject):
    def __init__(self, x=0, y=0, sd=1):
        super(Ball, self).__init__(x, y, 10, 10)
        self.speed = [0, 0]
        self.slowdown = sd
        # self.rect.center = (self.position[0], self.position[1])

    def move(self, dt=0):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        self.speed[0] -= self.slowdown * dt
        self.speed[1] -= self.slowdown * dt
        self.rect.center = (self.position[0], self.position[1])

    def collision_update(self):
        # pass
        self.speed[0] *= -1
        self.speed[1] *= -1

    def set_speed(self, val):
        self.speed = val

    def update(self):
        self.move()


class Goalkeeper(Player):
    """Класс для описания вратаря, потомок класса Player"""

    pass


# первая команда "blue"
pl1 = Player("1", "blue")  # создаем игрока
# pl2 = Player("2", "blue")  # создаем еще одного игрока
pl1.move(50, 50)  # скомандуем игроку переместиться
# pl2.move(30, 40)
# print(pl2)  # используем метод __str__ для вывода

# вторая команда "green"
pl3 = Player("1", "green")
pl3.move(350, 350)
# pl4 = Player("2", "green")
# pl3.move(310, 40)
# pl4.move(200, 200)
b = Ball(100, 100)
b.set_speed([1,1])
scr = pygame.display.set_mode((400, 400))

all_sprites = pygame.sprite.Group()  # группа для всех "спрайтов"
team_1 = pygame.sprite.Group([pl1])
team_2 = pygame.sprite.Group([pl3])
all_sprites.add(team_1)
all_sprites.add(team_2)
all_sprites.add(b)

players = pygame.sprite.Group(team_1, team_2)

# основной цикл игры
while True:
    # обработка пользовательских событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # работаем с игроками
    for pl in players:
        pl.check_collision(all_sprites)
    b.check_collision(all_sprites)
    b.update()
    pl1.move(0.5, 0.5)
    pl3.move(-0.5, -0.5)

    # отрисовываем картинку
    scr.fill((255, 255, 255))
    all_sprites.draw(scr)
    pygame.display.update()
    pygame.time.delay(20)

    # for sprite in all_sprites_list:
    #     print("проверяем", sprite)
    #     collided_list = pygame.sprite.spritecollide(sprite, all_sprites_list, False)
    #     for collided in collided_list:
    #         print("столкнулся с ", collided)
    #         sprite.stop = True
    #         collided.stop = True
