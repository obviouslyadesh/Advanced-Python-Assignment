class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

emp = Employee("John", 50000)


# print(emp.__salary)  # As it shows error so it is commented for demonstrating salary using getter and setter

print("Salary (using getter):", emp.get_salary())
emp.set_salary(55000)
print("Updated Salary (using setter):", emp.get_salary())
