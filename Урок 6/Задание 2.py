

X = int(input("Введите целое чилсло "))
count = 0
for i in range(1, X + 1):
    if X % i == 0:
        count += 1
        print(i)
print(f'Число делителей {count}')