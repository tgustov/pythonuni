n = int(input("Введите число чисел "))
if n < 1 or n > 100000:
    print("Диапазон от 1 до 100000 ")
else:
    numbers = list(map(int, input("Введите числа через пробел ").split()))
    unique_numbers = set(numbers)
    for x in unique_numbers:
        if x > 2*10e9:
            print("Число не может быть больше 2*10e9")
            break

    print(len(unique_numbers))

