n = int(input("Введите количество чисел "))
numbers = []

if n <= 1 or n >=100000:
    print("N должно быть в диапазоне от 1 до 100000")
else:
    for i in range(n):
        num = int(input("Введите число "))
        numbers.append(num)

    for x in numbers:
        if x >= 10e5 or x <= 1:
            print("Число не должно быть больше 10е9 или меньше 1")
            break
    else:
        print(numbers[-1:] + numbers[:-1])