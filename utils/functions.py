import json

def uploading_file():
    """достаем файлы из json"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        raw_json = json.load(file)
        return raw_json


def sorting_operations():
    """сортируем дынные: по 'CANCELED' и дате"""
    sort_state = []
    raw_json = uploading_file()
    for transaction in raw_json:
        if 'state' in transaction:
            if transaction['state'] == 'EXECUTED':
                sort_state.append(transaction)

    sort_state.sort(reverse = True, key=lambda x: x['date'])
    return sort_state


