# 1. Квадрат числа
print("\n Розрахунок квадрата числа")
number = int(input("Введіть число: "))
print(f"Квадрат числа: {number ** 2}")

# 2. Середнє трьох чисел
print("\n Розрахунок середнього трьох чисел")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
print(f"Середнє: {(a + b + c) / 3}")

# 3. Перетворення хвилин у години
print("\n Перетворення хвилин у години")
minutes = int(input("Введіть кількість хвилин: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{hours} години {remaining_minutes} хвилин")

# 4. Розрахунок знижки
print("\n Розрахунок знижки")
price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
final_price = price * (1 - discount / 100)
print(f"Ціна зі знижкою: {final_price}")

# 5. Остання цифра числа
print("\n Остання цифра числа")
number = int(input("Введіть число: "))
print(f"Остання цифра: {number % 10}")

# 6. Периметр прямокутника
print("\n Розрахунок периметра прямокутника")
length = int(input("Введіть довжину: "))
width = int(input("Введіть ширину: "))
print(f"Периметр: {2 * (length + width)}")

# 7. Виведення числа в стовпчик
print("\n Виведення числа в стовпчик")
number = int(input("Введіть 4-х значне число: "))
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10
print(digit1)
print(digit2)
print(digit3)
print(digit4)
