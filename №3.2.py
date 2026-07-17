# Завдання 3.2 Перенесення останнього елемента на початок списку

elements = input("Введіть елементи списку через пробіл: ").split()

if len(elements) > 1:
    elements = [elements[-1]] + elements[:-1]

print(elements)
