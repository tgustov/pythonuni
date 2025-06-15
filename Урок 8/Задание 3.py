m = int(input('Сколько выдерживает лодка '))
n = int(input("Количество рыбаков "))
weights = [int(input("Индивидуальный вес рыбака ")) for i in range(n)]
weights.sort()

left = 0
right = n - 1
boats = 0

if m <= 1 or m >= 10e6 or n <= 1 or n>= 100:
    print("Вес должен быть от 1 до 10е6 или количество рыбаков за рамками 1-100")
else:
    while left <= right:
        if weights[left] + weights[right] <= m:
            left += 1
        right -= 1
        boats += 1

print(boats)