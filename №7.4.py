def common_elements() -> set[int]:
   
    multiples_of_3 = {n for n in range(100) if n % 3 == 0}
    multiples_of_5 = {n for n in range(100) if n % 5 == 0}
    return multiples_of_3 & multiples_of_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
