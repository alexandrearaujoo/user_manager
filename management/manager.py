from management.employee import Employee

class Manager(Employee):
    function = 'Gerente'

    def __init__(self, full_name, cpf, wage = 8000, employees = []):
        Employee.__init__(self, full_name, cpf, wage)
        self.employees = employees

    def __len__(self):
        return len(self.employees)

    def adicionar_funcionario(self, employee):   
        if not employee in self.employees:
            self.employees.append(vars(employee))
            print(self.employees)
            return True
        return False