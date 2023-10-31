class Student:
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def get_age(self):
        age = 2023 - self.year
        return age
    
student1 = Student("Иван", "Иванов", 1995)
student2 = Student("Мария", "Петрова", 1998)

print("Полное имя студента 1:", student1.get_full_name())
print("Возраст студента 1:", student1.get_age())

print("Полное имя студента 2:", student2.get_full_name())
print("Возраст студента 2:", student2.get_age())
