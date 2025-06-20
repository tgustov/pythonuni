class Turtle:

    def __init__(self, x=0, y=0, s=1):
        self.horizontal = x
        self.vertical = y
        self.speed = s

    def go_up(self):
        self.vertical += self.speed

    def go_down(self):
        self.vertical -= self.speed

    def go_left(self):
        self.horizontal -= self.speed

    def go_right(self):
        self.horizontal += self.speed

    def evolve(self):
        self.speed += 1

    def degrade(self):
        self.speed -=1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.horizontal)
        dy = abs(y2 - self.vertical)
        steps_x = dx // self.speed + (1 if dx % self.speed != 0 else 0)
        steps_y = dy // self.speed + (1 if dy % self.speed != 0 else 0)
        return steps_x + steps_y

turtle = Turtle(0, 0, 1)

turtle.go_up()
print(f"Позиция после движения вверх: ({turtle.horizontal}, {turtle.vertical})")

turtle.go_right()
print(f"Позиция после движения вправо: ({turtle.horizontal}, {turtle.vertical})")

turtle.evolve()
print(f"Шаг после evolve: {turtle.speed}")

try:
    turtle.degrade()
    print(f"Шаг после degrade: {turtle.speed}")
except ValueError as e:
    print(f"Ошибка: {e}")

x2, y2 = 2, 2
moves = turtle.count_moves(x2, y2)
print(f"Минимальное число ходов до ({x2}, {y2}) (С учетом прошлой позиции ({turtle.horizontal}, {turtle.vertical}) и скоростью {turtle.speed}): {moves}")