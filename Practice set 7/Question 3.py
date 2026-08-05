class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter 
    def salary(self, new_salary):
        if (new_salary < 0):
            print("Hey don't set a negative value for salary")
        else:
            self._salary = new_salary    

e = Employee(3000)
print(e.salary)
e.salary = 3500
print(e.salary)        