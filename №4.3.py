import random

list_length = random.randint(3, 10)

numbers = []

for _ in range(list_length):
    random_number = random.randint(0, 100)
    numbers.append(random_number)

result = [numbers[0], numbers[2], numbers[-2]]

print("Початковий список:", numbers)
print("Новий список:", result)
