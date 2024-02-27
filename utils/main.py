from utils.functions import uploading_file, sorting_operations, transaction_output, account_transaction, quantity


def main():
    file_transaction = 'operations.json'
    raw_json = uploading_file(file_transaction)    #получаем файлы из json
    sort_state = sorting_operations(raw_json)    #сортируем

    for operation in sort_state:    #выводим информацию
        print(transaction_output(operation["date"], operation["description"]))
        print(account_transaction(operation))
        print(quantity(operation["operationAmount"]))
        print()


if __name__ == "__main__":
    main()
