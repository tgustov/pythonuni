# Пятизначное число
number = 46275

# Число на цифры
tens_of_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

# Вычисление
step1 = tens ** ones
step2 = step1 * hundreds
denominator = tens_of_thousands - thousands

result = step2 / denominator

print(result)  # Выводим результат