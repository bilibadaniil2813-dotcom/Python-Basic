#Конвертер із числа в дату
total_seconds = int(input("Введіть кількість секунд (від 0 до 8639999): "))

# 1. Обчислення днів, годин, хвилин та секунд
days, remainder = divmod(total_seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)

# 2. Правильне відмінювання слова "день"
if days % 10 == 1 and days % 100 != 11:
    day_word = "День"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20 ):
    day_word = "Дні"
else:
    day_word = "Днів"

# 3. Форматування часу з провідними нулями

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(f" {days} {day_word} {hours_str}:{minutes_str}:{seconds_str}")