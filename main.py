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


# _______________________________________________________________________
cool_student = Student('Cool', 'Student', 'female')
cool_student.courses_in_progress += ['Python']
cool_student.finished_courses += ['SQL']
good_student = Student('Good', 'Student', 'male')
good_student.courses_in_progress += ['HTML']
good_student.finished_courses += ['GIT']

cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']
good_reviewer = Reviewer('Good', 'Reviewer')
good_reviewer.courses_attached += ['HTML']

cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python']
good_lecturer = Lecturer('Good', 'Lecturer')
good_lecturer.courses_attached += ['HTML']
# _____________________________________________________________________
cool_reviewer.rate_hw(cool_student, 'Python', 9)
cool_reviewer.rate_hw(cool_student, 'Python', 8)
cool_reviewer.rate_hw(cool_student, 'Python', 10)

good_reviewer.rate_hw(good_student, 'HTML', 7)
good_reviewer.rate_hw(good_student, 'HTML', 8)
good_reviewer.rate_hw(good_student, 'HTML', 6)

cool_student.feedback(cool_lecturer, 'Python', 9)
cool_student.feedback(cool_lecturer, 'Python', 7)
cool_student.feedback(cool_lecturer, 'Python', 8)

good_student.feedback(good_lecturer, 'HTML', 10)
good_student.feedback(good_lecturer, 'HTML', 6)
good_student.feedback(good_lecturer, 'HTML', 8)
# _______________________________________________________________________

print(
    f"Все оценки лектора {cool_lecturer.name} за курс{cool_lecturer.grades}\nВсе оценки лектора {good_lecturer.name} "
    f"за курс {good_lecturer.grades}\n")
print('\n', cool_student, '\n', good_student, '\n')
print('\n', cool_lecturer, '\n', cool_reviewer, '\n', good_reviewer, '\n', good_lecturer, '\n')
print(f"Все оценки студента {cool_student.name} за курс {cool_student.grades} \nВсе оценки студента {good_student.name}"
      f" за курс{good_student.grades} \n")
print(cool_student >= cool_lecturer, '\n')

print(student_course_average(Student.students, 'Python'))
print(lecturer_course_average(Lecturer.lecturers, 'HTML'))
