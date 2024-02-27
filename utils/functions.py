import json

def uploading_file(file_transaction):
    """достаем файлы из json"""
    with open(file_transaction, 'r', encoding='utf-8') as file:
        raw_json = json.load(file)
        return raw_json


def sorting_operations(raw_json):
    """сортируем дынные: по 'CANCELED' и дате"""
    sort_state = []
    for transaction in raw_json:
        if 'state' in transaction:
            if transaction['state'] == 'EXECUTED':
                sort_state.append(transaction)

    sort_state.sort(reverse = True, key=lambda x: x['date'])
    return sort_state[:5]


def transaction_output(date, description):
    """
    передаем дату и вид операции
    :param date: дата платежа
    :param description: операция
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]} {description}"


def account_transaction(operation):
    """
    передаем счет отправителя и получателя
    """
    received = operation["to"]
    if "from" in operation:
        sent = operation["from"]
        return f"{sent[:-16]}{sent[-16:-12]} {sent[-12:-10]}** **** {sent[-4:]} -> Счет **{received[-4:]}"
    else:
        action = operation["description"]
        return f"{action} -> Счет **{received[-4:]}"

def quantity(operation):
    """
    передаем сумму и валюту
    """
    return f"{operation["amount"]} {operation["currency"]["name"]}"
