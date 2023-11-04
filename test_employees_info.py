import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    result = []
    result = employee_info.get_employees_by_age_range(23, 30)

    assert len(result) == 1

def test_calculate_average_salary():
    avge_salary = employee_info.calculate_average_salary()

    assert (avge_salary==(50000+60000+56000+70000+65000+60000)/len(employee_data))

def test_get_employees_by_dept():
    result = []
    getEmployees = employee_info.get_employees_by_dept('Marketing')

    assert len(getEmployees) == 2