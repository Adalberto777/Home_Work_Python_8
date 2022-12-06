def read_import_text(donor: str) -> str:
    with open(donor, "r", encoding = "utf-8") as file_data_donor:
        data = file_data_donor.read()
        data = ''.join(filter(lambda x: ' ' not in x, data.split()))
        data = data.split(',')
    return data


def create_new_data(data: str, donor: str) -> dict:
    data_dict = {}
    for i in range(0, len(read_import_text(donor)) - 3, 4):              
        data_dict[int(data[i])] = data[i + 1], data[i + 2], data[i + 3]
    return data_dict


def show_data(data: dict, id: str) -> dict:
    id = int(id)
    print(data[id])