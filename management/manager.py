from management.company import Company
from management.employee import Employee

class Manager(Employee):
    function = 'Manager'

    def __init__(self, full_name, cpf, wage = 8000, employees = []):
        Employee.__init__(self, full_name, cpf, wage)
        self.employees = employees

    def __len__(self):
        return len(self.employees)

    def add_employee(self, employee):   
        if employee.function == 'Manager' or employee.company != self.company:
            return False

        if not employee in self.employees:
            self.employees.append(employee)
            return True

    def salary_increase(self, company, employee):
        if not employee in self.employees:
            return False

        new_wage = 10 * employee.wage / 100
        employee.wage += new_wage

        if employee.wage > 8000:
            company.promotion(employee)

        return employee