def function1():
    """
    Функция, которая читает файл "data.txt" и записывает в файл "res1.txt" строки,
    длина которых (без учета пробелов) меньше заданного значения n.
    """
    n = int(input())
    with open("data.txt", "r", encoding="utf-8") as source_file, open("res.txt", "w", encoding="utf-8") as dest_file:
        for line in source_file:
            if len(line.strip()) < n:
                dest_file.write(line)
                print(line)

def function2():
    """
    Функция, которая читает файл "data.txt" и записывает в файл "res2.txt"
    количество слов в каждой строке, а также общее количество строк.
    """
    with open("data.txt", "r", encoding="utf-8") as source_file, open("res2.txt", "w", encoding="utf-8") as dest_file:
        x = 0  # Счетчик строк
        for line in source_file:
            x += 1
            y_temp = line.split()
            y = len(y_temp)
            dest_file.write(f"Строка - {x}: слов: {y}\n")
        dest_file.write(f"Всего строк - {x}\n")

def function3():
    """
    Функция, которая читает файл "data.txt" и записывает в файл "res3.txt"
    строки с удалением лишних пробелов.
    """
    with open("data.txt", "r", encoding="utf-8") as source_file, open("res3.txt", "w", encoding="utf-8") as dest_file:
        for line in source_file:
            cleaned_line = ""
            fspace = False  # Флаг, указывающий на наличие пробела
            for char in line:
                if char == " ":
                    if not fspace:
                        cleaned_line += " "
                        fspace = True
                else:
                    cleaned_line += char
                    fspace = False
            dest_file.write(cleaned_line)

def function4():
    """
    Функция, которая читает файл "data.csv" и записывает в файл "res4.txt"
    названия книг заданного автора, написанных до 2019 года.
    """
    author_name = input("Фамилия автора: ")
    books = []
    with open("data.csv", "r", encoding='windows-1251') as source_file, open("res4.txt", "w", encoding='utf-8') as dest_file:
        next(source_file)  # Пропускаем заголовок
        for line in source_file:
            parts = line.strip().split(';')
            if len(parts) >= 3:
                surname, title, year = parts
                year = int(year)
                if surname == author_name and year < 2019:
                    books.append(title)
                    print(title)
        if books:
            dest_file.write('\n'.join(books))
        else:
            dest_file.write("Книги автора до 2019 не найдены.")

def function5():
    """
    Функция, которая читает файл "data5.txt" и записывает в файл "res5.txt"
    текст, заключенный в скобки в каждой строке.
    """
    with open("data5.txt", "r", encoding="utf-8") as source_file, open("res5.txt", "w", encoding="utf-8") as dest_file:
        for line_number, line in enumerate(source_file, 1):
            start_index = line.find('(')
            if start_index != -1:
                end_index = line.find(')', start_index)
                if end_index != -1:
                    extracted_text = line[start_index + 1:end_index]
                    dest_file.write(f"Line {line_number}: {extracted_text}\n")

if name == 'main':
    function1()
    function2()
    function3()
    function4()
    function5()
