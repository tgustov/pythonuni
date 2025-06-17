n = int(input("Введите число чисел первого списка "))
m = int(input("Введите число чисел второго списка "))
list1 = []
list2 = []

# test = int(input("Введите число"))
# list1.append(test)
# print(list1)

if n < 1 or n > 100000 or m < 1 or m > 100000:
    print("Диапазон от 1 до 100000 ")
else:
    for i in range(n):
        number = int(input("Введите число для первого списка "))
        list1.append(number)

    for i in range(m):
        number = int(input("Введите число для вторго списка "))
        list2.append(number)

    print(f'Первый список {list1}')
    print(f'Второй список {list2}')
    print(f'Количество чисел вместе {len(list1)+len(list2)}')