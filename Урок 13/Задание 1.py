import random

start = input("Выберите матрицу либо 10x10 либо 4x3 ").strip()

def pl(t):
    print("\n")
    for i in t:
        print(i)

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j]
             for j in range(len(matrix1[0]))]
            for i in range(len(matrix1))]


if start == "10x10":
    m1 = [[random.randint(1, 10) for i in range(10)] for i in range(10)]
    m2 = [[random.randint(1, 10) for i in range(10)] for i in range(10)]
    result = add_matrices(m1, m2)
    pl(m1)
    pl(m2)
    pl(result)
elif start == "4x3":
    m1 = [[random.randint(1, 10) for i in range(4)] for i in range(3)]
    m2 = [[random.randint(1, 10) for i in range(4)] for i in range(3)]
    result = add_matrices(m1, m2)
    pl(m1)
    pl(m2)
    pl(result)
else:
    print("Ошибка, проверьте ввели ли вы правильное значение (x из английской раскладки)")

