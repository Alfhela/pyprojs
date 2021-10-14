import pygame
class Person(pygame.sprite.Sprite):
    """Класс для описания любого участника игры"""

    # Аттрибуты класса
    ableToMove = True

    # Методы класса
    def __init__(self, x=0, y=0):
        super().__init__()
        self.position = [x, y]

        self.image = pygame.surface((50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0],self.position[1])

    def move(self, dx, dy):
        """Метод класса для перемещения участника игры"""
        if self.ableToMove == True:
            self.position[0] += dx
            self.position[1] += dy

    def freeze(self):
        """Метод для остановки всех участников игры"""
        self.ableToMove = False


class Player(Person):
    """Класс для описания игроков, потомок класса Person"""

    def __init__(self, num):
        super().__init__()
        self.number = num


class Goalkeeper(Player):
    """Класс для описания вратаря, потомок класса Player"""

    pass


person1 = Person()  # создаем человека
print("Положение человека 1:", person1.position)
person1.move(1, 1)  # отдаем команду человеку переместиться
print("Положение человека 1 после перемещения:", person1.position)

pl1 = Player("1")  # создаем игрока
pl2 = Player("2")  # создаем еще одного игрока
print("Положение игрока:", pl1.number, pl1.position)
print("Положение игрока:", pl2.number, pl2.position)
pl1.move(2, 2)  # скомандуем игроку переместиться
print("Положение игрока 1:", pl1.position)
