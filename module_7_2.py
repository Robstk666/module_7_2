def custom_write(file_name: str, strings: list[str]) -> dict[tuple[int, int], str]:
    strings_positions = {}
    try:
        # Открываем файл с явным указанием, что не нужно преобразовывать символы новой строки
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            for line_number, line in enumerate(strings, start=1):
                byte_position = file.tell()
                # Явно добавляем '\r\n' для соответствия ожидаемому выводу
                file.write(line + '\r\n')
                strings_positions[(line_number, byte_position)] = line
    except FileNotFoundError as error:
        print(f"Ошибка: файл '{file_name}' не найден. {error}")
        raise
    except OSError as error:
        print(f"Ошибка ввода/вывода при работе с файлом '{file_name}'. {error}")
        raise
    return strings_positions

if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    try:
        result = custom_write('test.txt', info)
        for key, value in list(result.items()):
            print(f"(({key[0]}, {key[1]}), '{value}')")
    except Exception as error:
        print(f"Программа завершилась с ошибкой: {error}")