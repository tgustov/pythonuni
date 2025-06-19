import collections


pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"


def get_pet(ID):
    return pets[ID] if ID in pets else False


def pets_list():
    print("\nСписок всех питомцев:")
    for pet_id, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        print(f"ID: {pet_id}, Кличка: '{pet_name}'")


def create():
    last_id = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last_id + 1

    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }
    print(f"\nПитомец '{pet_name}' успешно добавлен под ID {new_id}!")


def read(pet_id):
    pet_info = get_pet(pet_id)
    if not pet_info:
        print(f"\nПитомец с ID {pet_id} не найден!")
        return

    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    age = pet_data["Возраст питомца"]
    suffix = get_suffix(age)

    print(f'\nЭто {pet_data["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {age} {suffix}. '
          f'Имя владельца: {pet_data["Имя владельца"]}')


def update(pet_id):
    pet_info = get_pet(pet_id)
    if not pet_info:
        print(f"\nПитомец с ID {pet_id} не найден!")
        return

    pet_name = list(pet_info.keys())[0]
    print(f"\nОбновление информации для питомца '{pet_name}':")

    new_type = input(f"Вид питомца ({pet_info[pet_name]['Вид питомца']}): ") or pet_info[pet_name]['Вид питомца']
    new_age = input(f"Возраст питомца ({pet_info[pet_name]['Возраст питомца']}): ") or pet_info[pet_name][
        'Возраст питомца']
    new_owner = input(f"Имя владельца ({pet_info[pet_name]['Имя владельца']}): ") or pet_info[pet_name]['Имя владельца']

    pets[pet_id][pet_name] = {
        "Вид питомца": new_type,
        "Возраст питомца": int(new_age),
        "Имя владельца": new_owner
    }
    print(f"\nИнформация о питомце '{pet_name}' успешно обновлена!")


def delete(pet_id):
    pet_info = get_pet(pet_id)
    if not pet_info:
        print(f"\nПитомец с ID {pet_id} не найден!")
        return

    pet_name = list(pet_info.keys())[0]
    del pets[pet_id]
    print(f"\nПитомец '{pet_name}' (ID {pet_id}) успешно удален!")


def main():
    print("Добро пожаловать в базу данных питомцев!")
    print("Доступные команды: create, read, update, delete, list, stop")

    while True:
        command = input("\nВведите команду: ").lower()

        if command == "stop":
            print("Работа с базой данных завершена.")
            break

        elif command == "create":
            create()

        elif command == "read":
            pet_id = int(input("Введите ID питомца: "))
            read(pet_id)

        elif command == "update":
            pet_id = int(input("Введите ID питомца: "))
            update(pet_id)

        elif command == "delete":
            pet_id = int(input("Введите ID питомца: "))
            delete(pet_id)

        elif command == "list":
            pets_list()

        else:
            print("Неизвестная команда! Попробуйте снова.")


if __name__ == "__main__":
    main()