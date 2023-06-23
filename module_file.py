import module_book
import module_print
def choice(command: str) -> None:
    command.lower()
    if command == "w":
        path = input("Введите название файла который хотите открыть: ")
        return create_write_data(path)
    elif command == "a":
        return write_data(path)

    elif command == "quit":
        module_print.message_info_finish()  # Выход с программы
        quit()


# def read_test() -> None:
#     x = print("1")
#     return x



def create_write_data(path: str) -> None:

    try:
        file = open(path, "w")
        module_book.add_new_book(file) # создание книги
    except FileNotFoundError:
        print("Ошибка файл не найден, хотите создать новый?", end="")
        answer = input("y/n\n>> ")
        answer.lower()
        if answer == "y":
            create_file()
        elif answer == "n":
            choice()
        else:
            print("Вы не верно ввели y или n")
    finally:
        file.close()


def write_data(path: str, value: str) -> None:
    x = print("2")
    return x


def create_file(path: str, file_name: str, value=None) -> bool:
    pass


def delete_file(path: str) -> bool:
    pass