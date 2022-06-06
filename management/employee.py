from datetime import datetime as dt

class Employee:
    function = 'Employee'

    def __init__(self, full_name, cpf, wage = 3000, admission = dt.now()):
        self.full_name = full_name.title()
        self.cpf = cpf
        self.wage = wage
        self.admission = admission.strftime('%d-%m-%Y')

    def __str__(self):
        return f'{Employee.function}: {self.full_name}'
