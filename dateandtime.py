from datetime import date, datetime, timedelta
import calendar
import locale
locale.setlocale(locale.LC_TIME, "ru_RU")


# Выводим сегодняшнюю дату
today = date.today()
print(today.strftime("(%A) - %d.%m.%Y"))
# Выводим вчерашнюю дату
yesterday = today - timedelta(days=1)
print(yesterday.strftime("(%A) - %d.%m.%Y"))
# Выводим дату месяц назад
days = calendar.monthrange(today.year, today.month)[1]
month_ago = today - timedelta(days=days)
print(month_ago.strftime("(%A) - %d.%m.%Y"))

# Превратите строку "01/01/25 12:10:03.234567" в объект datetime
samedate = "01/01/25 12:10:03.234567"
formate_date = datetime.strptime(samedate, "%y/%m/%d %H:%M:%S.%f")
print(formate_date)
