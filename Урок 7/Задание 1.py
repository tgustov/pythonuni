
word = input("Введите слово ").strip()
print("yes" if word == word[::-1] else "no")