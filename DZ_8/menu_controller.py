import view
import phone_book_model as pb
import data_base as db


def main_menu(choice: int):
    match choice:
        case 1:
            phone_book = pb.get_phone_book()    # получение тел.книги 
            view.print_phone_book(phone_book)   # распечатка телефонной книги в консоли
        case 2:
            db.load_data_base()                 # загрузить тел.книгу из файла
            view.load_success()                 # печать "ТЕЛЕФОННАЯ КНИГА ЗАГРУЖЕНА"
        case 3:
            db.save_data_base()                 # сохранить тел. книгу в файл
            view.save_success()                 # печать "ТЕЛЕФОННАЯ КНИГА СОХРАНЕНА!"
        case 4:
            contact = view.input_new_contact()  # создание элемента в списке тел.книги
            pb.add_contact(contact)             # добавление контакта в тел. книгу
        case 5:
            phone_book = pb.get_phone_book()
            pb.change_contact()

        case 6:
            phone_book = pb.get_phone_book()    # получение телефонной книги
            view.print_phone_book(phone_book)   # распечатка телефонной книги в консоли, т.е.отображение перед удалением
            id = view.input_remove_contact()    # получение ID для удаления (вводим с клавы)
            if pb.remove_contact(id):           # удаление самой записи
                view.remove_success()           # печать "КОНТАКТ УДАЛЕН"
        case 7:
            phone_book = pb.get_phone_book()
            pb.find_contact()               
 
        case 0:
            return True


def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break
