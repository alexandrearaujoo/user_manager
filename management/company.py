import os
import ujson as json

class Company:

    def __init__(self, name, cnpj, hired = []) -> None:
        self.name = name.title()
        self.cnpj = cnpj
        self.hired = hired

    def __len__(self):
        return len(self.hired)

    def contratar_funcionario(self,employee):
        

        employee.email = f'{employee.full_name.replace(" ", "_").lower()}@{self.name.replace(" ", "").lower()}.com'
        employee.empresa = self.name

        if not employee in self.hired:
            self.hired.append(employee)
            return 'Funcionario cadastrado'

        return 'CPF ja cadastrado'
        

    def gerar_horelite(self, employee):

        if not employee.empresa == self.name:
           return False

        os.makedirs (f'./empresas/{self.name.lower().replace(" ", "_")}', exist_ok=True)
        with open(f'./empresas/{self.name.lower().replace(" ", "_")}/{employee.full_name.lower().replace(" ", "_")}.json', 'w') as employee_file:
            json.dump(vars(employee), employee_file, indent=4)

