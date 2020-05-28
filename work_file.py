# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

def open_file(file_name):
    with open(file_name, "r", encoding="utf-8") as text:
        text_all = text.read()
        return text_all

def save_file(file_name, text_whis_exclamation=0):
    with open(file_name, "w", encoding="utf-8") as text:
        text.write(text_whis_exclamation)
        print("Файл перезаписан!")

def count_lenght_string(text_all):
    return len(text_all)

def point_to_exclamation(text_all):
    text_whis_exclamation = text_all.replace(".", "!")
    return text_whis_exclamation


if __name__ == "__main__":
    result_read = open_file("referat.txt")
    print(f"Длина всей строки файла: {count_lenght_string(result_read)}")
    result_for_save = point_to_exclamation(result_read)
    save_file("referat.txt", result_for_save)
