def menu() -> str:
    print("MAIN MENU: \n"
            "1 - Create the new records in base\n"
            "2 - Show all records in concole\n"
            "3 - Delete an record by id\n"
            "4 - Update an record by id\n"
            "5 - Show an records by id in concole\n"
            "6 - Import all records from csv-file without id to txt-file\n"
            "7 - Import all records from csv-file with id to txt-file\n"
            "8 - Exit")
    result = input('Select a menu item: ')
    return result


def get_last_name() -> str:
    data = input('Enter last name: ')
    return data


def get_first_name() -> str:
    data = input('Enter name: ')
    return data


def get_group() -> str:
    data = input('Enter group: ')
    return data


def get_id() -> str:
    data = input('Enter id: ')
    return data