import os
import ujson as json

from helpers import remove_space, snake_case


class Company():

    def __init__(self, name, cnpj, hired = []) -> None:
        self.name = remove_space(name).title()
        self.cnpj = cnpj
        self.hired = hired

    def __len__(self):
        return len(self.hired)

    def hire_employee(self,employee):
        full_name_formated = snake_case(employee.full_name).lower()
        
        employee.email = f'{full_name_formated}@{self.name.replace(" ", "").lower()}.com'
        employee.company = self.name

        if not employee in self.hired:
            self.hired.append(employee)
            return f'Registered {employee.full_name} on {self.name}'

        return 'CPF already registered'
        

    def generate_horelite(self, employee):
        full_name_formated = snake_case(employee.full_name).lower()
        company_name_formated = snake_case(self.name).lower()


        if not employee.company == self.name:
           return False

        os.makedirs (f'./companies/{company_name_formated}', exist_ok=True)
        with open(f'./companies/{company_name_formated}/{full_name_formated}.json', 'w') as employee_file:
            json.dump(vars(employee), employee_file, indent=4)
            return f"{employee.full_name}'s horelite generated"


    @staticmethod
    def read_horelite(company, employee):
        try:
            company_name_formated = snake_case(company.name).lower()
            full_name_formated = snake_case(employee.full_name).lower()

            with open(f'./companies/{company_name_formated}/{full_name_formated}.json') as file:
                return json.load(file)
        except:
            return "Horelite does not exists"

    def resignation(self, employee):
        if not employee in self.hired:
            return 'CPF does not exists'

        if employee.function == 'Manager':
            self.hired.remove(employee)
            return f'{employee.function}: {employee.full_name} fired'

        if employee in self.hired:
            if not employee.company == self.name:
                return 'Employee does not belong to this company'
            for value in self.hired:
                if value.function == 'Manager':
                    self.hired.remove(employee)
                    value.employees.remove(employee)
                    return f'{employee.function}: {employee.full_name} fired'


    def promotion(self, employee):
            if not employee in self.hired:
                return 'Employee does not exists'
            
            if not employee.function == 'Employee':
                return 'Promoted employee'

            employee.function = 'Manager'

            return employee
            


        
        

