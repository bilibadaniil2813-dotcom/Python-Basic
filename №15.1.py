class GroupOverflowError(Exception):
    """Виняток, що виникає при спробі додати більше 10 студентів у групу."""
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, record book: {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupOverflowError(f'У групі не може бути більше {self.MAX_STUDENTS} студентів')
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '


gr = Group('PD1')

for i in range(10):
    gr.add_student(Student('Male', 20, f'Name{i}', f'Surname{i}', f'AN{i}'))

print(f'Студентів у групі: {len(gr.group)}')  # 10

try:
    gr.add_student(Student('Male', 20, 'Extra', 'Student', 'AN999'))
except GroupOverflowError as e:
    print(f'Помилка: {e}')

print(f'Студентів у групі: {len(gr.group)}')  # все ще 10
print('ОК')