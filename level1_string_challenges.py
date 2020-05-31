from collections import Counter


# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последняя буква в слове: {word[-1]}")

# Вывести количество букв "а" в слове
word = 'Архангельск'
word = list(word.lower())
result = Counter(word)
print(f"Букв А в слове: {result['а']}")

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ["а", "я", "о", "е", "у", "ю", "ы", "и", "й", "э", "е", "ё"]
word = list(word.lower())
counter = 0
for letter_in_word in word:
    for letter_in_vowels in vowels:
        if letter_in_word == letter_in_vowels:
             counter += 1
print(f"Гласных букв в слове: {counter}")

# # Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(" ")
print(f"Кол-во слов в предложении: {len(words)}")

# # Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(" ")
for word in words:
    print(word[0])

# # Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split(" ")
count_len_word = 0
for word in words:
    count_len_word += len(word)
middle_count = count_len_word / len(words)
print(f"Усредненная длина слова {middle_count}")
