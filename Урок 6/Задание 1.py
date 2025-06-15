

number = int(input("Введите целое число: "))
count = 0

for x in range(number):
    num = int(input())
    if num == 0:
        count += 1

print(f'Количество нулей {count}')