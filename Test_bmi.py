import importlib
Lab2 = importlib.import_module("Lab-2")

def test_bmi_normal_weight():
    input_weight = 57
    input_height = 1.73

    result = Lab2.bmi.calculate_bmi(input_height, input_weight)

    assert(result==0)
def test_bmi_over_weight():
    input_weight = 72
    input_height = 1.65

    result = Lab2.bmi.calculate_bmi(input_height, input_weight)

    assert (result == 1)
def test_bmi_under_weight():
    input_weight = 59
    input_height = 1.81

    result = Lab2.bmi.calculate_bmi(input_height, input_weight)

    assert (result == -1)



