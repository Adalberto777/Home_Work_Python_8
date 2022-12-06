
def create_new_record(last_name: str, name: str, group: str, id, file_name_base: str) -> None:
    with open(file_name_base, mode="a", encoding="utf-8") as file:
        file.write(f'{id},'
        f'{last_name},'
        f'{name},'
        f'{group}\n')        


