from management.company import Company
from management.employee import Employee

def init():
    # funcionario = Employee('alexandre araujo', '12345678')
    # print(funcionario.__dict__)
    # print(funcionario)

    empresa_1 = Company("kenzie brasil", "12345678910124")
    # print(empresa_1.__dict__)
    # print(len(empresa_1))

    funcionario_1 = Employee("jordan cardoso poole", "32112343215")
    funcionario_2 = Employee("stephen alves curry", "12332145665")

    resposta = empresa_1.contratar_funcionario(funcionario_1.__dict__)
    empresa_1.contratar_funcionario(funcionario_2.__dict__)
    # print(resposta) 
    empresa_1.gerar_horelite(funcionario_1.__dict__)
    empresa_1.gerar_horelite(funcionario_2.__dict__)

if __name__ == "__main__":
    init()
