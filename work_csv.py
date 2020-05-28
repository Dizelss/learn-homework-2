import csv


dictionary_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
with open("export_csv.csv", "w", encoding="utf-8") as f:
    fields = ["name", "age", "job"]
    writer = csv.DictWriter(f, fields, delimiter=";")
    writer.writeheader()
    for people in dictionary_list:
        writer.writerow(people)
