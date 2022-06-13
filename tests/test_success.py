from unittest import TestCase

from management.company import Company
from management.employee import Employee
from management.manager import Manager

class TesteSuccess(TestCase):
    company_1 = Company(' gas company ', '1234567891011')
    company_2 = Company(' shoe company ', '1234567891013')

    def test_to_hire_employee(self):
        employee_alexandre = Employee('  alexandre  araujo  ', '12345678910')
        
        result = TesteSuccess.company_1.hire_employee(employee_alexandre)

        expect = f'Registered {employee_alexandre.full_name} on {TesteSuccess.company_1.name}'

        self.assertEqual(result, expect)

    def test_to_add_employee_on_manager(self):
        employee_alexandre = Employee('  alexandre  araujo  ', '12345678910')
        manager_pedro = Manager('  pedro  costa  ', '12345678914', 10000)

        TesteSuccess.company_1.hire_employee(employee_alexandre)
        TesteSuccess.company_1.hire_employee(manager_pedro)

        result = manager_pedro.add_employee(employee_alexandre)


        self.assertTrue(result)

    def test_to_generate_horelite(self):
        employee_alexandre = Employee('  alexandre  araujo  ', '12345678910')
        manager_pedro = Manager('  pedro  costa  ', '12345678914', 10000)

        TesteSuccess.company_1.hire_employee(employee_alexandre)
        TesteSuccess.company_1.hire_employee(manager_pedro)

        result = TesteSuccess.company_1.generate_horelite(employee_alexandre)

        expect = f"{employee_alexandre.full_name}'s horelite generated"

        self.assertEqual(result, expect)

    def test_to_read_horelite(self):
        employee_alexandre = Employee('  alexandre  araujo  ', '12345678910')
        manager_pedro = Manager('  pedro  costa  ', '12345678914', 10000)

        TesteSuccess.company_1.hire_employee(employee_alexandre)
        TesteSuccess.company_1.hire_employee(manager_pedro)

        TesteSuccess.company_1.generate_horelite(employee_alexandre)

        result = TesteSuccess.company_1.read_horelite(TesteSuccess.company_1, employee_alexandre)

        expect = {
            "full_name": "Alexandre Araujo",
            "cpf": "12345678910",
            "wage": 3000,
            "month": "June",
            "admission": "10-06-2022",
            "email": "alexandre_araujo@gascompany.com",
            "company": "Gas Company"
        }

        self.assertDictEqual(result, expect)

    def test_to_resignation_employee(self):
        employee_luiz = Employee('  luiz  felipe  ', '12345678913', 6000)
        employee_iasmim = Employee('  iasmim  fernanda   ', '12345678914', 7500)
        manager_guilherme = Manager('  guilherme  milek  ', '12345678915', 10000)

        TesteSuccess.company_2.hire_employee(employee_luiz)
        TesteSuccess.company_2.hire_employee(employee_iasmim)
        TesteSuccess.company_2.hire_employee(manager_guilherme)

        print(len(TesteSuccess.company_1.hired))

        result = TesteSuccess.company_2.resignation(employee_iasmim)
        expect = f'{employee_iasmim.function}: {employee_iasmim.full_name} fired'

        self.assertEqual(result, expect)


       
