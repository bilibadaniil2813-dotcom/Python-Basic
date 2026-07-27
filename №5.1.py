import keyword
import string

user_input = input("Введіть ім'я змінної: ")

# Список заборонених символів пунктуації (всі пунктуації з string, окрім '_')
invalid_punctuation = string.punctuation.replace("_", "")

# Початково припускаємо, що ім'я валідне
is_valid = True

# 1. Перевірка на порожній рядок
if not user_input:
    is_valid = False

# 2. Перевірка на зарезервоване слово (БЕЗ "not")
elif user_input in keyword.kwlist:
    is_valid = False

# 3. Перевірка на подвійне підкреслення "__" поспіль
elif "__" in user_input:
    is_valid = False

# 4. Перевірка на першу цифру
elif user_input[0].isdigit():
    is_valid = False

# 5. Перевірка кожного символу на великі літери, пробіли та пунктуацію
else:
    for char in user_input:
        if char.isupper() or char.isspace() or char in invalid_punctuation:
            is_valid = False
            break

print(is_valid)


