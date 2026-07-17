# Завдання 3.3 Розділення списку на два
# Task 3.3 Splitting a list into two


elements = input("Введіть елементи списку: ").split()
middle = (len(elements) + 1) // 2
result = [elements[:middle], elements[middle:]]

print(result)