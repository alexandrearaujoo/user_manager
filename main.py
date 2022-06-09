from management.manager import Manager
from management.company import Company
from management.employee import Employee

def init():
    # funcionario = Employee('alexandre araujo', '12345678')
    # print(funcionario.__dict__)
    # print(funcionario)

    # empresa_1 = Company("kenzie brasil", "12345678910124")
    # print(empresa_1.__dict__)
    # print(len(empresa_1))

    # funcionario_1 = Employee("jordan cardoso poole", "32112343215")
    # funcionario_2 = Employee("stephen alves curry", "12332145665")

    # resposta = empresa_1.contratar_funcionario(funcionario_1.__dict__)
    # empresa_1.contratar_funcionario(funcionario_2.__dict__)
    # print(resposta) 
    # empresa_1.gerar_horelite(funcionario_1.__dict__)
    # empresa_1.gerar_horelite(funcionario_2.__dict__)

    gerente_1 = Manager(" bill    gates ", "32132186712", 10000)
    # gerente_2 = Manager(" billaaa", "32132186717", 10000)

    empresa_1 = Company("  kenzie    brasil ", "12345678910124")
    funcionario_1 = Employee(" jordan  cardoso poole ", "32112343215")

    # empresa_1.contratar_funcionario(funcionario_1.__dict__)
    # empresa_1.contratar_funcionario(gerente_1.__dict__)
    # empresa_1.contratar_funcionario(gerente_2.__dict__)

    empresa_2 = Company(" golden state warriors  ", "12345678910111")
    funcionario_3 = Employee("lamelo  ball souza ", "98778965434")
    # empresa_2.contratar_funcionario(funcionario_3.__dict__)

    # resposta = gerente_1.adicionar_funcionario(funcionario_1)
    # print(resposta) 

    # resposta = gerente_1.adicionar_funcionario(funcionario_1)
    # print(resposta) 

    # resposta = gerente_1.adicionar_funcionario(gerente_2)
    # print(resposta) 

    # print(f'FUNCIONARIOS: {len(gerente_1)}')

    # print(empresa_1.contratar_funcionario(funcionario_1))
    # print(vars(empresa_1.hired[0]))

    # print(empresa_1.contratar_funcionario(funcionario_1))
    # print(empresa_1.hired)

    # print(empresa_1.gerar_horelite(funcionario_1))

    # print(empresa_2.contratar_funcionario(funcionario_3))

    # print(empresa_2.gerar_horelite(funcionario_3))

    # print(gerente_1.adicionar_funcionario(funcionario_1))
    # print(vars(gerente_1.employees[0]))

    # print(gerente_1.adicionar_funcionario(funcionario_1))
    # print(vars(gerente_1.employees[0]))

    # print(empresa_1.contratar_funcionario(funcionario_1))

    # empresa_1.gerar_horelite(funcionario_1)

    # holerite = Company.ler_horelite(empresa_1, funcionario_1)

    # print(holerite)

    empresa_1 = Company("  kenzie   brasil ", 12345678910124)

    funcionario_1 = Employee(" jordan  cardoso poole ", 32112343215)

    gerente_1 = Manager(" bill    gates ", "32132186712")
    gerente_2 = Manager("elon musk", "12342186574")

    empresa_1.contratar_funcionario(funcionario_1)

    empresa_1.contratar_funcionario(gerente_1)

    empresa_1.contratar_funcionario(gerente_2)

    gerente_1.adicionar_funcionario(funcionario_1)

    funcionario_2 = Employee("klay mota thompson ", 92478965434)

    empresa_1.gerar_horelite(funcionario_1)

    holerite = Company.ler_horelite(empresa_1 ,funcionario_1)

    print(holerite)

    print(len(empresa_1.hired))

    resposta = empresa_1.demissao(funcionario_1)

    print(resposta) 

    resposta = empresa_1.demissao(gerente_1) 

    print(resposta) 

    print(len(gerente_1.employees)) 

    resposta = empresa_1.demissao(funcionario_1)

    # print(resposta) 

    print(len(gerente_1.employees))

    print(len(empresa_1.hired)) 

if __name__ == "__main__":
    init()
