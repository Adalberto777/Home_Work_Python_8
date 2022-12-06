def write_id(id: str, donor_id: str,) -> None:
    with open(donor_id, 'w', encoding = "utf-8") as file:
        new_id = int(id) + 1
        file.write(str(new_id))