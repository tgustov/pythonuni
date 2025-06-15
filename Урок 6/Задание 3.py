

a = int(input('Введите меньшее число '))
b = int(input('Введите большее число '))
result = []

if a > b:
    print("Первое число должно быть меньше второго")
else:
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(str(i))
    else:
        print(' '.join(result))
