from student import Student
from group import Group
from exceptions import GroupOverflowError


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student

# Перевірка власного винятку GroupOverflowError
gr2 = Group('PD2')
for i in range(10):
    gr2.add_student(Student('Male', 20, f'Name{i}', f'Surname{i}', f'AN{i}'))

try:
    gr2.add_student(Student('Male', 20, 'Extra', 'Student', 'AN999'))
except GroupOverflowError as e:
    print(f'Помилка: {e}')

print('ОК')
