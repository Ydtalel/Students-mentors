from classes import *


def student_course_average(students_list, course):
    grades_list = []
    for student in students_list:
        if course in student.courses_in_progress:
            grades_list.extend(student.grades[course])
    average = sum(grades_list) / len(grades_list)
    return f"Cредняя оценка за домашние задания по всем студентам в рамках  курса {course} - {average}"


def lecturer_course_average(lecturers_list, course):
    grades_list = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            grades_list.extend(lecturer.grades[course])
    average = sum(grades_list) / len(grades_list)
    return f"Cредняя оценка за лекции всех лекторов в рамках курса {course} - {average}"


# _______________________________add two students________________________________
cool_student = Student('Cool', 'Student', 'female')
cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['GIT']
cool_student.finished_courses += ['SQL']
cool_student.finished_courses += ['GIT']

good_student = Student('Good', 'Student', 'male')
good_student.courses_in_progress += ['HTML']
good_student.finished_courses += ['GIT']
# ___________________________add some mentors_____________________________________
cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']
good_reviewer = Reviewer('Good', 'Reviewer')
good_reviewer.courses_attached += ['HTML']

cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']
good_lecturer = Lecturer('Good', 'Lecturer')
good_lecturer.courses_attached += ['HTML']
# ______________________give marks_______________________________________________
cool_reviewer.rate_hw(cool_student, 'Python', 9)
cool_reviewer.rate_hw(cool_student, 'Python', 8)
cool_reviewer.rate_hw(cool_student, 'Python', 10)

good_reviewer.rate_hw(good_student, 'HTML', 7)
good_reviewer.rate_hw(good_student, 'HTML', 8)
good_reviewer.rate_hw(good_student, 'HTML', 6)

cool_student.feedback(cool_lecturer, 'Python', 9)
cool_student.feedback(cool_lecturer, 'Python', 7)
cool_student.feedback(cool_lecturer, 'Python', 8)

cool_student.feedback(cool_lecturer, 'GIT', 5)
cool_student.feedback(cool_lecturer, 'GIT', 7)
cool_student.feedback(cool_lecturer, 'GIT', 9)

good_student.feedback(good_lecturer, 'HTML', 10)
good_student.feedback(good_lecturer, 'HTML', 6)
good_student.feedback(good_lecturer, 'HTML', 8)
# ____________________________make a few tests___________________________________________
# Задание № 3 пункт-1

print(" Вызываем магический метод __str__ у всех экземпляров классов\n")
print(*cool_student.students, sep='\n')
print(*good_lecturer.lecturers, sep='\n')
print(*good_reviewer.reviewers, sep='\n')

# Задание № 3 пункт-2

print("сравниваем (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней "
      "оценке за домашние задания.\n")
print(cool_student >= good_student, '\n')
print(good_lecturer >= cool_lecturer, '\n')

# Задание № 4. Полевые испытания

print(
    f"Все оценки лектора {cool_lecturer.name} за курс{cool_lecturer.grades}\nВсе оценки лектора {good_lecturer.name} "
    f"за курс {good_lecturer.grades}\n")
print(f"Все оценки студента {cool_student.name} за курс {cool_student.grades} \nВсе оценки студента {good_student.name}"
      f" за курс{good_student.grades} \n")
# Задание № 4.1-4.2
print(student_course_average(Student.students, 'Python'))
print(lecturer_course_average(Lecturer.lecturers, 'HTML'))
