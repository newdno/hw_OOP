class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')
        
    def average_grade(self):
        av_grade = 0
        all_grades = []
        for a in self.grades.values():
            all_grades.extend(a)
        if all_grades:
            av_grade = round(sum(all_grades)/len(all_grades),1)
        return av_grade
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return 'Ошибка'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return(f'Имя: {self.name} \nФамилия: {self.surname}')

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
  
    def __str__(self):
        return (f'{super().__str__()} \nСредняя оценка за лекции: {self.average_grade()}')
   
    def average_grade(self):
        av_grade = 0
        all_grades = []
        for a in self.grades.values():
            all_grades.extend(a)
        if all_grades:
            av_grade = round(sum(all_grades)/len(all_grades),1)
        return av_grade
  
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return 'Ошибка'
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return super().__str__()

def average_student_hw_by_course(students, course):
    grades = []
    avr_h = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grades.extend(student.grades.get(course, []))
    if grades:
        avr_h = sum(grades)/len(grades)
    return avr_h
        
def average_rate_of_lecturer_by_course(lecturers, course):
    grades = []
    avr_r = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grades.extend(lecturer.grades.get(course, []))
    if grades:
        avt_r = sum(grades)/len(grades)
    return avr_r

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
some_student = Student('Ann', 'Lee', '-')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']

 
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Any', 'Buddy')
reviewer_2.courses_attached += ['Git']

lecturer_1 = Lecturer('John', 'Dou')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
lecturer_2 = Lecturer('Jane', 'Dou')
lecturer_2.courses_attached += ['Git']
 
reviewer_1.rate_hw(best_student, 'Python', 8)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_2.rate_hw(best_student, 'Git', 9)
reviewer_1.rate_hw(some_student, 'Python', 5)
reviewer_1.rate_hw(some_student, 'Python', 7)


best_student.rate_lecturer(lecturer_1, 'Git', 10)
best_student.rate_lecturer(lecturer_1, 'Python', 8)
best_student.rate_lecturer(lecturer_1, 'Python', 10)
best_student.rate_lecturer(lecturer_1, 'Git', 6)
best_student.rate_lecturer(lecturer_2, 'Git', 10)
some_student.rate_lecturer(lecturer_2, 'Git', 6)
some_student.rate_lecturer(lecturer_1, 'Python', 10)
 
print(best_student)
print(some_student)
#print(lecturer_1.grades['Git'])
print(reviewer_1)
print(lecturer_1)
print(some_student < best_student)
print(lecturer_1 < lecturer_2)
print(f'{lecturer_1.average_grade()}, {lecturer_2.average_grade()}')

print(f'Средняя оценка за домашние задания: {average_student_hw_by_course([best_student, some_student], "Python")}')
