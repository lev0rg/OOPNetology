class Student:
    def __init__(self, name, surname, gender):                                                                                  
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_stud = {}

    def grade_lecturer(self, lecturer, course, grade):                                                                         
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lect:
                lecturer.grades_lect[course] += [grade]
            else:
                lecturer.grades_lect[course] = [grade]
        else:
            return 'Ошибка'
        
    def avg_grade_stud(self):
        avg = []
        for grade in self.grades_stud.values():
            avg.extend(grade)
        return sum(avg) / len(avg)
    
    def __str__(self):
        avg_stud = self.avg_grade_stud()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {"{:.1f}".format(avg_stud)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {"".join(self.finished_courses)}\n')
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.avg_grade_stud() < other.avg_grade_stud()
    

class Mentor:                                                                                                                    
    def __init__(self, name, surname):                                                                                           
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):                                                                                                          
    def __init__(self, name, surname):
        super().__init__(name, surname)                                                                                                        
        self.grades_lect = {}

    def avg_grade_lect(self):
        avg = []
        for grade in self.grades_lect.values():
            avg.extend(grade)
        return sum(avg) / len(avg)

    def __str__(self):
        avg_lect = self.avg_grade_lect()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {"{:.1f}".format(avg_lect)}'
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_grade_lect() < other.avg_grade_lect()
    

class Reviewer(Mentor):                                                                                                         
    def grade_student(self, student, course, grade):                                                                            
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades_stud:
                student.grades_stud[course] += [grade]
            else:
                student.grades_stud[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

#Создание экземпляров студентов      
some_student = Student('Ruoy', 'Eman', 'Male')
another_student = Student('Ivan', 'Ivanov', 'Male')
some_student.courses_in_progress += ['Python', 'Git']
another_student.courses_in_progress += ['Python', 'Javascript']
some_student.finished_courses += ['Введение в программирование']
another_student.finished_courses += ['Начало работы с Linux']

#Создание экземпляров лекторов
some_lecturer = Lecturer('Some', 'Buddy')
another_lecturer = Lecturer('Alex', 'Alexeev')
some_lecturer.courses_attached += ['Python', 'Javascript', 'Git']
another_lecturer.courses_attached += ['Python', 'Javascript', 'Git']

#Создание экземпляров проверяющих
some_reviewer = Reviewer('Some', 'Buddy')
another_reviewer = Reviewer('Sergey', 'Sergeev')
some_reviewer.courses_attached += ['Python', 'Javascript', 'Git']
another_reviewer.courses_attached += ['Python', 'Javascript', 'Git']

#Оценки студентам:
some_reviewer.grade_student(some_student, 'Python', 5)
another_reviewer.grade_student(some_student, 'Git', 5)
some_reviewer.grade_student(another_student, 'Python', 8)
another_reviewer.grade_student(another_student, 'Javascript', 8)

#Оценки лекторам:
some_student.grade_lecturer(some_lecturer, 'Python', 4)
another_student.grade_lecturer(some_lecturer, 'Javascript', 4)
some_student.grade_lecturer(another_lecturer, 'Git', 2)
another_student.grade_lecturer(another_lecturer, 'Javascript', 3)

#Сравнение средней оценки студентов:
if some_student > another_student:
    print(f'Средняя оценка {some_student.name} {some_student.surname} лучше чем у {another_student.name} {another_student.surname}')
else:
    print(f'Средняя оценка {some_student.name} {some_student.surname} хуже чем у {another_student.name} {another_student.surname}')

#Сравнение средней оценки лекторов
if some_lecturer > another_lecturer:
    print(f'Средняя оценка {some_lecturer.name} {some_lecturer.surname} лучше чем у {another_lecturer.name} {another_lecturer.surname}')
else:
    print(f'Средняя оценка {some_lecturer.name} {some_lecturer.surname} хуже чем у {another_lecturer.name} {another_lecturer.surname}')

#Подсчет средней оценки студентов по курсу
def avg_grade_students(students_list, course_name):
        total_grade = 0
        count = 0
        for student in students_list:
            if course_name in student.grades_stud:
                total_grade += sum(student.grades_stud[course_name])
                count += len(student.grades_stud[course_name])
        return round(total_grade / count, 1) if count > 0 else 0

#Подсчет средней оценки лекторов по курсу
def avg_grade_lectors(lectors_list, course_name):
        total_grade = 0
        count = 0
        for lecturer in lectors_list:
            if course_name in lecturer.grades_lect:
                total_grade += sum(lecturer.grades_lect[course_name])
                count += len(lecturer.grades_lect[course_name])
        return round(total_grade / count, 1) if count > 0 else 0

students = [some_student, another_student]
lectors = [some_lecturer, another_lecturer]

print(f'\nПроверяющие:\n{some_reviewer}\n\n{another_reviewer}\n')
print(f'Лекторы:\n{some_lecturer}\n\n{another_lecturer}\n')
print(f'Студенты:\n{some_student}\n{another_student}')
print(f'Средняя оценка студентов по курсу Python: {avg_grade_students(students, 'Python')}')
print(f'Средняя оценка лекторов по курсу Javascript: {avg_grade_lectors(lectors, 'Javascript')}')


