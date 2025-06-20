class CashRegister:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def top_up(self, x):
        if x <= 0:
            return "Невозможно пополнить на сумму меньше 0"
        else:
            self.amount += x

    def count(self):
        return self.amount // 1000

    def take_away(self, x):
        if x <= 0:
            return "Невозможно снять сумму меньше 0"
        elif self.amount < x:
            return "Недостаточно денег в кассе"
        else:
            self.amount -= x


### Тестирование

test = CashRegister(2000)
print(f'Текущая сумма: {test.amount}')

test.top_up(1000)
print(f'Сумма после пополнения: {test.amount}')

print(f'Количество целых тысяч: {test.count()}')

test.take_away(1500)
print(f'Сумма после снятия: {test.amount} и количество целых тысяч после снятия: {test.count()}\n')

print("Тестирование ошибок")

error = CashRegister(1000)

print(f'Текущая сумма: {error.amount}')

print(f'Сумма после пополнения: {error.top_up(-1000)}')

print(f'Сумма после снятия: {error.take_away(-1500)}')

print(f'Сумма после снятия: {error.take_away(10000)}')