# Консольний бот-помічник (книга контактів)
# Запуск:  python assistant.py
# Або імпорт:  from assistant import assistant_main


# Парсер команд користувача
def parse_input(user_input):

    #Розбиває введений користувачем рядок на команду та аргументи.
    #Наприклад: "add Petro 12345"  ->  команда 'add', аргументи ['Petro', '12345']

    # Видаляємо зайві пробіли і ділимо рядок на частини
    parts = user_input.strip().split()

    # Якщо користувач нічого не ввів — повертаємо порожні значення
    if not parts:
        return "", []

    # Перше слово — це команда, решта — аргументи
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

# Обробники команд

def add_contact(args, contacts):

    #Команда:  add <name> <phone>
    #Додає новий контакт у словник або перезаписує номер, якщо ім’я вже є.

    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):

    #Команда:  change <name> <new_phone>
    #Змінює номер телефону для існуючого контакту.

    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, new_phone = args

    # Перевіряємо, чи є таке ім’я у словнику
    if name not in contacts:
        return "Contact not found."

    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args, contacts):
    #Команда:  phone <name>
    #Виводить номер телефону за іменем контакту.

    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]

    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts):
    #Команда:  all
    #Виводить усі контакти зі словника у форматі: Name: phone

    if not contacts:
        return "No contacts."

    # Отримуємо список усіх імен і сортуємо їх за алфавітом
    names = list(contacts.keys())
    names.sort()

    # Формуємо список рядків для виводу
    lines = []
    for name in names:
        lines.append(f"{name}: {contacts[name]}")

    # Повертаємо всі рядки об’єднані символом нового рядка
    return "\n".join(lines)


# Основна логіка роботи бота

def assistant_main():
    #Основний цикл роботи.
    #Читає команду користувача, визначає її тип і виконує відповідну дію.
    #Завершує роботу після введення 'close' або 'exit'.

    # Словник для зберігання контактів у пам’яті
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        # Зчитуємо команду користувача
        user_input = input("Enter a command: ")

        # Отримуємо команду та аргументи
        command, args = parse_input(user_input)

        # Команди виходу ===
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Привітання
        elif command == "hello":
            print("How can I help you?")

        # Додавання нового контакту
        elif command == "add":
            print(add_contact(args, contacts))

        # Зміна номера телефону
        elif command == "change":
            print(change_contact(args, contacts))

        # Пошук номера за ім’ям
        elif command == "phone":
            print(show_phone(args, contacts))

        # Виведення всіх контактів
        elif command == "all":
            print(show_all(contacts))

        # Якщо команда не розпізнана
        else:
            print("Invalid command.")


# Точка входу при запуску
if __name__ == "__main__":
    # Якщо файл запущено напряму, запускаємо основний цикл
    assistant_main()