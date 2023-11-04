import price_info

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def test_total_cost_shopping():
    expected_cost = (5 * 1.20) + (5 * 1.40) + (1 * 6.50) + (2 * 2.70) + (10 * 0.90) + (1 * 2.95) + (2 * 4.95)
    total_cost = price_info.total_cost_shopping()

    assert total_cost == expected_cost
def test_cost_of_fruit():
    cost = price_info.cost_of_fruits("apple", 12)

    assert (cost == 12 * 1.20)