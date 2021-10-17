class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {Lecturer.av_rate(self)}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nПройденные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Reviewer):
            print("Неподходящая персона для сравнения")
            return
        return Lecturer.av_rate(self) < Lecturer.av_rate(other)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
class Lecturer(Mentor):
    def av_rate(self):
        total = 0
        n = 0
        for key, value in self.grades.items():
            for grade in value:
                total += grade
                n += 1
        res = total/n
        return res
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rate()}'
        return res

    def __lt__(self, other):
        if isinstance(other, Reviewer):
            print("Неподходящая персона для сравнения")
            return
        return self.av_rate() < Lecturer.av_rate(other)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.add_courses('CSS')

some_student = Student('Nik', 'Piteson', 'man')
some_student.courses_in_progress += ['Java']
some_student.courses_in_progress += ['Python']
some_student.add_courses('HTML')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

some_reviewer = Reviewer('Ammy', 'Mihaello')
some_reviewer.courses_attached += ['Java']

cool_lecturer = Lecturer('Vinni', 'Pyh')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

some_lecturer = Lecturer('Alex', 'Ronin')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Java']


cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

some_reviewer.rate_hw(best_student, 'Java', 5)
some_reviewer.rate_hw(best_student, 'Java', 7)
some_reviewer.rate_hw(best_student, 'Java', 9)

cool_reviewer.rate_hw(some_student, 'Python', 8)
cool_reviewer.rate_hw(some_student, 'Python', 8)
cool_reviewer.rate_hw(some_student, 'Python', 6)

some_reviewer.rate_hw(some_student, 'Java', 10)
some_reviewer.rate_hw(some_student, 'Java', 6)
some_reviewer.rate_hw(some_student, 'Java', 10)

best_student.rate_lecturer(cool_lecturer, 'Python', 6)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 6)
some_student.rate_lecturer(cool_lecturer, 'Java', 8)
some_student.rate_lecturer(cool_lecturer, 'Java', 9)
some_student.rate_lecturer(cool_lecturer, 'Java', 7)

some_student.rate_lecturer(some_lecturer, 'Python', 8)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 8)
best_student.rate_lecturer(some_lecturer, 'Java', 6)
best_student.rate_lecturer(some_lecturer, 'Java', 10)
best_student.rate_lecturer(some_lecturer, 'Java', 6)


st_list = [best_student, some_student]
lect_list = [cool_lecturer, some_lecturer]

def av_grade_all(rating_list, course):
    total = 0
    n = 0
    for member in rating_list:
        for key, grades in member.grades.items():
            if key == course:
                total += sum(grades)
                n += len(grades)
    return total/n
print(best_student.grades)
print(some_student.grades)
print(cool_lecturer.grades)
print(some_lecturer.grades)
print(best_student)
print(some_student)
print(cool_reviewer)
print(some_reviewer)
print(cool_lecturer)
print(some_lecturer)
print(best_student < some_student)
print(some_lecturer < cool_lecturer)
print(av_grade_all(st_list, 'Python'))
print(av_grade_all(st_list, 'Java'))
print(av_grade_all(lect_list, 'Python'))
print(av_grade_all(lect_list, 'Java'))