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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('John', 'Dou')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
 
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 7)
some_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(some_lecturer, 'Git', 10)
best_student.rate_lecturer(some_lecturer, 'Python', 8)
best_student.rate_lecturer(some_lecturer, 'Python', 10)
best_student.rate_lecturer(some_lecturer, 'Git', 6)
best_student.rate_lecturer(some_lecturer, 'Git', 10)
 
print(best_student.grades)
print(some_lecturer.grades['Git'])
print(some_reviewer)
print(some_lecturer)
print(best_student)
