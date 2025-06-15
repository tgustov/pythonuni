n = int(input("Введите количество чисел "))
numbers = []

if n <= 1 or n >=10000:
    print("N должно быть в диапазоне от 1 до 10000")
else:
    for i in range(n):
        num = int(input("Введите число "))
        numbers.append(num)

    for x in numbers:
        if x >= 10e5:
            print("Число не должно быть больше 10е5")
            break

    else:
            reversed_numbers = numbers[::-1]
            for num in reversed_numbers:
                print(num)