from itertools import product


user_input = input ("ведіть ціле число  ") 

# Перевірка на помилку: чи дійсно користувач ввів число, а не літери
if not user_input.isdigit():
    print ("Помилка: будь ласка, введіть саме ціле число.") 
else:
    # Перетворюємо рядок на число
    number = int(user_input)

# Цикл працює, поки число більше за 9
while number > 9:
    product = 1
    # Перетворюємо поточне число назад у рядок.
    for bigit in str(number):
        product *= int(bigit)
    number = product

print (f"Рузультат: {number}")
