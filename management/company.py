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
        employee['email'] = f'{employee["full_name"].replace(" ", "_").lower()}@{self.name.replace(" ", "").lower()}.com'
        employee['empresa'] = self.name
        self.hired.append(employee)

    def gerar_horelite(self, employee):
        os.makedirs (f'./empresas/{self.name.lower().replace(" ", "_")}', exist_ok=True)
        with open(f'./empresas/{self.name.lower().replace(" ", "_")}/{employee["full_name"].lower().replace(" ", "_")}.json', 'w') as employee_file:
            json.dump(employee, employee_file, indent=4)

        

