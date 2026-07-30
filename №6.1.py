# Діапазон букв / Range of letters

import string

input_str = input("Введіть дві літери через дефіс (наприклад, a-c): ").strip()

# Перевірка на базову коректність формату (наявність дефісу та правильна кількість елементів)
# Check for basic format correctness (presence of hyphen and correct number of elements)
if '-' in input_str and len(input_str.split('-')) == 2:
    start_char, end_char = input_str.split('-')
    letters = string.ascii_letters

    # Перевірка, чи обидва введені символи є латинськими літерами
    # Check if both entered characters are Latin letters
    if start_char in letters and end_char in letters:
        start_index = letters.index(start_char)
        end_index = letters.index(end_char)

        # Перевірка, що початковий індекс не більший за кінцевий
        # Check that the start index is not greater than the end index
        if start_index <= end_index:
            print(letters[start_index:end_index + 1])
        else:
            print("Помилка: перша літера повинна йти в алфавіті перед другою або бути такою ж (враховуючи регістр).")
    else:
        print("Помилка: введіть лише латинські літери.")
else:
    print("Помилка: невірний формат. Будь ласка, використовуйте дефіс між двома літерами.")
