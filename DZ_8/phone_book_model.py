import view

phone_book = []


def get_phone_book():                      # получение телефонной книги
    global phone_book
    return phone_book


def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book


def add_contact(contact: list):            # добавить контакт
    global phone_book                      # берем список ТЕЛКНИГУ
    phone_book.append(contact)             # добавляем контакт в ТЕЛКНИГУ


def remove_contact(id):                    # удалить контакт
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False


def change_contact():
    global phone_book
    id = view.input_change_contact()
    confirm = input(f'Вы уверены, что хотите изменить контакт {phone_book[id - 1][0]}? (yes/no)')
    if confirm.lower() == 'yes':
        del_contact = phone_book.pop(id - 1)
        change_contact = view.input_new_contact()
        phone_book.insert(id-1, change_contact)


def find_contact():
    global phone_book
    find = view.input_find_contact()
    count = 0
    for contact in phone_book:
        for item in contact:
            if find.lower() in item.lower():
                print(contact)
                count += 1
    if count == 0:
        print('\nКонтакта с такими данными отсутствует в списке!!!')




def change_contact():
    global phone_book
    id = view.input_change_contact()
    confirm = input(f'Вы уверены, что хотите изменить контакт {phone_book[id - 1][0]}? (yes/no): ')
    if confirm.lower() == 'yes':
        del_contact = phone_book.pop(id - 1)
        change_contact = view.input_new_contact()
        phone_book.insert(id-1, change_contact)