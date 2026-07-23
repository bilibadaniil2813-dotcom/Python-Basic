# Завдання 3.2 Перенесення останнього елемента на початок списку 
# Task 3.2 Moving the last element to the beginning of the list

elements = input("Введіть елементи списку через пробіл: ").split()

if len(elements) > 1:
    elements = [elements[-1]] + elements[:-1]

print(elements) 
