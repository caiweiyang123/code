class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(['a', 'b', 'c', 'd'])

# employee = company.employee
company1 = Company([1, 2, 3, 4, '5', '6', '7', 8])
company2 = company1[2:6]
for em in company2:
    print(em, type(em))
