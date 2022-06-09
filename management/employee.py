from datetime import datetime as dt

from helpers import remove_space

class Employee:
    function = 'Employee'

    def __init__(self, full_name, cpf, wage = 3000, admission = dt.now()):
        self.full_name = remove_space(full_name).title()
        self.cpf = cpf
        self.wage = wage
        self.month = admission.strftime('%B')
        self.admission = admission.strftime('%d-%m-%Y')

    def __str__(self):
        return f'{Employee.function}: {self.full_name}'
