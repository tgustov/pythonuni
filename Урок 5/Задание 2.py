

word = input("Введите слово из маленькиз латинских букв: ").lower()

vowels = {'a', 'e', 'i', 'o', 'u'}

consonant_count = 0
vowel_count = 0
vowel_stats = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_stats[letter] += 1
    else:
        consonant_count += 1

print(f"Гласных: {vowel_count}")
print(f"Согласных: {consonant_count}")

print("\nКоличество каждой гласной:")
for vowel in vowel_stats:
    if vowel_stats[vowel] == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {vowel_stats[vowel]}")