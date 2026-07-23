numbers = [2, 4, 13, 0, 48, 0, 85, 0, 0]

non_zero_numbers = []

for number in numbers:
    if number != 0:
        non_zero_numbers.append (number)
    
zero_count = numbers.count (0)

numbers = non_zero_numbers + [0] * zero_count

print (numbers)