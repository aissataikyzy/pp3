class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        if not self.employees:
            print("Список сотрудников пуст")
        else:
            print("Список сотрудников:")
            for employee in self.employees:
                print(f"Имя: {employee.name}\n Должность: {employee.position}\n Зарплата: {employee.salary}\n")

    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

# Создание экземпляров класса "Employee"
employee1 = Employee("Иван Петров", "Инженер", 50000)
employee2 = Employee("Мария Иванова", "Дизайнер", 60000)

# Создание экземпляра класса "Company"
company = Company()

# Добавление сотрудников в компанию
company.add_employee(employee1)
company.add_employee(employee2)

# Вывод списка сотрудников
company.list_employees()

# Вычисление общей зарплаты
total_salary = company.calculate_total_salary()
print("Общая зарплата:", total_salary)
