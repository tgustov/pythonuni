

number = int(input("Введите целое число: "))

if number == 0:
    print("Нулевое число")
else:
    if number > 0:
        sign = "Положительное"
    else:
        sign = "Отрицательное"

    if number % 2 == 0:
        divider = "Четное"
        print(f"{sign} {divider} число")
    else:
        print("число не является четным")