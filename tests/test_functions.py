from utils import functions


test_file = [
    {
        "id": 285353808,
        "state": "EXECUTED",
        "date": "2018-08-06T16:22:54.643491",
        "operationAmount": {
            "amount": "82946.19",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 12189246980267075758"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
]

test_file_sort = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 285353808,
        "state": "EXECUTED",
        "date": "2018-08-06T16:22:54.643491",
        "operationAmount": {
            "amount": "82946.19",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 12189246980267075758"
    }
]


# def test_uploading_file():
#     assert functions.uploading_file('test_operations.json') == test_file


def test_sorting_operations():
    assert functions.sorting_operations(test_file) == test_file_sort


def test_transaction_output():
    assert functions.transaction_output(test_file_sort[0]["date"], test_file_sort[0]["description"]) == '03.07.2019 Перевод организации'


def test_account_transaction():
    assert functions.account_transaction(test_file_sort[0]) == 'MasterCard 7158 30** **** 6758 -> Счет **5560'
    assert functions.account_transaction(test_file_sort[1]) == 'Открытие вклада -> Счет **5758'


def test_quantity():
    assert functions.quantity(test_file_sort[0]["operationAmount"]) == '8221.37 USD'
