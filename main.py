from management.manager import Manager
from management.company import Company
from management.employee import Employee

def init():
    company_1 = Company(' gas company ', '1234567891011')
    company_2 = Company('  shoe company', '1234567891012')

    print('-' * 70)
    print(f'Companies\n\n{company_1.name}\n{company_2.name}')

    employee_alexandre = Employee('  alexandre  araujo  ', '12345678910')
    employee_paulo = Employee('  paulo  marioto   ', '12345678911', 5000)
    employee_luiz = Employee('   luiz  felipe  ', '12345678912', 6000)
    employee_iasmim = Employee('    iasmim  fernanda ', '12345678913', 7500)
    
    print('-' * 70)
    print(f'Employees\n\n{employee_alexandre}\n{employee_paulo}\n{employee_luiz}\n{employee_iasmim}')

    manager_pedro = Manager('  pedro  costa  ', '12345678914', 10000)
    manager_guilherme = Manager(' guilherme milek ', '12345678915', 9000)

    print('-' * 70)
    print(f'Managers\n\n{manager_pedro}\n{manager_guilherme}')

    admission_1 = company_1.hire_employee(employee_alexandre)
    admission_2 = company_1.hire_employee(employee_paulo)
    admission_3 = company_2.hire_employee(employee_iasmim)
    admission_4 = company_2.hire_employee(employee_luiz)

    print('-' * 70)
    print(f'New hires\n\n{admission_1}\n{admission_2}\n{admission_3}\n{admission_4}')

    pedro_admission_1 = company_1.hire_employee(manager_pedro)
    guilherme_admission_2 = company_2.hire_employee(manager_guilherme)

    print('-' * 70)
    print(f'New managers\n\n{pedro_admission_1}\n{guilherme_admission_2}')

    success_in_hiring_1 = manager_pedro.add_employee(employee_alexandre)
    success_in_hiring_2 = manager_pedro.add_employee(employee_paulo)

    same_person_1 = manager_pedro.add_employee(employee_alexandre)
    same_person_2 = manager_pedro.add_employee(employee_paulo)

    print('-' * 70)
    print(f'Success in hiring if it is from the same company as Pedro\n\n{success_in_hiring_1} - {employee_alexandre}\n{success_in_hiring_2} - {employee_paulo}')

    print('-' * 70)
    print(f"Attempt to register the same person in Pedro's company\n\n{same_person_1} - {employee_alexandre}\n{same_person_2} - {employee_paulo}")

    failed_in_hiring_1 = manager_guilherme.add_employee(employee_alexandre)
    failed_in_hiring_2 = manager_guilherme.add_employee(employee_paulo)

    print('-' * 70)
    print(f"Another company trying to hire employees from Pedro's company\n\n{failed_in_hiring_1} - {employee_alexandre} not from the same company")
    print(f'{failed_in_hiring_2} - {employee_paulo} not from the same company')

    success_in_hiring_1 = manager_guilherme.add_employee(employee_luiz)
    success_in_hiring_2 = manager_guilherme.add_employee(employee_iasmim)

    print('-' * 70)
    print(f'Success in hiring if it is from the same company as Guilherme\n\n{success_in_hiring_1} - {employee_luiz}')
    print(f'{success_in_hiring_2} - {employee_iasmim}')

    same_person_1 = manager_guilherme.add_employee(employee_luiz)
    same_person_2 = manager_guilherme.add_employee(employee_iasmim)

    print('-' * 70)
    print(f"Attempt to register the same person in Guilherme's company\n\n{same_person_1} - {employee_luiz}\n{same_person_2} - {employee_iasmim}")

    generate_employee_horelite = company_1.generate_horelite(employee_alexandre)
    generate_employee_horelite_2 = company_1.generate_horelite(employee_paulo)

    print('-' * 70)
    print(f"Successfully spawning a horelite from Pedro's company\n")
    print(f'{generate_employee_horelite}')
    print(f'{generate_employee_horelite_2}')

    failed_generate_horelite = company_1.generate_horelite(employee_iasmim)

    print('-' * 70)
    print('Failed to spawn a horelite\n')
    print(f'{failed_generate_horelite} - {employee_iasmim} does not a same company')

    generate_employee_horelite = company_2.generate_horelite(employee_luiz)
    generate_employee_horelite_2 = company_2.generate_horelite(employee_iasmim)

    print('-' * 70)
    print("Successfully spawning a horelite from Guilherme's company\n")
    print(f'{generate_employee_horelite}')
    print(f'{generate_employee_horelite_2}')

    read_employee_horelite = company_1.read_horelite(company_1, employee_alexandre)
    read_employee_horelite_2 = company_1.read_horelite(company_1, employee_paulo)

    print('-' * 70)
    print("Success when reading Pedro's company horelites\n")
    print(read_employee_horelite)
    print(read_employee_horelite_2)

    failed_read_horelite = company_1.read_horelite(company_1, employee_iasmim)

    print('-' * 70)
    print("Failed to read Pedro's company horelites\n")
    print(f'{failed_read_horelite} - {employee_iasmim} does not a same company')

    read_employee_horelite = company_2.read_horelite(company_2, employee_luiz)
    read_employee_horelite_2 = company_2.read_horelite(company_2, employee_iasmim)

    print('-' * 70)
    print("Success when reading Guilherme's company horelites\n")
    print(read_employee_horelite)
    print(read_employee_horelite_2)

    employee_dismissal_1 = company_1.resignation(employee_alexandre)

    print('-' * 70)
    print("Firing an employee of the Pedro's company\n")
    print(employee_dismissal_1)

    failed_dismissal = company_1.resignation(employee_iasmim)

    print('-' * 70)
    print("Trying to dismiss a employee of another company\n")
    print(failed_dismissal)


    print('-' * 70)
    print(f'Promoting employee\n')
    print(f'{employee_paulo.full_name} before: {employee_paulo.function}')
    company_1.promotion(employee_paulo)
    print(f'{employee_paulo.full_name} after: {employee_paulo.function}')

    failed_promo = company_1.promotion(employee_iasmim)

    print('-' * 70)
    print('Trying to promote an employee of another company\n')
    print(failed_promo)

    failed_promo_2 = company_1.promotion(manager_pedro)

    print('-' * 70)
    print('Trying to promote a manager\n')
    print(failed_promo_2)


    print('-' * 70)
    print(f'Increasing employee salary in 10%\n')
    print(f'{employee_paulo.full_name} before: {employee_paulo.wage}')
    manager_pedro.salary_increase(company_1, employee_paulo)
    print(f'{employee_paulo.full_name} after: {employee_paulo.wage}')

    failed_salary_increase = manager_pedro.salary_increase(company_2, employee_paulo)

    print('-' * 70)
    print('Trying to give a raise to an employee of another company\n')
    print(failed_salary_increase)    

    print('-' * 70)
    print('Earning promotion with salary above 8000 thousand\n')
    print(f'{employee_iasmim.full_name} before: {employee_iasmim.function} {employee_iasmim.wage}')
    manager_guilherme.salary_increase(company_2, employee_iasmim)
    print(f'{employee_iasmim.full_name} after: {employee_iasmim.function} {employee_iasmim.wage}')


if __name__ == "__main__":
    init()
