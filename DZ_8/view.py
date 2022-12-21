def main_menu():
    print('\n1. Показать телефонную книгу')
    print('2. Открыть файл телефонной книги')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choise_main_menu()


def choise_main_menu():                 # try - except - без break - тогда можно через while True
    while True:
        try:
            choice = int(input('Выберите команду из меню: '))
            if choice in range(0, 8):
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные!')


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('\nТелефонная книга пуста или не загружена')


def log_off():
    print('До свидания, до новых встреч!')


def load_success():
    print('\nТелефонная книга загружена')


def save_success():
    print('Телефонная книга сохранена!')


def remove_success():
    print('Контакт удален!')


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [f'{name}, {phone}, {comment}']


def input_remove_contact():
    id = int(input('Введите ID контакта, который желаете удалить: '))
    return id


def input_find_contact():
    find = input('Введите имя контакта или номер телефона, который Вы хотите найти: ')
    return find



def input_change_contact():
    id = int(input('Введите ID контакта, который желаете измениь: '))
    return id