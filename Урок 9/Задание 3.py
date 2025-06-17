numbers = list(map(int, input("Введите числа через пробел").split()))
seen = set()
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)