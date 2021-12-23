import pygame
class Person(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        self.AbleToMove = True
        self.position = (x, y)

    def freeze(self):
        self.AbleToMove = False

    def move(self, dx, dy):
        if self.AbleToMove:
            self.position = (self.position[0] + dx, self.position[1] + dy)

    def moveto(self, x, y):
        if self.AbleToMove:
            self.position = (x, y)


class Player(Person):
    def __init__(self, team='None', x=0, y=0, num = 0):
        super().__init__(x, y)
        self.number=num
        self.team = team


class Goalkeeper(Player):
    def __init__(self, team='None', x=0, y=0,num = 0):
        super().__init__(team, x, y,num)
        self.inGates = True


p1 = Player('Blue', 5, 6)
p2 = Player('Red', 2, 3)

p1.move(10, 20)
p2.moveto(-10, -3)
p2.freeze()
p2.move(123, 321)
print(p1.position, p2.position)
print(p1.team)



