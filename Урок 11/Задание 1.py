def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_sequence(start_num):
    initial_factorial = factorial(start_num)
    result = []
    for num in range(initial_factorial, 0, -1):
        result.append(factorial(num))

    return result



input_num = 3
output_list = factorial_sequence(input_num)
print(output_list) 