from datetime import datetime
import module_file

def message_info_start() -> None:
    print(f"{datetime.now()} \033[36m Info: \033[0m Приложение для работы с книгами запущено")


def message_info_finish() -> None:
    print(f"{datetime.now()} \033[36m Info: \033[0m Приложение для работы с книгами завершено")


def message_info_help() -> None:
    print(f"\nПожалуйста выберите действие: \n \033[36m 'w' \033[0m на создание нового файла с книгами или открытие файла с удалением данных в нем \n \033[36m 'a' \033[0m открытие на дозаписование в конце файла\n \033[36m 'quit' \033[0m для выхода из программы\n")


def message_action() -> None:
    command = input("Введите действие \n>> ")
    module_file.choice(command)
