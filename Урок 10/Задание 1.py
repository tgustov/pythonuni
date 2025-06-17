pets = {}

# Ввод информации о питомце
pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Добавление информации в словарь
pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

pet_info = pets[pet_name]
pet_type = pet_info['Вид питомца']
pet_age = pet_info['Возраст питомца']
owner_name = pet_info['Имя владельца']
age_suffix = get_age_suffix(pet_age)

info_string = f'Это {pet_type.lower()} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}'
print(info_string)

