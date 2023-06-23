import module_print
def choice_action_book():
    pass

def add_new_book(file: str):
    text = ""
    d = {0: "название книги", 1: "автора", 2: "год издания", 3: "жанр"}
    d1 = {0: " ", 1: " ", 2: " ", 3: "\n"}
    d2 = {0: "", 1: "", 2: "", 3: ""}
    d3 = {0: "Книга с названием", 1: "Автор", 2: "Год издания", 3: "Жанр"}
    while True:
        for i in range(4):
            x = input(f"Введите {d[i]}, или \033[36mстоп\033[0m для выхода из программы \n>> ")
            x.lower()
            if x == "стоп":
                module_print.message_info_finish() # Выход с программы
                quit()
            d2[i] = x
            text = text + x + f"{d1[i]}"
        print(f"\nВы добавили:")
        for i in range(4):
            print(f"{d3[i]}: \033[36m{d2[i]}\033[0m;")
        choice_v = input(f"\nХотите добавить \033[36mкнигу\033[0m в файл, если нет, то введите \033[36mотмена\033[0m для исправления ошибки \n>> ")
        choice_v.lower()
        if choice_v != "отмена":
            file.write(text)
        text = ""


