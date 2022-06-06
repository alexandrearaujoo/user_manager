from management.employee import Employee

def init():
    funcionario = Employee('alexandre araujo', '12345678')
    print(funcionario.__dict__)
    print(funcionario)

if __name__ == "__main__":
    init()
