class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students.append(self)

    def find_average(self):
        grades_dic = self.grades.values()
        grades_lst = [grade for grade_list in grades_dic for grade in grade_list]
        if len(grades_lst) != 0:
            average = sum(grades_lst) / len(grades_lst)
        else:
            average = sum(grades_lst)
        return average

    def __le__(self, other):
        return self.find_average() <= other.find_average()

    def __ge__(self, other):
        return self.find_average() >= other.find_average()

    def feedback(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and lecturer.courses_attached == self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average = self.find_average()
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: " \
               f"{average}\n Курсы в процессе изучения: {''.join(self.courses_in_progress)}\n" \
               f" Завершенные курсы: {''.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturers.append(self)

    def find_average(self):
        grades_dic = self.grades.values()
        grades_lst = [grade for grade_list in grades_dic for grade in grade_list]
        if len(grades_lst) != 0:
            average = sum(grades_lst) / len(grades_lst)
        else:
            average = sum(grades_lst)
        return average

    def __le__(self, other):
        return self.find_average() <= other.find_average()

    def __ge__(self, other):
        return self.find_average() >= other.find_average()

    def __str__(self):
        average = self.find_average()
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n " \
               f"Средняя оценка за лекции: {average}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
