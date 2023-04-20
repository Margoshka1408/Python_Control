def show_menu() -> str:
    print('*'*25)
    print('Журнал заметок:')
    print('*'*25)
    print('Выберите действие:')
    print('0 - Выйти из заметок')
    print('1 - Создать новую заметку')
    print('2 - Распечатать содержимое журнала заметок')
    print('3 - Выбрать заметку по названию')
    print('4 - Изменить поле(я) выбранной заметки')
    print('5 - Удалить заметку из журнала')
    print('6 - Импортировать данные из текстового файла')
    print('7 - Экспортировать данные в текстовый файл')

    return input('Введите действие: ')