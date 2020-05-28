# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

def work_this_file(file_name, action_file, text_whis_exclamation=0):
    with open(file_name, action_file, encoding="utf-8") as text:
        if action_file == "r":
            text_all = text.read()
            return text_all
        if action_file == "w":
            text.write(text_whis_exclamation)
            print("Файл перезаписан!")

def count_lenght_string(text_all):
    return len(text_all)

def point_to_exclamation(text_all):
    text_whis_exclamation = text_all.replace(".", "!")
    return text_whis_exclamation


if __name__ == "__main__":
    result_read = work_this_file("referat.txt", "r")
    print(f"Длина всей строки файла: {count_lenght_string(result_read)}")
    result_for_save = point_to_exclamation(result_read)
    work_this_file("referat.txt", "w", result_for_save)
