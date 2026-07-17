# Завдання 3 Найпростіший калькулятор / Simple calculator



number_1 = int(input("Ведіть перше число: "))


mathematical_operation = input("Ведіть математичну операцію: (+, -, *, /) ")


number_2 = int(input("Ведіть друге число: "))

# перевірка на 0  / check for 0
if mathematical_operation == "/" and number_2 == 0:
    print("Дільник не може дорівнювати 0!")
else:

 # результат / result  
    match mathematical_operation:
        case "+":
            print("Результат: ", number_1 + number_2)
        case "-":
            print("Результат: ", number_1 - number_2)
        case "*":
            print("Результат: ", number_1 * number_2)
        case "/":
            print("Результат: ", number_1 / number_2)
        case _:
            print("Невідома операція")



