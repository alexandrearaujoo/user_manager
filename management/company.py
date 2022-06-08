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
        new_employee = vars(employee)

        new_employee['email'] = f'{new_employee["full_name"].replace(" ", "_").lower()}@{self.name.replace(" ", "").lower()}.com'
        new_employee['empresa'] = self.name

        if len(self.hired) == 0:
            self.hired.append(new_employee)
            return 'Funcionario cadastrado'

        for value in self.hired:
            if value["cpf"] == new_employee["cpf"]:
                return 'CPF ja cadastrado'
        
        self.hired.append(new_employee)
        

    def gerar_horelite(self, employee):
        new_employee = vars(employee)

        os.makedirs (f'./empresas/{self.name.lower().replace(" ", "_")}', exist_ok=True)
        with open(f'./empresas/{self.name.lower().replace(" ", "_")}/{new_employee["full_name"].lower().replace(" ", "_")}.json', 'w') as employee_file:
            json.dump(new_employee, employee_file, indent=4)

        

