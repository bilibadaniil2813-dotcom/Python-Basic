numbers = [0, 1, 7, 2, 4, 8]

if not numbers:
    result = 0
else:
    even_index_sum = 0
    
    for index in range (0, len(numbers),2):
        even_index_sum += numbers[index]
    print (numbers)
    
    result = even_index_sum * numbers [-1]

print (result)