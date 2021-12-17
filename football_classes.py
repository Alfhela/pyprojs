import pygame
from math import atan
from pygame import surface
from pygame.color import THECOLORS
from pygame.draw import line

pygame.font.init()


class GameObject(pygame.sprite.Sprite):
    """Класс для описания отрисовки всех игровых объектов"""

    def __init__(self, x=0, y=0, xrec=50, yrec=50, rotate=0.0):
        """Конструктор класса GameObject"""
        super().__init__()
        # инициализация атрибутов класса
        self.position = [x, y]
        # инициализируем графический объект ("спрайт") для визуализаци
        self.image = pygame.transform.rotate(pygame.Surface((xrec, yrec)), rotate)
        self.rect = self.image.get_rect()

    # Методы класса
    def check_collision(self, group=pygame.sprite.Group()):
        others = group.copy()
        if group.has(self):
            others.remove(self)
        collided = pygame.sprite.spritecollideany(self, others)
        if collided:
            self.update_on_collision(collided)

    # виртуальный метод
    def update_on_collision(self, collided):
        pass  # виртуальня метод реализуется в классах-наследниках

    def update(self):
        """Используется группой спрайтов для обновления спрайта"""
        # обновляем графический объект ("спрайт")
        self.rect.center = (self.position[0], self.position[1])

    # метод-сеттер
    def set_position(self, x, y):
        """Устанавливает значение атрибута"""
        self.position = [x, y]

    def get_position(self):
        """Устанавливает значение атрибута"""
        return self.position

    # специальный метод для отображения экземпляра класса
    def __str__(self):
        return "Object position %s" % self.position


class Gate(GameObject):
    def __init__(self, x=0, y=0):
        super().__init__(x, y, xrec=15, yrec=15)


class GateCenter(GameObject):
    def __init__(self, width, g1: Gate, g2: Gate):
        pos1 = g1.get_position()
        pos2 = g2.get_position()
        super().__init__(x=(pos1[0] + pos2[0]) // 2, y=(pos1[1] + pos2[1]) // 2,
                         xrec=((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5, yrec=width,
                         rotate=atan((abs(pos1[1] - pos2[1]) - (abs(pos1[0] - pos2[0])))))


class Person(GameObject):
    """Класс для описания любого участника игры"""

    # Аттрибуты класса
    ableToMove = True

    # Методы класса
    def __init__(self):
        """Конструктор класса Person"""
        super().__init__()
        self.stop = False

    # реализация виртуального метода
    def update_on_collision(self, collided):
        if isinstance(collided, Person):
            self.stop = True

    def move(self, dx, dy):
        """Метод класса для перемещения участника игры"""
        if not self.stop:
            self.position[0] += dx
            self.position[1] += dy

    def freeze(self):
        """Метод для остановки всех участников игры"""
        self.ableToMove = False


class Player(Person):
    """Класс для описания игроков, потомок класса Person"""

    def __init__(self, num, col=THECOLORS["red"]):
        """Конструктор класса Player"""
        super().__init__()
        self.number = num
        self.color = col
        # инициализируем графический объект цветом и номером
        self.image.fill(col)
        font = pygame.font.SysFont(None, 24)
        img = font.render(self.number, True, "white")
        self.image.blit(img, self.rect.center)

    def dribble(self, ball):
        """Метод для ведения мяча"""
        ball.speed = [0, 0]
        ball.set_position(self.position[0], self.position[1])

    def kick(self):
        """Метод для передачи паса"""
        pass

    # реализация виртуального метода
    def update_on_collision(self, collided):
        super().update_on_collision(collided)
        if isinstance(collided, Ball):
            self.dribble(collided)

    def __str__(self):
        return "Игрок %s цвет %s" % (self.number, self.color)


class Goalkeeper(Player):
    """Класс для описания вратаря, потомок класса Player"""

    pass


class Ball(GameObject):

    def __init__(self, x=0, y=0):
        super().__init__(x, y, xrec=10, yrec=10)
        self.speed = [0, 0]

    def update_on_collision(self, collided):
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]

    def move(self, dt=0):
        self.position[0] += self.speed[0] * dt
        self.position[1] += self.speed[1] * dt


class Team:
    players = 0

    def __init__(self, name, players: list):
        self.name = name
        self.players = players

    def count_players(self):
        return len(self.players)

    def get_name(self):
        return self.name

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)
