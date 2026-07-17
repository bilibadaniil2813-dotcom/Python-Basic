# Завдання 3 Найпростіший калькулятор / Simple calculator

number_1 =(int(input("Ведіть перше число: ")))

if number_1  <= 0:
    print("Введіть число більше 0")
    exit()
а
    

mathematical_operation = input("Ведіть математичну операцію: (+, -, *, /) ")

number_2 =(int(input("Ведіть друге число: ")))


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

