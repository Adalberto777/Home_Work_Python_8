def del_record(data: dict, id: str) -> dict:
    id = int(id)
    data.pop(id)
    return data

  
def update_record(data: dict, id: str, last_name: str, name: str, group: str) -> dict:
    id = int(id)
    data[id] = last_name, name, group
    return data


def create_new_data(data_dict: dict, file_name_base: str) -> None:
    with open(file_name_base, mode = "w", encoding = "utf-8") as file:       
        for key, value in data_dict.items():
            data = ','.join(value)                   
            file.write(f'{key},{data},\n') 