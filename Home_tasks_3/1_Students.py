# Создание класса "Студент" с атрибутами "имя", "фамилия", "курс", "средний балл".
# Реализовать методы для добавления и удаления студента, изменения данных студента, вывода информации о всех студентах, а также поиска студента по фамилии.
# импортируем класс
class Student:
    all_students=[]
    def __init__(self, first_name, last_name, year, gpa ):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.gpa = gpa
        Student.all_students.append(self)

    @classmethod
    def add_student(cls,student):
        cls.all_students.append(student)


    @classmethod
    def delete_student(cls, student):
        Student.all_students.remove(student)


    # def delete_student(self, student):
    #     self.all_students.remove(student)

    def change_course(self,year):
        self.year = year

    @classmethod
    def print_students(cls):
        for student in Student.all_students:
            print(student.first_name, student.last_name, student.year, student.gpa)

    @classmethod
    def search_student(cls,last_name):
        for students in Student.all_students:
            if last_name==students.last_name:
                print(students.first_name, students.last_name, students.year, students.gpa)

# создаем объекты студентов
student1 = Student("Иван", "Иванов", 3, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)

# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
Student.print_students()

# ищем студента по фамилии
Student.search_student("Иванов")

# удаляем студента
Student.delete_student(student2)


# выводим информацию о всех студентах

print('последний принт')
Student.print_students()