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
            return 'Registered employee'

        return 'CPF already registered'
        

    def generate_horelite(self, employee):
        full_name_formated = snake_case(employee.full_name).lower()
        company_name_formated = snake_case(self.name).lower()


        if not employee.company == self.name:
           return False

        os.makedirs (f'./companies/{company_name_formated}', exist_ok=True)
        with open(f'./companies/{company_name_formated}/{full_name_formated}.json', 'w') as employee_file:
            json.dump(vars(employee), employee_file, indent=4)


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
        if employee in self.hired:
            self.hired.remove(employee)

            if employee.function == 'Employee':
                for value in self.hired:
                    if value.function == 'Manager':
                        value.employees.remove(employee)

            return f'{employee.function} fired'
        
        else:
            return 'CPF does not exists'

    def promotion(self, employee):
            if not employee in self.hired:
                return 'Employee does not exists'
            
            if not employee.function == 'Employee':
                return 'Promoted employee'

            employee.function = 'Manager'

            return employee
            


        
        

