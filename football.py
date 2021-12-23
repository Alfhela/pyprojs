from football_classes import *

person1 = Person()  # создаем человека
print("Положение человека 1:", person1.position)
person1.move(1, 1)  # отдаем команду человеку переместиться
print("Положение человека 1 после перемещения:", person1.position)

# первая команда "blue"
pl1 = Player("1", "blue")  # создаем игрока
pl2 = Player("2", "blue")  # создаем еще одного игрока
print("Положение игрока:", pl1.number, pl1.position)
print("Положение игрока:", pl2.number, pl2.position)
pl1.move(100, 100)  # скомандуем игроку переместиться
print("Положение игрока 1:", pl1.position)
pl2.move(30, 40)
print(pl2)  # используем метод __str__ для вывода

# вторая команда "green"
pl3 = Player("1", "green")
pl4 = Player("2", "green")
pl3.move(310, 40)
pl4.move(350, 350)

b = Ball(x=250, y=250)
b.speed = [1, 0]
g1 = Gate(380, 250)
g2 = Gate(230, 350)
g3 = GateCenter(10, g1, g2)

if __name__ == '__main__':
    pygame.init()
    scr = pygame.display.set_mode((400, 400))

    all_sprites = pygame.sprite.Group()  # группа для всех "спрайтов"
    all_sprites.add([pl1, pl2])
    all_sprites.add([pl3, pl4])
    all_sprites.add(b)
    all_sprites.add([g1, g2, g3])
    all_sprites.update()

    team_1 = pygame.sprite.Group([pl1, pl2])
    team_2 = pygame.sprite.Group([pl3, pl4])
    players = pygame.sprite.Group([team_1, team_2])

    # основной цикл игры
    while True:
        # обработка пользовательских событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # работаем с игроками
        b.check_collision(all_sprites)
        for pl in players:
            pl.check_collision(players)
            pl.check_collision(pygame.sprite.Group(b))

        pl1.move(1, 1)
        pl3.move(0, 1)
        b.move(dt=1)

        # отрисовываем картинку
        scr.fill("white")
        all_sprites.update()
        all_sprites.draw(scr)
        pygame.display.update()
        pygame.time.delay(20)


class TestClass:
    def __init__(self, x=0):
        self.__x = x

    def get_x(self):
        return self.__x
